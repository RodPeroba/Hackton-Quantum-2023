from Downloader import Downloader

#files_downloader = Downloader()
#files_downloader.run(pdfs_to_read="pdfs_to_read.txt")
class Scorer():

    def __init__(self):
    # guardando as palavras chaves para identificar cada campo
        self.key_words = {
            "adm_perct":(("taxa de administração", "taxa", "administração", "serviços de administração", "%", "remuneração", "percentual", "taxa de administração máxima", "taxa máxima", "máxima"), (10, 3, 3, 6, 1, 3, 2, -5, -2, -1)), 
            "adm_fin":(), 
            "cota_resgate":(), 
            "rec_resgate":(), 
            "Exerc_social":()
        }

        self.ScoreVector = []
        self.blockSize = 15
        self.currentBlock = []
        self.bestBlock = []

    def getScore(self, line):
        score = 0
        for i, key_word in enumerate(self.key_words["adm_perct"][0]):
            if key_word in line.lower():
                score += self.key_words["adm_perct"][1][i]
        return score

    def make_score(self, fileName):
        txt = open(fileName,"r",encoding="UTF-8")

        for line in txt.readlines():
            score = self.getScore(line)
            self.ScoreVector.append(score)

        # for i, score in enumerate(ScoreVector):
        #     print(f"linha: {i}, score: {score}")

    def print_score(self, fileName):
        txt = open(fileName,"r",encoding="UTF-8")

        for i, line in enumerate(txt.readlines()):
            print(f"id: {i}, score {self.ScoreVector[i]}, linha: {line}")