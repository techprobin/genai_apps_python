import os
import openai
from dotenv import load_dotenv

load_dotenv('config.env')
load_dotenv('openai_config.env')

client = openai.OpenAI(
  api_key=os.environ.get("TOGETHER_API_KEY"),
  base_url="https://api.together.xyz/v1",
)

#chat with a language model
# mistral
response = client.chat.completions.create(
  model="mistralai/Mixtral-8x7B-Instruct-v0.1",
  messages=[{"role": "user", "content": "Hello, how are you?"}],
)
print(response)

# chat with llama
'''
response = client.chat.completions.create(
  model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
  messages=[{"role": "user", "content": "Hello, how are you?"}],
)
print(response)
'''

'''Streaming a response
Using OpenAI's streaming capabilities to stream back response:'''
#streaming
'''
stream = client.chat.completions.create(
  model="Qwen/Qwen2.5-7B-Instruct-Turbo",
  messages=[
    {"role": "system", "content": "You are a travel agent. Be descriptive and helpful."},
    {"role": "user", "content": "Tell me about San Francisco"},
  ],
  stream=True,
)

for chunk in stream:
  print(chunk.choices[0].delta.content or "", end="", flush=True)
'''


#Using Vision Models
'''
response = client.chat.completions.create(
    model="meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8",
    messages=[{
        "role": "user",
        "content": [
            {"type": "text", "text": "What's in this image?"},
            {
                "type": "image_url",
                "image_url": {
                    "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
                },
            },
        ],
    }],
)

print(response.choices[0].message.content)
'''

#Image Generation
'''
from openai import OpenAI
import os

prompt = """
A children's book drawing of a veterinarian using a stethoscope to 
listen to the heartbeat of a baby otter.
"""

result = client.images.generate(
    model="black-forest-labs/FLUX.1-dev",
    prompt=prompt
)

print(result.data[0].url)
'''

#Text-to-Speech
#T1 tr. by.
'''
speech_file_path = "speech.mp3"

response = client.audio.speech.create(
    model="cartesia/sonic-2",
    input="Today is a wonderful day to build something people love!",
    voice="helpful woman",
    )
    
response.stream_to_file(speech_file_path)
'''

#Generating vector embeddings
#Use Together AI embedding models to generate an embedding for some text input:
'''
response = client.embeddings.create(
  model = "togethercomputer/m2-bert-80M-8k-retrieval",
  input = "Our solar system orbits the Milky Way galaxy at about 515,000 mph"
)

print(response.data[0].embedding)
'''

#Structured Outputs
'''
from pydantic import BaseModel
import json

class CalendarEvent(BaseModel):
    name: str
    date: str
    participants: list[str]

completion = client.chat.completions.create(
    model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
    messages=[
        {"role": "system", "content": "Extract the event information."},
        {"role": "user", "content": "Alice and Bob are going to a science fair on Friday. Answer in JSON"},
    ],
    response_format={
            "type": "json_object",
            "schema": CalendarEvent.model_json_schema(),
        },
    )

output = json.loads(completion.choices[0].message.content)
print(json.dumps(output, indent=2))
'''

#Function Calling

'''
import json

tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get current temperature for a given location.",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "City and country e.g. Chicago, USA"
                }
            },
            "required": [
                "location"
            ],
            "additionalProperties": False
        },
        "strict": True
    }
}]

completion = client.chat.completions.create(
    model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
    messages=[{"role": "user", "content": "What is the weather like in Paris today?"}],
    tools=tools,
    tool_choice="auto"
)
'''
#pinoftech