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
