#####################################
#help
from os import linesep
from typing import Text
from reportlab.lib import colors


def drawMyRuler(pdf):
    pdf.drawString(100,810, 'x100')
    pdf.drawString(200,810, 'x200')
    pdf.drawString(300,810, 'x300')
    pdf.drawString(400,810, 'x400')
    pdf.drawString(500,810, 'x500')

    pdf.drawString(10,100, 'y100')
    pdf.drawString(10,200, 'y200')
    pdf.drawString(10,300, 'y300')
    pdf.drawString(10,400, 'y400')
    pdf.drawString(10,500, 'y500')
    pdf.drawString(10,600, 'y600')
    pdf.drawString(10,700, 'y700')
    pdf.drawString(10,800, 'y800')




 
# ############################################
#Content
filename = 'Bill.pdf'
documentTitle = 'Document title!'


title = 'Công ty TNHH một thành viên Hutech'
title1 = 'Địa chỉ: 24/22 HBC/Thủ Đức/tp.HCM'
title2 = 'Máy pos: 01'
title3 = 'Ngày bán: 25/05/2021'
title4 = 'Giờ bán: 16:42:50'
subTitle1 = 'HÓA ĐƠN BÁN HÀNG'
subTitle2 = 'Món ăn'
subTitle3 = 'SL'
subTitle4 = 'Thành tiền'

# textLines = [
# 'Công ty TNHH một thành viên Hutech',
# 'Địa chỉ: 24/22 HBC/Thủ Đức/tp.HCM',
# 'Máy pos: 01'
# ]

# image = 'tasmanianDevil.jpg'


# ######################################################
# 0)create document
from reportlab.pdfgen import canvas

pdf = canvas.Canvas(filename)
pdf.setTitle(documentTitle)



drawMyRuler(pdf)

# ############################################
# 1) TItle :: Set fonts
# Print available fonts
# for font in pdf.getAvailableFonts():
#     print(font)

# Register a new font
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

pdfmetrics.registerFont(
    TTFont('abc','tahoma.ttf')
)
pdf.setFont('abc',14)
# pdf.drawString(Khoảng cách từ phải qua, khoảng cách từ trên xuống, title)
pdf.drawString(10, 770, title)
pdf.drawString(10, 750, title1)
pdf.drawString(10, 730, title2)

pdf.line(0,720,700,720)

pdf.drawString(10, 700, title3)
pdf.drawString(10, 680, title4)










# ################################################
# 2) Sub Title 1 :: tiêu đề
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

pdfmetrics.registerFont(
    TTFont(subTitle1,'TAHOMAB0.TTF')
)
pdf.setFont(subTitle1,30)
# pdf.setFillColorRGB(0, 0, 255)
# pdf.setFont("Courier-Bold", 24)
pdf.drawCentredString(290, 630, subTitle1)

#  3)Sub Title 2 :: tiêu đề bảng
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

pdfmetrics.registerFont(
    TTFont('subTitle2','tahoma.ttf')
)
pdf.setFont('subTitle2',20)
pdf.drawString(50, 580, subTitle2)
pdf.drawString(280, 580, subTitle3)
pdf.drawString(450, 580, subTitle4)

pdf.line(0,570,570,570)






# ####################################################
# # 3) Draw a line
# pdf.line(30,710, 550, 710)








# ####################################################
# 4) Text object :: for large amounts of text
# from reportlab.lib import colors

# text = pdf.beginText(40, 680)
# text.setFont("Courier", 18)
# text.setFillColor(colors.red)
# for line in textLines:
#     text.textLine(line)

# pdf.drawText(text)





# #################################################
# 5) Draw a image
# pdf.drawInlineImage(image,130,400)




pdf.save()