import copy

def getPromptContext(file):
    txt = open(file, "r", encoding="utf-8")
    txt_lines = txt.readlines()

    # guardando as palavras chaves para identificar cada campo
    key_words = {
        "adm_perct":(("taxa de administração", "taxa", "administração", "serviços de administração", "%", "remuneração", "percentual", "taxa de administração máxima", "taxa máxima", "máxima", "a.a."), (10, 3, 3, 6, 1, 3, 2, -8, -2, -1, 4)), 
        "adm_fin":(("taxa de administração", "taxa", "administração", "serviços de administração", "r$", "remuneração", "percentual", "taxa de administração máxima", "taxa máxima", "máxima"), (10, 3, 3, 6, 2, 3, 2, -8, -2, -1)), 
        "cota_resgate":(("d+", "dia(s) útil", "resgate", "resgate de cotas", "cotas", "conversão"),(15, 4, 4, 5, 2, 7)), 
        "rec_resgate":(("d+", "dia(s) útil", "resgate", "resgate de cotas", "cotas", "conversão"),(15, 4, 4, 5, 2, 7)), 
        "Exerc_social":(("exercício social", "cada ano", "ano", "demonstrações contábeis", "janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"),(15, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2))
    }

    prompts = []


    # faremos uma busca para cada campo
    for field in key_words.keys():
        ScoreVector = []

        # número de linhas com score alto para realizarmos a busca
        nScoresAnalysed = 3

        def getScore(line):
            score = 0
            for i, key_word in enumerate(key_words[field][0]):
                if key_word.lower() in line.lower():
                    score += key_words[field][1][i]
            return score

        for i, line in enumerate(txt_lines):
            score_index = []
            score = getScore(line)
            score_index.append(score)
            score_index.append(i)
            ScoreVector.append(score_index)

        blockSize = 20
        boundary_size = int(blockSize/2)
        currentBlock = []
        bestBlock = []
        bestScore = 0

        # ordenando a lista pelas linhas mais relevantes do documento
        sortedScoreVector = sorted(ScoreVector, key=lambda x:x[0])

        # lista com as melhoras linhas e seus indices
        bestLines = sortedScoreVector[-nScoresAnalysed:]

        for line in bestLines:
            line_index = line[1] 
            block = ScoreVector[line_index - boundary_size:line_index + boundary_size]
            # print(txt_lines[line_index - boundary_size:line_index + boundary_size])
            # print("--------------------------------------------------")
            sum_score = 0
            for score in block:
                sum_score += score[0]
            # print(sum_score)
            if sum_score > bestScore:
                bestScore = sum_score
                bestBlock = txt_lines[line_index - boundary_size:line_index + boundary_size]

        prompt = ""
        prompt = prompt.join(bestBlock)
        prompts.append(prompt)

    return prompts