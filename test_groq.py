from groq import Groq

client = Groq(api_key="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")
completion = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {
            "role": "user",
            "content": "Hola, ¿puedes decirme en qué año se fundó Google?"
        }
    ],
    temperature=1,
    max_completion_tokens=1024,
    top_p=1,
    stream=True,
    stop=None,
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")
