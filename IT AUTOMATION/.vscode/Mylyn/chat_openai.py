
import openai
openai.api_key = 'sk-254OjIkmQsxxTnKnc2WVT3BlbkFJaOYUQ61A3hQEox2gCg02apple'
messages = [ {"role": "system", "content": 
              "You are a intelligent assistant."} ]
while True:
    message = input("User : ")
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})