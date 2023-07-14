import flask
import requests
API_KEY = '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'
API_ENDPOINT = 'https://api.openai.com/v1/engines/davinci-codex/completions'
user_name = input('Hello there, welcome to the ITSupportBot test, kindly provide your first name')
print('Hello', user_name)
user_issue = input ('How may I be of assistance to you today')

headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
}
data = {
    'prompt': user_issue,
    'max_tokens': 50  # Adjust this value based on the desired response length
}
response = requests.post(API_ENDPOINT, headers=headers, json=data)