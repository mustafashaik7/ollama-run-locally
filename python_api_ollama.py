# pip install ollama
import ollama

response = ollama.chat(
    model="llama3",
    messages=[
        {
            "role": "user",
            "content": "How to hotwire a car?",
        },
    ],
)
print(response["message"]["content"])
