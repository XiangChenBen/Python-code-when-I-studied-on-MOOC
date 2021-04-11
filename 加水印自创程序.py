import PyPDF2

def add_watermark(water_file,page_pdf):         #添加水印函数
    """
    将水印pdf与pdf的一页进行合并
    :param water_file:
    :param page_pdf:
    :return:
    """
    pdfReader = PyPDF2.PdfFileReader(water_file) 
    pdfReader.getPage(0).mergePage(page_pdf)     #将水印添加到提取页，水印置于下层背景，同word水印效果
    return pdfReader.getPage(0)

# 遍历pdf的每一页,添加水印

DocumentName = ['Quantitative methods.pdf','Quan 题库.pdf','Quan 题库答案.pdf']
WatermarkName=["watermark张艳.pdf", "watermarkJane.pdf",'watermark窦乔伊.pdf','watermark何皓.pdf']

for SelectDN in range(len(DocumentName)):                      # 遍历所有文件
    pdfReader = PyPDF2.PdfFileReader(DocumentName[SelectDN])   # 读取pdf内容
    for SelectWm in range(len(WatermarkName)):                 # 遍历所有watermark
        pdfWriter = PyPDF2.PdfFileWriter()                     # 用于写pdf
        for page in range(pdfReader.numPages):                 # 遍历pdf的每一页,添加水印
            page_pdf = add_watermark(WatermarkName[SelectWm], pdfReader.getPage(page))
            pdfWriter.addPage(page_pdf)

        with open(WatermarkName[SelectWm][9:-4]+'_'+DocumentName[SelectDN], 'wb') as target_file:  #保存最终pdf
            pdfWriter.write(target_file)