from tkinter import Tk
from tkinter.constants import END

from pdf_merge import PdfMerge
from pdf_view import PdfView

class PdfController:
    #設定初值
    def __init__(self):
        self.m = PdfMerge()
        self.folder_path=''
        self.pdf_name=''
        
        self.app = PdfView(master=Tk())
        self.app.mb['command'] = self.mbc
        self.app.mainloop()

    def mbc(self):
        self.app.rt.delete("1.0", END)
        
        if len(self.app.pe.get()) == 0 or len(self.app.fe.get()) == 0:
            self.app.rt.insert(END, "路徑名稱和輸出名稱不得為空\n")
        else:
            self.folder_path = self.app.pe.get()
            self.pdf_name = self.app.fe.get() + '.pdf'
            self.app.rt.insert(END, "PDF文件正在合併，請稍等......\n")       
            self.m.MergePDF(self.folder_path, self.pdf_name)
            self.app.rt.insert(END, f"合併後的總頁數:{self.m.outputPages}\nPDF文件合併完成\n")
            self.app.pe.delete(0, END)
            self.app.fe.delete(0, END)
        
if __name__ == '__main__':
    app = PdfController()