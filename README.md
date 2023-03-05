# davinci-functions
Library to ask OpenAI GPT for generating Python literals.

This library is prepared to record prompts that would be useful for Python programs.
If you developed something, let's make a pull request!


## Getting started

Set your OpenAI Organization ID and API key before using this library.
Then invoke the functions in the library.

```python
import openai
import davinci_functions

openai.organization = "YOUR_ORG_ID"
openai.api_key = "YOUR_API_KEY"

prompt = """\
Output the list of 10 random city names in the United States.
"""

for val in davinci_functions.list(prompt):
    print(val)
```

This script will print something like:

```
New York
Los Angeles
Chicago
Houston
Phoenix
Philadelphia
San Antonio
San Diego
Dallas
San Jose
```


## Functions

### `davinci_functions.list`

Returns the list of something.

```python
>>> davinci_functions.list("say hello.")
['Hello']
>>> davinci_functions.list("say hello world.")
['Hello', 'world']
>>> davinci_functions.list("Output first 5 prime numbers.")
[2, 3, 5, 7, 11]
>>> davinci_functions.list("5 random countries")
['Japan', 'Australia', 'Brazil', 'India', 'China']
```

Solving some tasks (e.g., named entity recognition):

```python
>>> prompt="""
... Extract all named entities in the following paragraph:
... 
... Google is founded by Larry Page and Sergey Brin in 1998.
... The headquarter is located in Mountain View, Carifornia, United States.
... """
>>> davinci_functions.list(prompt)
['Google', 'Larry Page', 'Sergey Brin', 'Mountain View', 'Carifornia', 'United States']
```

Other language (Japanese):

```python
>>> davinci_functions.list("日本語の単語を5個")
['日本語', '単語', '文字', '言葉', '意味']
>>> davinci_functions.list("1から10までの数字のリスト。ただし3で割り切れるときはFizzにしてください。")
[1, 2, 'Fizz', 4, 5, 'Fizz', 7, 8, 'Fizz', 10]
>>> davinci_functions.list("「明日は明日の風が吹く」の形態素の一覧")
['明日', 'は', '明日', 'の', '風', 'が', '吹く']
```

### `davinci_functions.judge`

Returns the truth of something.

```python
>>> davinci_functions.judge("The sum of 2 and 3 is 5.")
True
>>> davinci_functions.judge("The sum of 2 and 3 is 6.")
False
>>> davinci_functions.judge("San Francisco is the capital of the United States.")
False
>>> davinci_functions.judge("New York is the capital of the United States.")
True  # Wrong answer! This kind of mistakes happens very often: please take care.
>>> davinci_functions.judge("Washington D.C. is the capital of the United States. How about New York?")
False
```

### `davinci_functions.function`

Synthesizes a Python function described in the prompt.

```python
>>> f = davinci_functions.function("Multiply the argument x by 2.")
>>> f(3)
6
>>> f = davinci_functions.function("Arithmetic mean of all elements in the list x.")
>>> f([1, 2, 3])
2.0
```


## Caveats

Right now, this library doesn't consider prompt injection and validity of the returned
expression by GPT. Please don't use this library in the real products that needs to
take care about consistency and security.
