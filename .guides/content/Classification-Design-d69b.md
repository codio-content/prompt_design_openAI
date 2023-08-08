##

A classifier is any algorithm that sorts data into different classes. GPT-3 is a model which makes use of several different algorithms, including those used for classification, to generate its results. This means that GPT-3 can perform classification out of the box. However, you need to structure your prompts for successful results.

**We use plain language to describe your inputs and outputs**. In the code below, We use plain language for the input "tweet" and the expected output "sentiment." As a best practice, start with plain language descriptions. 

```markdown
Classify the sentiment of these tweets:

1. "I had the worst day"
2. "I had a blast at the movies"
3. "I can't wait for christmas"
4. "My cat is adorable ❤️❤️"
5. "I hate chocolate 😠"
6. "My day was okay"
```

{Try it!}(python3 box.py 8)
{Reset}(python3 reset.py 8)

While you can often use shorthand or keys to indicate the input and output, it's best to start by being as descriptive as possible. Then work backwards to remove extra words and see if performance stays consistent.

|||challenge
## Try this variation:
* Reduce the clarity of the prompt by having only a single word. Compare these results from the prompt above.

```markdown
sentiment

1. "I had the worst day"
2. "I had a blast at the movies"
3. "I can't wait for christmas"
4. "My cat is adorable ❤️❤️"
5. "I hate chocolate 😠"
6. "My day was okay"
```

{Try it!}(python3 box.py 9)
{Reset}(python3 reset.py 9)

|||

**Show the API how to respond to any case**. In this example, we remove the prompt in plain language. Instead we provide examples for how the model should respond to the prompt. The model should be able to infer how to respond to each tweet in the prompt. Click the `TRY IT` button a few times and notice how the model responds to tweet #6.

```markdown
1. "I had the worst day"
2. "I had a blast at the movies"
3. "I can't wait for christmas"
4. "My cat is adorable ❤️❤️"
5. "I hate chocolate 😠"
6. "My day was okay"

tweet 1: -
tweet 2: +
```

{Try it!}(python3 box.py 10)
{Reset}(python3 reset.py 10)

Because we did not specify how to respond to tweets with the neutral sentiment, the model will respond with `0` or `+/-` or sometimes a `+`. If we want to have a specific label for a neutral tweet, then we need to provide an example for how to respond. A neutral label is important because there will be many cases where even a human would have a hard time determining if something is positive or negative.

Add a key with the expected label for each sentiment. Click the `TRY IT` button a few times and compare the output from the example above.

```markdown
1. "I had the worst day"
2. "I had a blast at the movies"
3. "I can't wait for christmas"
4. "My cat is adorable ❤️❤️"
5. "I hate chocolate 😠"
6. "My day was okay"

if positive: +
if negative: -
if neutral: ?

tweet 1: -
tweet 2: +
```

{Try it!}(python3 box.py 11)
{Reset}(python3 reset.py 11)

**Important**, the model already understands the concepts of sentiment and a tweet. You need fewer examples for familiar tasks such as this. If you're building a classifier for something the model might not be familiar with, it might be necessary to provide more examples.

{Check It!|assessment}(multiple-choice-3829999602)
