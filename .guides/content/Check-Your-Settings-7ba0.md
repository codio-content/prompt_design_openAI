##

## Keyword Arguments

As important as the prompt is, it is only one component of generating a response from the GPT-3 model. Let's leave the OpenAI playground and return to the Python language. We pass the `openai.Completion.create` method a variety of keyword arguments. The `prompt` is but one of these keyword arguments. By focusing on the interplay between these keyword arguments, we can improve the quality of the responses.

```python-hide-clipboard
response = openai.Completion.create(
  model="text-davinci-002",
  prompt="",
  temperature=0,
  max_tokens=25,
  top_p=0,
  frequency_penalty=0,
  presence_penalty=0
)
```

In particular, keep a close eye on `temperature` and `top_p`. These keyword arguments control how deterministic the model is when generating a response. That is, adjusting the values of these keyword arguments can create a result that does not change much (if at all) each time the model runs.

Let's set the temperature to `0.1` and try it with the prompt `when did dadism start`. This value increases the model's confidence in its top choice.
The closer your temperature is to 0, the more deterministic the model will become. This means you may see very little variance or "creativity" in the response. Instead, you should see a rather matter-of-fact statement.

```python
prompts ="when did dadism start?"

response = openai.Completion.create(
  model="text-davinci-002",
  prompt=prompts,
  temperature=0.1)

print(response['choices'][0]['text'].strip())
```

{Try it!}(python3 setting.py)

|||challenge
## Try this variation:

* Try running the code multiple times when you set `temperature` to `1`. You should now see more variance or "creativity" in the responses.

```python
response = openai.Completion.create(
  model="text-davinci-002", 
  prompt=prompts,
  temperature=1)
```

{Try it!}(python3 setting.py 2)
|||

Now let's take a look at `top_p`. This keyword argument sets the scope of the potential results. The larger the value, the greater number of potential responses the model will consider the best result. Set the value of `top_p` to `1` and run the code a few times. You should see a variety in responses each time the code runs.

```python
response = openai.Completion.create(
  model="text-davinci-002",
  prompt=prompts,
  top_p=1)
```

{Try it!}(python3 setting.py 3)

|||challenge
## Try this variation:

* Try running the code multiple times when you set `top_p` to `0.1`. In this example, you are limiting the responses to the 10% of the possible answers. This means the potential responses are limited in nature and therefore more deterministic.

```python
response = openai.Completion.create(
  model="text-davinci-002", 
  prompt=prompts,
  top_p=0.1)
```

{Try it!}(python3 setting.py 4)
|||

## Combining `top_p` and `temperature`

Both the `top_p` and `temperature` are correlated, which means using one affects the results of the other. Be careful in how you use these two keyword arguments. Take a look at the example below. The `temperature` keyword argument should maximize creativity. However, `top_p` limits the results to only the top 10%. That means the `top_p` value counteracts the `temperature` value, and the results will be more deterministic rather than creative.

```python
response = openai.Completion.create(
  model="text-davinci-002", 
  prompt=prompts,
  temperature=1,
  top_p=0.1)
```

{Try it!}(python3 setting.py 5)

Keep in mind how these two keyword arguments work together. Starting out, it might be best to use either `top_p` or `temperature` to control variance in responses. This way you will not "undo" one keyword argument with the other.

top_p is a hyperparameter that controls the cumulative probability cutoff for the set of next possible words the model can choose during generation. If top_p is set to 0.95, for example, the model will consider the smallest set of next possible words whose combined probability exceeds 0.95.

## Troubleshooting Tips
If you're having trouble getting the API to perform as expected, follow this checklist:

* Is it clear what the intended generation should be?
* Are there enough examples?
* Did you check your examples for mistakes? (The API won't tell you directly)
* Are you using `temperature` and `top_p` correctly?
* Are your other settings being used correctly?

The last tip may seem a bit vague. To illustrate this point, change the prompt so that it is asking for the sentiment of each sentence.

```python
prompts ="what is the overall sentiment for each of the following sentences:['i am happy','i am happy to be sad','I am sad']"
```

Run the script once more. You should notice that the response is incomplete. The response ends before describing the sentiment of each sentence. That is because we did not specify a value for the `max_tokens` keyword argument. The model uses the default value `16`, which is insufficient for the response.

{Try it!}(python3 setting.py 6)

To remedy this problem, set `max_tokens` to `100`. Run the program again. 

```python
response = openai.Completion.create(
  model="text-davinci-002",
  prompt=prompts,
  top_p=1,
  max_tokens=100)
```

{Try it!}(python3 setting.py 7)

You should see a complete response that lists the sentiment for each sentence. Generating a good response is a balancing act between all of the different factors that affect how the model works.

{Check It!|assessment}(multiple-choice-3848935923)
