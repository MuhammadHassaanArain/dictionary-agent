import asyncio
from tools.tools import get_meaning
from agents import Agent,Runner
from configuration import config,model,session
from agents import InputGuardrailTripwireTriggered 
async def main(user_input:str):
    agent =Agent(
        name = "Dictionary Agent",
        instructions="You are a dictionary agent who provides a word's definition, synonyms, antonyms, part of speech, example sentences, and pronunciation if available.",
        model =model,
        tools=[get_meaning],
    )
    try:
        result =  Runner.run_streamed(agent, user_input, run_config=config, session=session)
        return result
    except Exception as e:
        return f"❗ An unexpected error occurred: {str(e)}"
