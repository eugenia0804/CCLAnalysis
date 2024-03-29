from code.utils import get_questions, get_answers,
from prompts import formulate_chat_prompt
from llm import get_gpt_response
import json
import pandas as pd
import re
import sys
import os
import importlib

index = int(os.environ.get('index', 0))
iteration = int(os.environ.get('iteration', 0))

prompt = importlib.import_module(f'iteration-{str(iteration)}.prompt-iteration-{str(iteration)}')


def classify_questions(index,start_q,end_q):
  if iteration <= 3:
    prompt = prompt.formulate_prompt(index, start_q, end_q)
    result = get_openai(prompt)
  else:
    sys_prompt, usr_prompt = prompt.formulate_chat_prompt(index,start_q,end_q)
    result = get_gpt_response(sys_prompt, usr_prompt) 
  print('llm completed')
  return sys_prompt + usr_prompt , result

def store_result(index,start_q,end_q,iteration): 
  [prompt, results] = classify_questions(index,start_q,end_q)
  filename = 'results/iteration-'+str(iteration)+'/prompts/'+str(start_q)+'to'+str(end_q)+'.txt'
  with open(filename, 'w', encoding='utf-8') as file:
    file.write(prompt)
  filename = 'results/iteration-'+str(iteration)+'/raw_results/'+str(start_q)+'to'+str(end_q)+'.txt'
  with open(filename, 'w', encoding='utf-8') as file:
    json.dump(results, file)
    
  final_result = {}
  input_str = results.strip()#.replace("'", '"')
  '''
  raw_string = re.sub(r'"(.*?)"', r"'\1'", results)
  string = re.sub(r"'(.*?)':", r'"\1":', results)
  i_str = re.sub(r"'(.*?)',", r'"\1",', string)
  input_str = re.sub(r"'(.*?)'}}", r'"\1"}}', i_str)
  '''

  print(input_str)
  json_res = json.loads(input_str)
  correct_answers = get_answers(index, start_q, end_q)
  for i, (key, value) in enumerate(json_res.items()):
    correct_answer = "No"
    if correct_answers[i] == 1:
        correct_answer = "Yes"
    value["Correct Answer"] = correct_answer
    final_result[key] = value
  
  with open('results/iteration-'+str(iteration)+'/results/'+str(start_q)+'to'+str(end_q)+'.json', 'w') as file:
    json.dump(final_result, file)

    
  return final_result
    
#store_result(index = 2, start_q = 1,end_q = 3)

def run_all(index, iteration):
  question_df = get_questions()
  num_questions = question_df.shape[0]
  result_dict = {}
  for i in range(1, num_questions, 10):
    result_dict.update(store_result(index, i, i+9, iteration))
  keys = result_dict.keys()
  with open('results/iteration-'+str(iteration)+'/final/1to'+str(num_questions-80)+'.json', 'w') as file:
    json.dump(result_dict, file)
  return 


print('work-stream began')
run_all(index, iteration)

