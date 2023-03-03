# davinci-functions
Library to ask OpenAPI GPT3 for generating Python literals


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
FizzBuzz
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

More examples:

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

Other language (Japanese):

```python
>>> davinci_functions.list("日本語の単語を5個")
['日本語', '単語', '文字', '言葉', '意味']
>>> davinci_functions.list("1から10までの数字のリスト。ただし3で割り切れるときはFizzにしてください。")
[1, 2, 'Fizz', 4, 5, 'Fizz', 7, 8, 'Fizz', 10]
```
