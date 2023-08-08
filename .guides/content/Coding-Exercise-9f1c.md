Write a function called `generate_response` that takes a prompt and model as input and returns the generated response using the `openai.Completion.create method`. The function should have the following signature:
```python
def generate_response(prompt, model):
  #your code should be below this line
    return response.choices[0].text.strip()
```

{Try it!}(python exerc.py)


{Check It!|assessment}(code-output-compare-3200389207)


|||guidance
```python
def generate_response(prompt: str, model: str) -> str:
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
    )

    return response.choices[0].text.strip()
```
|||