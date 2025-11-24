import openai

class ChatGPT():
    def __init__(self, key):
        openai.api_key = key

    def get_promt(self, best_block, pergunta):

        pergunta_completa = pergunta + best_block
        completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", # this is "ChatGPT" $0.002 per 1k tokens
        messages=[{"role": "user", "content": pergunta_completa}]
        )
        #print(pergunta_completa)
        return completion.choices[0].message.content