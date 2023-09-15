import openai

# Set your OpenAI API key here
api_key = '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'

# Define the input prompt
input_prompt = "Translate the following English text to French:"

# Initialize the OpenAI API client
openai.api_key = api_key

# Create a function to generate text based on a prompt
def generate_text(prompt, max_tokens=50, engine="text-davinci-002"):
    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        max_tokens=max_tokens
    )
    return response.choices[0].text

# Generate text using the input prompt
generated_text = generate_text(input_prompt)

# Print the generated text
print("Generated Text:")
print(generated_text)

