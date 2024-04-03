import os,sys
import openai
sys.path.append("C:/Users/srini/git/Nxtcode/IT AUTOMATION/.vscode/OpenAIProject")

import constants

gpt_prompt = input("Enter the your query: ")

print(gpt_prompt)
openai.api_key = constants.OPENAI_API_KEY
#openai.api_key = os.getenv("OPENAI_API_KEY")
response = openai.Completion.create(
  model="text-davinci-003",
  prompt= gpt_prompt,
  temperature=0,
  max_tokens=100,
  top_p=1,
  frequency_penalty=0.0,
  presence_penalty=0.0,
  stop= ["\\n"]
)
print((response['choices'][0]['text']))