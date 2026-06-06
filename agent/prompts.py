
def planner_prompt(user_prompt : str) -> str:

    PLANNER_PROMPT = f"""
        You are a PLANNER agent. Convert the user prompt into a COMPLETE engineering project plan 

        USER Request: {user_prompt}
        """
    return PLANNER_PROMPT


