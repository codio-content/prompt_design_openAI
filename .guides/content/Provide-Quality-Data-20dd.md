##

## Intentionality

You may be familiar with the expression, "Garbage in, garbage out." Believe it or not, this holds true for models like GPT-3. The model is sophisticated enough to produce coherent output even with terrible prompts, so GPT-3 rarely provides "garbage out". However, the idea is to produce the best results possible, so we need to give the model the best data we can. We are going to ask the model to perform sentiment analysis, which determines how positive or negative a sentence is.

```markdown
what is the overall sentiment of the following sentences:
["i am happy","i am happy to be sad","I am sad"]
```

{Try it!}(python3 box.py 5)
{Reset}(python3 reset.py 5)

The model will say something along the lines of that the overall sentiment is "happy". Is that true? The third sentence clearly does not portray a happy sentiment. What happened? We gave GPT-3 three distinct sentences, but we did not specify how the sentiment analysis should be performed. Do we want an average score for all three sentences, or do we want scores for each individual sentence? We never told the model what to do, so it calculated the average sentiment.

If we want sentiment analysis for each sentence in the list, then we need to explicitly tell that to the model. Let's modify the original prompt above by adding the words "for each" to it.

```markdown
what is the overall sentiment for each of the following sentences:
["i am happy","i am happy to be sad","I am sad"]
```

{Try it!}(python3 box.py 6)
{Reset}(python3 reset.py 6)

We can see by giving it better directions, it was more clear on the assignment it was given. Feel free to reset and try different ways you can get the AI to generate and present new information.

|||challenge
## Try this variation:
Modify the prompt above so that it performs sentiment analysis on each sentence. The results should display each sentence followed by its sentiment analysis.

{Try it!}(python3 box.py 7)
{Reset}(python3 reset.py 7)

<details>
<summary><strong>Solution</strong></summary>
Here is one possible solution:

```markdown
what is the overall sentiment for each of the following sentences:
["i am happy","i am happy to be sad","I am sad"]

sentence: i am happy
sentiment:
```

</details>

|||

Finally, be sure to proofread your examples. The model is usually smart enough to see through basic spelling mistakes and give you a response. However, it also might assume this is intentional (think of companies like eBay, Tumblr, and Reddit), which can affect the response. Be intentional about the instructions you give to the model.

{Check It!|assessment}(multiple-choice-3316116500)
