import os
import openai
import constants as co

# Load your API key from an environment variable or secret management service
openai.api_key = co.OPENAI_API_KEY
'''
print(openai.api_key)
response = openai.Completion.create(model="text-davinci-003", 
                                    prompt="Say this is a test", 
                                    temperature=0, max_tokens=7)
'''
openai.Completion.create(
  model="text-davinci-003",
  prompt="Say this is a test",
  max_tokens=7,
  temperature=0
)
