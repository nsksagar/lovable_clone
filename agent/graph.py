from langchain_groq import ChatGroq
from dotenv import load_dotenv

from prompts import *
from states import *

from langgraph.constants import END
from langgraph.graph import StateGraph


user_prompt = 'create a simple calculator web application'

load_dotenv()

llm = ChatGroq(model = 'llama-3.3-70b-versatile')

def planner_agent(state: dict)-> dict:
    user_prompt = state['user_prompt']
    resp = llm.with_structured_output(Plan).invoke(planner_prompt(user_prompt))
    return {"plan" : resp}

graph = StateGraph(dict)
graph.add_node("planner", planner_agent)
graph.set_entry_point('planner')

agent = graph.compile()

user_prompt = "create a simple calculator web application"

result = agent.invoke({"user_prompt" : user_prompt})

print(result)
