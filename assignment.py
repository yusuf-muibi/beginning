import openai
openai.api_key = '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'
def user_request(user_input):
    response = openai.Completion.create(
    engine='text-davinci-003',
    prompt=user_input,
    max_tokens=100,  # Adjust the desired response length
    n=1,  # Generate a single response
    stop=None,  # Define a stop condition if needed
    temperature=0.7,  # Control the randomness of the response
    timeout=20,  # Set a timeout value (optional)
    )
    return response.choices[0].text.strip()
print("How may I be of assistance to you today?")
while True:
    user_input = input("User: ")
    response = user_request(user_input)
    print("ChatGPT: " + response)