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
