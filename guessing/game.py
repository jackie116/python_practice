from random import randint, random

class Game:
    #設定初值
    def __init__(self):
        self.answer= self.random_answer()
        self.times=1
    #判斷大小

    #猜測比對
    def test(self, answer, guess):
        if guess != answer:
            return False
        else:
            return True
    #隨機生成答案
    def random_answer(self):
        return randint()

if __name__ == '__main__':
    G=Game()