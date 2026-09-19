
from dotenv import *

load_dotenv(find_dotenv())


# source .venv/bin/activate
# from openai import OpenAI

# client = OpenAI()

# response = client.responses.create(
#     model="gpt-6-astra",
#     input="Write a one-sentence bedtime story about a unicorn.",
# )

# print(response.output_text)

from google import genai

client = genai.Client()

def getResponse(input:str, previous_interaction_id:str = None):
    interaction = client.interactions.create(
        model="gemini-3.5-flash-lite",
        input= input,
        previous_interaction_id=previous_interaction_id,
    )


    return interaction.id, interaction.output_text

if __name__ == "__main__":
        None
