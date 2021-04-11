#PyPDF整合
from  PyPDF2 import PdfFileReader, PdfFileMerger
merger = PdfFileMerger()
input1 = open("统计5.pdf","rb") #第一份文件
input2 = open("政府工作报告词云实例解析(下).pdf","rb") #第二份文件
merger.append(fileobj = input1, pages = (0,3)) #第一份文件页数
merger.merge(position = 2, fileobj = input2, pages= (0,1)) #第二份文件页数
output = open("document_output.pdf","wb") #新文件名称
merger.write(output)