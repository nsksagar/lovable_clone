from langchain_groq import ChatGroq
from dotenv import load_dotenv
from pydantic import BaseModel, Field


user_prompt = 'create a simple calculator web application'

prompt = f"""
        You are a PLANNER agent. Convert the user prompt into a COMPLETE engineering project plan 

        USER Request: {user_prompt}
"""

load_dotenv()

llm = ChatGroq(model = 'llama-3.3-70b-versatile')

#Schema is a class which you import from pydantic basemodel 
class Plan:


resp = llm.with_structured_output(Plan).invoke(prompt)

print(resp)