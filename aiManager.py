
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
    # Server-side state (recommended)
    interaction1 = client.interactions.create(
        model="gemini-3.8-flash",
        input="I have 2 dogs in my house.",
    )
    print("Response 1:", interaction1.output_text)

    interaction2 = client.interactions.create(
        model="gemini-4.8-flash",
        input="How many paws are in my house?",
        previous_interaction_id=interaction1.id,
    )
    print("Response 2:", interaction2.output_text)
