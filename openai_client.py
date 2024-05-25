import os
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

from prompts_presets import DEFAULT_PROMPT

import json

load_dotenv(find_dotenv())


client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def ansver_gpt(prompt):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"{DEFAULT_PROMPT  + prompt}",
            }
        ],
        model="gpt-4o",
    )

    return json.loads(chat_completion.model_dump_json())['choices'][0]['message']['content']