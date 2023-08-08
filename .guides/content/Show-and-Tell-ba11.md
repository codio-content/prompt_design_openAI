##

## Constructing a Better Prompt

One of the more impressive aspects of the GPT-3 model is that it can give quality answers to vague prompts. If we want to increase the quality of the responses, we need to improve the prompt. Use **show and tell** as a guideline when developing a prompt.

For show and tell  we want to focus on 3 things:

1. Giving the model clear instructions (tell)
2. Giving the model an example (show)
3. Giving the model clear instructions and an example (show and tell)

Let's start with a simple prompt that does not make use of the show and tell principles. 

```markdown
recommend 10 movies
```

{Try it!}(python3 box.py)

If you want to try other prompts. You can use the `RESET` button below to clear the text in the file on the left. Then use the `TRY IT` button to generate another response. 

{Reset}(python3 reset.py)

Most likely, you see movies that are popular, critically acclaimed, or maybe you have never heard of the film before. Since you are asking for ten titles, the model numbers each film. If you run the prompt a couple of times you may see the numbering like `1.` or even `1)`. Since we are not being specific, the model is not very consistent.

We can produce a better list of films by telling the model what features you are looking for. Instead of numbers, we want a list that uses numbers to identify each item.

```markdown
recommend 10 movies. use letters when listing your movies.
```

{Try it!}(python3 box.py 2)
{Reset}(python3 reset.py 2)

The model now produces a list with letters instead of numbers. But the list can be just as inconsistent in terms of formatting. This is where the show principle comes into play. In addition to the prompt, show the model how you want the list formatted. Each line in the list should contain a letter followed by a closing parenthesis, and the film title should appear between quotes.

```markdown
recommend 10 movies. use letters when listing your movies.
A) "Titanic"
B) "The Godfather"
```

{Try it!}(python3 box.py 3)
{Reset}(python3 reset.py 3)

For more precision, we can combine the show and tell principles. Tell the prompt that you want 10 horror movies in a list that uses letters. Then show the model how you want the list formatted.

```markdown
recommend 10 horror movies. use letters when listing your movies.
A) "The Ring"
B) "The Exorcist"
```

{Try it!}(python3 box.py 4)
{Reset}(python3 reset.py 4)

Using the show and tell principles, you can dramatically change the type and format of the model's response. With the right combination, you can improve the quality of the results, which is more desirable than the standard GPT-3 response.

{Check It!|assessment}(fill-in-the-blanks-2894602378)
