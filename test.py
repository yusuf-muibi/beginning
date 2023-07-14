import requests
import json

API_KEY = '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'
API_ENDPOINT = 'https://api.openai.com/v1/engines/davinci-codex/completions'

user_name = input('Hello there, welcome to the ITSupportBot test. Kindly provide your first name: ')
print('Hello', user_name)

user_issue = input('How may I be of assistance to you today? ')

headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
}

data = {
    'prompt': user_issue,
    'max_tokens': 50  # Adjust this value based on the desired response length
}

json_data = json.dumps(data)

response = requests.post(API_ENDPOINT, headers=headers, data=json_data)

response_data = response.json()
generated_text = response_data['choices'][0]['text']['content']

print('Generated Text:')
print(generated_text)
