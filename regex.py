import re

def regex_porcentagem(text):

    resultado = re.search("(\d+\,\d+)%", text)

    if resultado:
        numero = float(resultado.group(1).replace(",", "."))
        return numero
    else:
        print("Não foi possível encontrar o número e a porcentagem no texto.")

def regex_valor_real(text):
    
    resultado = re.search("R\$\s*(\d+(?:\.\d{3})*(?:,\d{2})?)", text)

    if resultado:
        resultado = resultado.group(1).replace(".", "")
        numero = float(resultado.replace(",", "."))
        return numero
    else:
        print("Não foi possível encontrar o número e a porcentagem no texto.")

def regex_valor_resgate(text):
    
    #resultado = re.search("\D\+\d+d", text)
    resultado = re.search("(\d+)", text)

    if resultado:
        numero = "D+" + resultado.group(1) 
        return numero
    else:
        print("Não foi possível encontrar o número e a porcentagem no texto.")

def regex_mes(text):
    text = text.lower()
    meses = ["janeiro","fevereiro","marco","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]
    for mes in meses:
        if mes in text:
            return mes
    print("Não foi possível o mes do ano.")