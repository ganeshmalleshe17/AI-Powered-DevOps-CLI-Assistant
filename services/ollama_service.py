from ollama import chat
from services.prompt_loader import load_prompt


def generate_response(template_name, user_prompt):

    prompt = load_prompt(template_name, user_prompt)

    response = chat(
        model="qwen2.5:3b",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    return response["message"]["content"]
