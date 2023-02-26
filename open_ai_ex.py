import os
import openai
import configsx

openai.api_key = configsx.API_open_AI_chat

def get_answer(instructiune, text_user):

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt= f"{instructiune}:\n\n{text_user}",
    temperature=0.9,
    max_tokens=300,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
    )

    return response['choices'][0]['text']

if __name__ == '__main__':
    print(get_answer('scrie o poezie in limba romana despre', 'python'))
