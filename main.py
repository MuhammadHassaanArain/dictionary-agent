import chainlit as cl
from agent import main
from agents import ItemHelpers
from agents import enable_verbose_stdout_logging
enable_verbose_stdout_logging()

@cl.on_chat_start
async def start_chating():
    await cl.Message(content="Ask me about any Word.").send()

@cl.on_message
async def message(message:cl.Message):
    res = await  main(message.content)
    if isinstance(res, str):
        await cl.Message(content=res).send()
        return
    final_output = res.final_output
    await cl.Message(content=f"{final_output}").send()

