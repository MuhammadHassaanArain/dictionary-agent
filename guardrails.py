
from configuration import config
from pydantic import BaseModel
from agents import (
    GuardrailFunctionOutput,
    input_guardrail,
    TResponseInputItem,
    RunContextWrapper,
    Runner,
    Agent,
)

class LanguageCheckOutput(BaseModel):
    is_english: bool
    reasoning: str

class AbuseCheckOutput(BaseModel):
    is_abusive: bool
    reasoning: str


language_guardrail_agent = Agent(
    name="Language Detector",
    instructions="""
Detect if the user input is in English.
- Return is_english=true if it's English, else false.
- Also return detected language name.
""",
    output_type=LanguageCheckOutput,
)
abuse_guardrail_agent = Agent(
    name="Abuse Checker",
    instructions="""
Detect if the user input contains any abusive, sexual, or offensive content
(in any language, creative spellings, or obfuscated forms).
Return is_abusive=true if found, else false.
Also return a message explaining why if abusive.
""",
    output_type=AbuseCheckOutput,
)

@input_guardrail
async def english_only_guardrail(ctx: RunContextWrapper[None], agent: Agent, input: str | list[TResponseInputItem]) -> GuardrailFunctionOutput:
    result = await Runner.run(language_guardrail_agent, input ,context=ctx.context, run_config=config, )
    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered= not result.final_output.is_english,
    )

@input_guardrail
async def abuse_check_guardrail( ctx: RunContextWrapper[None], agent: Agent, input: str | list[TResponseInputItem]) -> GuardrailFunctionOutput:
    result = await Runner.run(abuse_guardrail_agent, input, context=ctx.context,run_config=config, )
    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=result.final_output.is_abusive,
    )
