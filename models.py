import os
from interface import getPrompt
from groq import Groq
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# Buscando o prompt
def getPrompt():
    mensagem = input(" ")
    return mensagem

prompt = getPrompt()
client = Groq(
    api_key=os.environ.get(api_key),
)
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": f'{prompt}',
        }
    ],
    model="llama3-8b-8192",
)

print(chat_completion.choices[0].message.content)