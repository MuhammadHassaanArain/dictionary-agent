# from agents import (
#     Agent,
#     GuardrailFunctionOutput,
#     RunContextWrapper,
#     Runner,
#     TResponseInputItem,
#     input_guardrail,
# )


# from configuration import config,session
# from pydantic import BaseModel


# class LanguageCheckOutput(BaseModel):
#     is_english: bool
#     detected_lang: str

# class AbuseCheckOutput(BaseModel):
#     is_abusive: bool
#     message: str


# language_guardrail_agent = Agent(
#     name="Language Detector",
#     instructions="""
# Detect if the user input is in English.
# - Return is_english=true if it's English, else false.
# - Also return detected language name.
# """,
#     output_type=LanguageCheckOutput,
# )

# abuse_guardrail_agent = Agent(
#     name="Abuse Checker",
#     instructions="""
# Detect if the user input contains any abusive, sexual, or offensive content
# (in any language, creative spellings, or obfuscated forms).
# Return is_abusive=true if found, else false.
# Also return a message explaining why if abusive.
# """,
#     output_type=AbuseCheckOutput,
# )
# def extract_input_text(input):
#     if isinstance(input, str):
#         return input
#     elif isinstance(input, list) and isinstance(input[0], dict):
#         # Try common keys
#         return input[0].get("text") or input[0].get("content") or str(input[0])
#     else:
#         return str(input)


# @input_guardrail
# async def english_only_guardrail(
#     ctx: RunContextWrapper[None],
#     agent: Agent,
#     input: str | list[TResponseInputItem]
# ) -> GuardrailFunctionOutput:
#     input_str = extract_input_text(input)
#     result = await Runner.run(language_guardrail_agent, input=input_str ,context=ctx.context, run_config=config, session=session)
#     output = result.final_output_as(LanguageCheckOutput)
#     return GuardrailFunctionOutput(
#         output_info=result.final_output,
#         tripwire_triggered=not output.is_english
#     )

# @input_guardrail
# async def abuse_check_guardrail(
#     ctx: RunContextWrapper[None],
#     agent: Agent,
#     input: str | list[TResponseInputItem]
# ) -> GuardrailFunctionOutput:
#     input_str = extract_input_text(input)
#     result = await Runner.run(abuse_guardrail_agent, input=input_str, context=ctx.context,run_config=config, session=session)
#     output = result.final_output_as(AbuseCheckOutput)
#     print(f"Input: {input_str}, Detected: {output.detected_lang}, Is English: {output.is_english}")
#     return GuardrailFunctionOutput(
#         output_info=result.final_output,
#         tripwire_triggered=output.is_abusive
#     )
