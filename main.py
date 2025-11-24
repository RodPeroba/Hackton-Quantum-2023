from os import listdir
import getPromptContext
from openAiApi import ChatGPT
import regex
import pandas as pd
import csv
from Downloader import Downloader

def add_to_csv(CNPJ, campo, resultado):
    ###Checar se existe
    row = {'CNPJ':CNPJ, 'Campo':campo, 'Valor':resultado}
    with open('resultados.csv', 'a', newline='') as f:
    # Create a dictionary writer with the dict keys as column fieldnames
        writer = csv.DictWriter(f, fieldnames=row.keys())
    # Append single row to CSV
        writer.writerow(row)
'''
downloader = Downloader()
downloader.run(pdfs_to_read="pdfs_to_read.txt")
'''
#create csv 

add_to_csv("CNPJ","Campo","Valor")
chatGPT = ChatGPT(key = "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")
files_to_score = []
files_not_to_score = ["pdfs_to_read.txt","ReadMe.txt","requirements.txt"]
for my_file in listdir():
    #consertar se der tempo
    if ".txt" in my_file and my_file != files_not_to_score[0]and my_file != files_not_to_score[1]and my_file != files_not_to_score[2]:
        files_to_score.append(my_file)

prompt_questions = ["Qual o valor da taxa de administração do fundo em porcentagem? Diga só a porcentagem e nada mais     \n\n",
                    "Qual o valor em real da administração financeira do fundo? Diga só o numero em reais e nada mais. \n\n ",
                    "Qual a Conversão da cota para resgate em dias úteis? Responda em menos de 5 caracteres     \n\n",
                    "Qual a disponibiliza para resgate em dias úteis + os dias de conversão? Responda em menos de 5 caracteres      \n\n",
                    "Qual o mês do fim do exercicio social? Responda em menos de 10 caracteres.   \n\n"]

campos = [      "Taxa de administrao percentual",
                "Taxa de administracao financeira",
                "Conversao de cota para resgate",
                "Disponibilizacao dos recursos para resgate",
                "Fim do exercicio social"]

regex_functions = [regex.regex_porcentagem,
                   regex.regex_valor_real,
                   regex.regex_valor_resgate,
                   regex.regex_valor_resgate,
                   regex.regex_mes
                   ]

for my_file in files_to_score:
    prompt_block = getPromptContext.getPromptContext(my_file)
    ###novo for qnd tiver implementada as listas
    for i, prompt in enumerate(prompt_block):
        resposta = chatGPT.get_promt(prompt, pergunta = prompt_questions[i])
        taxa_de_adm = regex_functions[i](resposta)
        add_to_csv(my_file[1:-4],campos[i],taxa_de_adm) # fatiação retira o .txt do nome
