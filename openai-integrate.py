import openai

client = openai.OpenAI(api_key="your_openai_api_key")

completion = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Which number is larger, 9.11 or 9.8?"}],
    temperature=0.6,
    top_p=0.7,
    max_tokens=50,
    stream=True
)

for chunk in completion:
    if chunk.choices[0].delta.get("content"):
        print(chunk.choices[0].delta["content"], end="")
