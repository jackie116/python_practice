import tkinter as tk
from tkinter import ttk
from tkinter import Frame
from tkinter.ttk import Style


class GameView(Frame):
    '''
    nb:new game button
    gb:guess button
    ge:guess entry
    tl:times label
    sl:seconds label
    rt:round text
    '''
    def __init__(self, master=None):
        Frame.__init__(self, master)
        master.title("猜數字")
        #鎖定視窗大小
        master.resizable(width=0,height=0)
        #設定style
        style=Style()
        style.configure("Red.TLabel", foreground="red")
        self.grid()
        self.createWidgets()
    # 建立所有視窗元件
    def createWidgets(self):
       
        self.nb = ttk.Button(self)
        self.nb['text'] = 'New'
        self.nb.grid(row=10, column=0,columnspan=4,pady=20)
        
        self.ge = ttk.Entry(self)
        self.ge.grid(row=1, column=2, columnspan=2, padx=5)

        self.gb = ttk.Button(self)
        self.gb['text'] = 'Guess'
        self.gb.grid(row=2, column=2, columnspan=2)
        
        self.rl = ttk.Label(self)
        self.rl['text'] = 'result'
        self.rl.configure(style="Red.TLabel")
        self.rl.grid(row=4, column=2, columnspan=2)

        self.tl = ttk.Label(self)
        self.tl['text'] = '猜測次數'
        self.tl.grid(row=7, column=2, columnspan=2)
        
        self.sl = ttk.Label(self)
        self.sl['text'] = '猜測秒數'
        self.sl.grid(row=8, column=2, columnspan=2)
        
        self.rt = tk.Text(self)
        self.rt['width'] = 40
        self.rt.grid(row=0, column=0, rowspan=9, columnspan=2, padx=5, pady=5,ipadx=10,ipady=10)

# GUI 執行部分
if __name__ == '__main__':
    root = tk.Tk()
    app = GameView(master=root)
    root.mainloop()
        