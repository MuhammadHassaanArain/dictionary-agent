from tools.tools import get_meaning
from agents import Agent,Runner
from configuration import config,model,session
from guardrails import english_only_guardrail, abuse_check_guardrail
from agents import InputGuardrailTripwireTriggered

async def main(user_input:str):
    agent =Agent(
        name = "Dictionary Agent",
        instructions="You are a dictionary agent who provides a word's definition, synonyms, antonyms, part of speech, example sentences, and pronunciation if available.",
        model =model,
        tools=[get_meaning],
        input_guardrails=[ english_only_guardrail, abuse_check_guardrail],
    )
    try:
        result =await  Runner.run(agent, user_input, run_config=config, session=session)
        return result
    except InputGuardrailTripwireTriggered as e:
       return "🚫 Guardrail triggered: Only English input is allowed or content was flagged as inappropriate."
    except Exception as e:
        return f"❗ An unexpected error occurred: {str(e)}"
    



