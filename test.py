from ollama import chat

response = chat(
    model="qwen2.5:3b",
    messages=[
        {
            "role": "system",
            "content": "You are a DevOps engineer. Always return only code without explanation."
        },
        {
            "role": "user",
            "content": "Generate only a Dockerfile for a Flask application."
        }
    ]
)

print(response["message"]["content"])
