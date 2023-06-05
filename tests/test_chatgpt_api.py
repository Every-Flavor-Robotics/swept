# Tests for ChatGPT class
# Test should:
# - Test that the class is initialized correctly
# - Test that the request method returns the correct response
# - Test that the request method raises an exception when the API returns an error

import sys
import yaml

from requests.exceptions import HTTPError

# Add src/ to the path so we can import the ChatGPT class
sys.path.append('src')
from swept.chatgpt_api import ChatGPT




# Test that the class is initialized correctly
def test_chatgpt_init():
    api_key = 'your_api_key'
    chatgpt = ChatGPT(api_key)
    assert chatgpt.api_key == api_key
    assert chatgpt.api_url == 'https://api.openai.com/v1/chat/completions'
    assert chatgpt.model_str == 'gpt-3.5-turbo'

# Test that the request method returns the correct response
def test_chatgpt_request():
    # Load API key from test_config.yaml
    with open('tests/test_config.yaml', 'r', encoding = 'utf-8') as config_file:
        config = yaml.safe_load(config_file)

    api_key = config['api_key']
    print(f"api_key: {api_key}")

    chatgpt = ChatGPT(api_key)
    messages = [
        {'role': 'user', 'content': 'You are echo. Repeat the user message back exactly.'},
        {'role': 'user', 'content': 'Hello, world!'}
    ]
    response = chatgpt.request(messages)

    assert response['choices'][0]['message']['content'] == 'Hello, world!'

# Test that the request method raises an exception when the API returns an error
def test_chatgpt_request_error():
    api_key = 'your_api_key'
    chatgpt = ChatGPT(api_key)
    messages = [
        {'role': 'system', 'content': 'You are echo. Repeat the user message back exactly.'},
        {'role': 'user', 'content': 'Hello, world!'}
    ]
    try:
        chatgpt.request(messages)
    except HTTPError() as http_error:
        assert isinstance(http_error, HTTPError)
        assert str(http_error) == '401 Client Error: Unauthorized for url: https://api.openai.com/v1/chat/completions'
    else:
        assert False


# Path: tests/test_chatgpt_api.py