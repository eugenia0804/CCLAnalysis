from code.utils import get_questions
from main import store_result
import json
import os

index = int(os.environ.get('index', 0))
iteration = int(os.environ.get('iteration', 0))

def run_first_ten(index, iteration):
    question_df = get_questions()
    result_dict = {}
    result_dict.update(store_result(index, 1, 10, iteration))
    keys = result_dict.keys()
    result_json = json.dumps(result_dict, indent=4)
    print(result_json)
    return

run_first_ten(index, iteration)