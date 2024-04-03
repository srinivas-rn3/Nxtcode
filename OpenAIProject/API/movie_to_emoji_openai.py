import os,sys
import openai

sys.path.append("C:/Users/srini/git/Nxtcode/IT AUTOMATION/.vscode/OpenAIProject")

import constants
openai.api_key = constants.OPENAI_API_KEY

print("Program to convert movie name to emoji\n")
gpt_prompt = input('Enter tthe movie name :  ')

response = openai.Completion.create(
  model="text-davinci-003",
  prompt= gpt_prompt,
  temperature=0.8,
  max_tokens=60,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0,
  stop=["\\n"]
)
#print(response['choices'][0]['text'])
print(response)