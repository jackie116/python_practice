import tkinter as tk
from tkinter import StringVar, ttk
from tkinter import Frame
#from tkinter.ttk import Style
from tkinter.filedialog import askdirectory

class PdfView(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        master.title("PDF Merge")
        #鎖定視窗大小
        master.resizable(width=0, height=0)  
        
        #設定style
        #style=ttk.Style()
        #style.configure("Red.TLabel", foreground="red")
        self.path = StringVar()
        self.grid()
        self.createWidgets()
    
    def selectPath(self):
        selected_path = askdirectory()
        self.path.set(selected_path)

    # 建立所有視窗元件
    def createWidgets(self):
        self.pl = ttk.Label(self)
        self.pl['text'] = '資料夾路徑:'
        self.pl.grid(row=0,column=0,padx=5,pady=5)

        self.fl = ttk.Label(self)
        self.fl['text'] = '輸出名稱:'
        self.fl.grid(row=1,column=0,padx=5,pady=5)

        self.pe = ttk.Entry(self)
        self.pe['textvariable'] = self.path
        self.pe.grid(row=0, column=1, columnspan=3, padx=5, pady=5)

        self.fe = ttk.Entry(self)
        self.fe.grid(row=1, column=1, columnspan=3, padx=5, pady=5)

        self.pb =ttk.Button(self)
        self.pb['text'] = '...'
        self.pb['command'] = self.selectPath
        self.pb.grid(row=0, column=4, columnspan=2, padx=5, pady=5)

        self.mb =ttk.Button(self)
        self.mb['text'] = 'Merge'
        self.mb.grid(row=1, column=4, columnspan=2, padx=5, pady=5)

        self.rt = tk.Text(self)
        self.rt['height']= 5
        self.rt['width']= 40
        self.rt.grid(row=2, column=0, rowspan=5, columnspan=6, padx=5, pady=10)


# GUI 執行部分
if __name__ == '__main__':
    root = tk.Tk()
    app = PdfView(master=root)
    root.mainloop()