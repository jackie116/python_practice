from tkinter import Tk
from tkinter.constants import END, NONE
from guessgame import GuessGame
from game_view import GameView
from datetime import datetime

class GameController:
    #設定初值
    def __init__(self):
        self.g = None
        self.userinput = ""
        self.doTick = True

        self.app = GameView(master=Tk())
        self.app.nb['command'] = self.nbc
        self.app.gb['command'] = self.gbc
        self.app.mainloop()
    #計時器
    def update_clock(self):
        if not self.doTick:
            return
        self.end = datetime.now()
        self.delta = self.end-self.begin
        self.app.sl['text'] = f'經過{self.delta.seconds}秒'
        self.app.after(1000,self.update_clock)
    #初始化遊戲
    def nbc(self):
        self.g = GuessGame()
        self.app.rt.delete("1.0", END)
        self.app.rt.insert(END, "遊戲開始\n----------\n")
        self.app.ge.delete(0, END)
        self.app.rl['text'] = '遊戲開始'
        self.app.tl['text'] = '猜測0次' 
        self.doTick = True      
        self.begin=datetime.now()
        self.update_clock()
    #猜測數字 
    def gbc(self):
        if self.g == None:
            self.app.rl['text'] = '沒有遊戲'
        else:
            self.userinput = self.app.ge.get()
            if len(self.userinput)==4 and self.g.find_number(self.userinput) == True: 
                if self.g.test(self.g.answer, self.userinput) == False:
                    self.app.rt.insert(END, f"{self.g.times}-{self.userinput}-{self.g.ab_array[0]}A{self.g.ab_array[1]}B\n")
                    self.app.rl['text'] = f"{self.userinput}-{self.g.ab_array[0]}A{self.g.ab_array[1]}B"
                    self.app.tl['text'] = f"猜測{self.g.times}次"
                    self.g.times += 1
                else:
                    self.app.rt.insert(END, f"猜對了，猜了{self.g.times}次，{self.delta.seconds}秒\n")
                    self.app.rl['text']= "猜對了"
                    self.app.tl['text'] = f'猜測{self.g.times}次'
                    self.app.sl['text'] = None
                    self.doTick=False
                    self.g = None
            else: 
                self.app.rl['text']= "輸入不符合規則!\n(非4個數字或有重複數字)"
        self.app.ge.delete(0, END)   
            
if __name__ == '__main__':
    app = GameController()