import os
#os.environ["OPENAI_API_TYPE"] = "azure"
#os.environ["OPENAI_API_VERSION"] = "2023-05-15"
#os.environ["OPENAI_API_BASE"] = "https://chatlogo.openai.azure.com"
os.environ["OPENAI_API_KEY"] = os.environ['OPENAI_API_KEY']
import openai

'''
def get_openai1():
    from langchain.llms import AzureOpenAI
    llm = AzureOpenAI(
        deployment_name="davinci-003",
        max_tokens=2000,
        temperature=0.2
    )
    return llm
'''

def get_openai(text):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=text,
        temperature=0.3,
        max_tokens=2000,
    )
    return response.choices[0].text.strip()


def get_gpt_response(system_prompt, user_prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.4,
        max_tokens=2048,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    
    reply = response.choices[0].message.get('content')
    return reply
