#合併PDF
import os
from PyPDF2 import PdfFileReader, PdfFileWriter

class PdfMerge:
    #os.walk(dirPath)回傳三個元素tuple(dirPath路徑,dirNames所有資料夾名,fileNames所有檔案名)
    #os.path.join(dirPath,fileName) 把路徑跟檔名合併
    def GetFileName(self, dir_path):
        #list comprehension
        file_list = [os.path.join(dirpath, filesname) \
                    for dirpath, dirs, files in os.walk(dir_path) \
                    for filesname in files]
        return file_list

    def MergePDF(self, dir_path, file_name):
        output = PdfFileWriter()
        self.outputPages = 0
        file_list = self.GetFileName(dir_path)
        for pdf_file in file_list:
            #f-string內不能有反斜線，所以這裡用傳統格式化方式
            print("文件：%s" % pdf_file.split('\\')[-1], end=' ')
            # 讀取PDF文件
            input = PdfFileReader(open(pdf_file, "rb"))
            # 獲得源PDF文件中頁面總數
            pageCount = input.getNumPages()
            self.outputPages += pageCount
            print(f"頁數：{pageCount}")
            # 分别將page添加到输出output中
            for iPage in range(pageCount):
                output.addPage(input.getPage(iPage))
        print(f"\n合併後的總頁數:{self.outputPages}")
        # 寫入到目標PDF文件
        print("PDF文件正在合併，請稍等......")
        with open(os.path.join(dir_path, file_name), "wb") as outputfile:
            # 注意這裡的寫法和正常的上下文文件寫入是相反的
            output.write(outputfile)
        print("PDF文件合併完成")

if __name__ == '__main__':
    # 設置存放多個pdf文件的文件夾
    dir_path = r'C:\Users\jackiehuang\Desktop\python\docx\pdf_merge'
    # 目標文件的名字
    file_name = "test_5.pdf"
    M=PdfMerge()
    M.MergePDF(dir_path, file_name)