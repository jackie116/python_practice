from random import shuffle

class GuessGame:
    #設定初值
    def __init__(self):
        self.answer= self.random_answer()
        self.times=1
    #判斷是否有重複值
    def find_number(self, guess):
        if(len(list(guess))==len(set(guess))): 
            return True
        else: 
            return False         
    #判斷_A_B
    def ab_counter(self, answer, guess):
        self.ab_array=[0,0]
        for i in range(4):
            for j in range(4):
                if i==j and answer[i]==guess[j]:
                    self.ab_array[0]+=1
                elif answer[i]==guess[j]:
                    self.ab_array[1]+=1    
        print(f'{self.ab_array[0]}A{self.ab_array[1]}B')
    #猜測比對
    def test(self, answer, guess):
        if guess != answer:
            self.ab_counter(answer, guess)
            return False
        else:
            return True
    #隨機生成四位數
    def random_answer(self):
        answer =''
        items=[x for x in range(10)]
        shuffle(items)
        for i in range(4): answer+=str(items[i])
        print(answer) 
        return answer
    #guessgame.py 測試
    '''
    def run(self):
        while True:
            self.guess = input('猜數字:')
            if len(self.guess)==4 and self.find_number(self.guess) == True: 
                if self.test(self.answer, self.guess) == False:
                    self.times += 1  
                else:
                    print('猜對了!')
                    print(f'猜了{self.times}次')
                    break      
            else: 
                print('輸入不符合規則(超過4個數字或有重複數字)!')            
    '''
if __name__ == '__main__':
    G=GuessGame()
    G.run()