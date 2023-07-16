import openai
openai.api_key = "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"

prompt = "Create a 200 word short story which includes many language features"
response = openai.Completion.create(
  engine="text-davinci-003",
  prompt=prompt,
  max_tokens=50
)

generated_text = response.choices[0].text.strip()
print(generated_text)
