#####################################
#help
from os import linesep
from typing import Text
from reportlab.lib import colors


# def drawMyRuler(pdf):
#     pdf.drawString(100,810, 'x100')
#     pdf.drawString(200,810, 'x200')
#     pdf.drawString(300,810, 'x300')
#     pdf.drawString(400,810, 'x400')
#     pdf.drawString(500,810, 'x500')

#     pdf.drawString(10,100, 'y100')
#     pdf.drawString(10,200, 'y200')
#     pdf.drawString(10,300, 'y300')
#     pdf.drawString(10,400, 'y400')
#     pdf.drawString(10,500, 'y500')
#     pdf.drawString(10,600, 'y600')
#     pdf.drawString(10,700, 'y700')
#     pdf.drawString(10,800, 'y800')




 
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

# Sub title tiêu đề
subTitle2 = 'Món ăn'
subTitle3 = 'SL'
subTitle4 = 'Thành tiền'

# Sub title món ăn
subTitle5 = 'Cá kho'
subTitle6 = 'Thịt kho'
subTitle7 = 'Canh chua'

# Sub title Số lượng
subTitle8 = '2'
subTitle9 = '4'
subTitle10 = '5'

# Sub title Thành tiền
subTitle11 = '50.000 VNĐ'
subTitle12 = '50.000 VNĐ'
subTitle13 = '50.000 VNĐ'

#Sub title phương thức thanh toán
subTitle14 = 'Phương thức thanh toán:'

#Sub title kết quả
subTitle15 = 'MoMo'

#Sub title sum
subTitle16 = 'Tổng thanh toán:'

#Sub title kết quả sum
subTitle17 = '150.000 VNĐ'

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



# drawMyRuler(pdf)

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
pdf.setFont('subTitle2',25)
# pdf.setFont('subTitle2',25)
pdf.drawString(50, 580, subTitle2)

# subTitle 3 
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

pdfmetrics.registerFont(
    TTFont('subTitle3','tahoma.ttf')
)
pdf.setFont('subTitle3',25)
pdf.drawString(280, 580, subTitle3)

# subTitle 4 
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

pdfmetrics.registerFont(
    TTFont('subTitle4','tahoma.ttf')
)
pdf.setFont('subTitle4',25)
pdf.drawString(450, 580, subTitle4)

#gạch ngang (bắt đầu, khoảng cách x từ trên xuống, điểm kết thúc, khoảng cách x từ trên xuống)
pdf.line(0,570,600,570)

# 4. Sub title Món ăn
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

pdfmetrics.registerFont(
    TTFont('subTitle5','tahoma.ttf')
)
pdf.setFont('subTitle5',14)
pdf.drawString(50, 530, subTitle5)
pdf.drawString(50, 470, subTitle6)
pdf.drawString(50, 410, subTitle7)

# 5. Sub title Số lượng
pdf.drawString(285, 530, subTitle8)
pdf.drawString(285, 470, subTitle9)
pdf.drawString(285, 410, subTitle10)

# 5. Sub title Thành tiền
pdf.drawString(480, 530, subTitle11)
pdf.drawString(480, 470, subTitle12)
pdf.drawString(480, 410, subTitle13)

pdf.line(0,380,600,380)

# 4. Sub title phương thức thanh toán
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

pdfmetrics.registerFont(
    TTFont('subTitle14','tahoma.ttf')
)
pdf.setFont('subTitle14',20)
pdf.drawString(10, 330, subTitle14)
pdf.drawString(285, 330, subTitle15)

# 4. Sub title Tổng tiền
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

pdfmetrics.registerFont(
    TTFont('subTitle16','tahoma.ttf')
)
pdf.setFont('subTitle16',25)
pdf.drawString(10, 290, subTitle16)
pdf.drawString(285, 290, subTitle17)

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