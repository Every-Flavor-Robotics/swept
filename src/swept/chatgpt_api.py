## A class to handle the API calls to the ChatGPT API

import requests

class ChatGPT:
    """
    A class to handle the API calls to the ChatGPT chat API.
    """

    def __init__(self, api_key, model="gpt-3.5-turbo"):
        """
        Initialize the ChatGPT class
        :param api_key: The API key for the ChatGPT API
        :param model: The model to use for the API call. Defaults to "gpt-3.5-turbo"
        """

        self.api_key = api_key
        self.api_url = 'https://api.openai.com/v1/chat/completions'
        self.model_str = model

    def request(self, messages):
        """
        Make a request to the ChatGPT API
        :param messages: A list of messages to send to the API
        :return: The response from the API
        """

        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        payload = {
            "model" : self.model_str,
            'messages': messages
        }

        # Timeout after 30 seconds if response not received
        response = requests.post(self.api_url, headers=headers, json=payload, timeout=30)
        response.raise_for_status()

        return response.json()

# # Example usage
# api_key = 'your_api_key'
# chatgpt = ChatGPT(api_key)
# messages = [
#     {'role': 'system', 'content': 'You are a helpful assistant.'},
#     {'role': 'user', 'content': 'Who won the world series in 2020?'}
# ]
# response = chatgpt.chat(messages)
# print(response['choices'][0]['message']['content'])