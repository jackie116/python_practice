from tkinter import Tk
from tkinter.constants import END
from game import Game
from game_view import GameView
from datetime import datetime

class GameController:
    def __init__(self):
        self.g=None
        self.userinput=""
        self.doTick =True

        self.app = GameView(master=Tk())
        self.app.nb['command'] = self.nbc
        self.app.gb['command'] = self.gbc
        self.app.mainloop()
    #計時器
    def update_clock(self):
        if not self.doTick:
            return
        self.end=datetime.now()
        self.delta=self.end-self.begin
        self.app.sl['text']=f'經過{self.delta.seconds}秒'
        self.app.after(1000,self.update_clock)
    #初始化遊戲
    def nbc(self):
        self.g=Game()
        self.app.rt.delete("1.0",END)
        self.app.rt.insert(END,"遊戲開始\n----------\n")
        self.app.ge.delete(0, END)
        self.app.rl['text'] = '遊戲開始'
        self.app.tlp['text'] = '猜測0次'
        self.doTick=True
        self.begin=datetime.now()
        self.update_clock()
    #猜測數字
    def gbc(self):
        if self.g == None:
            self.app.rl['text']='沒有遊戲'
        else:
            self.userinput=self.app.ge.get()
            

        self.app.ge.delete(0,END)

if __name__ == '__main__':
    app = GameController()