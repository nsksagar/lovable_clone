from langchain_groq import ChatGroq
from dotenv import load_dotenv

from prompts import *
from states import *


user_prompt = 'create a simple calculator web application'

prompt = planner_prompt(user_prompt)

load_dotenv()

llm = ChatGroq(model = 'llama-3.3-70b-versatile')



resp = llm.with_structured_output(Plan).invoke(prompt)

print(resp)