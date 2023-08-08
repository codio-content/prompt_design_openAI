import os
import openai
import secret
openai.api_key=secret.api_key


# Define the generate_response function as shown


# CODIO SOLUTION BEGIN
def generate_response(prompt, model):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
    )

    return response.choices[0].text.strip()
# CODIO SOLUTION END