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


# Thấy cái hoá đơn nó trả về gì không. Nó trả về mảng ( array )
# thì cái ở bên trong nó sẽ nhưu vậy, vậy thiếu hả thiết kế thiếu đúng ko
# này là dư thiếu gì
# cái này mới đúng là cái nó trả về
textLines=[
  {
    "name":"Cơm",
    "quantity":2,
    "price":1000
  },
  {
    "name":"Cơm",
    "quantity":2,
    "price":1000
  },
  {
    "name":"Cơm",
    "quantity":2,
    "price":1000
  },
  {
    "name":"Cơm",
    "quantity":2,
    "price":1000
  },

]



#Sub title phương thức thanh toán
subTitle14 = 'Phương thức thanh toán:'

#Sub title kết quả
subTitle15 = 'MoMo'

#Sub title sum
subTitle16 = 'Tổng thanh toán:'

#Sub title kết quả sum
subTitle17 = '300.000 VNĐ'

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
    TTFont('abc','Roboto-Regular.ttf')
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
    TTFont(subTitle1,'Roboto-Bold.ttf')
)
pdf.setFont(subTitle1,30)
# pdf.setFillColorRGB(0, 0, 255)
# pdf.setFont("Courier-Bold", 24)
pdf.drawCentredString(290, 630, subTitle1)

#  3)Sub Title 2 :: tiêu đề bảng
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

pdfmetrics.registerFont(
    TTFont('subTitle2','Roboto-Regular.ttf')
)
pdf.setFont('subTitle2',25)
# pdf.setFont('subTitle2',25)
pdf.drawString(50, 580, subTitle2)

# subTitle 3 
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

pdfmetrics.registerFont(
    TTFont('subTitle3','Roboto-Regular.ttf')
)
pdf.setFont('subTitle3',25)
pdf.drawString(280, 580, subTitle3)

# subTitle 4 
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

pdfmetrics.registerFont(
    TTFont('subTitle4','Roboto-Regular.ttf')
)
pdf.setFont('subTitle4',25)
pdf.drawString(450, 580, subTitle4)

#gạch ngang (bắt đầu, khoảng cách x từ trên xuống, điểm kết thúc, khoảng cách x từ trên xuống)
pdf.line(0,570,600,570)
y=530
for item in textLines:
    # xem thử mới vào y bằng bao nheeiu
    # giờ lấy thg name trước nha
    # Lấy đưuuddwuojci thì đi  vẽ
    # lấy toạ độ bắt đầu cái danh sách là 530 nha
    # nó bị chồng nhau do ở cùng 1 toạ độ
    # ==> mỗi thg nên xuống tâm 50 độ nữa
    # Thấy chưa giờ tới 2 cái thông số kia, bằng trục dọc
    # tương đương bị chồng, này là đổi trục ngang vì nó phải nằm chung 1 dòng nên ko đổi y
    pdf.drawString(50,y,item["name"])
    # nó chỉ nhận str thôi (string)
    # vậy cho nó bằng vs maasycasi tiêu đê
    # đó thấy chưa. Giờ đến cái đường kẻ ngang
    pdf.drawString(280,y,str(item["quantity"]))
    pdf.drawString(450,y,str(item["price"]))
    y=y-50 # tương đương y-=20
    # kết thúc 1 vòng lặp thì y còn bao nhiêu
    # cái ra cuối cùng bị thừa tại đâu có item nào ở dưới nó nữa đâu nên mình phải cộng lại 50 khi kết thúc vòng fỏ
# do cái đường kẻ ngang ở dưới ko được set cứng vì nhiều hàng thì nó phải xuống. Nên mình phải tính toạ độ của cái trên trừ ra
y=y+20
# lấy y làm toạ độ để cân cái đường kẻ
# nó xát vách luôn giờ là lúc mình trừ ra khoảng mình muốn, vd là 30 đi
pdf.line(0,y,600,y)
# đó giờ mình thêm bao nhiêu cũng dc mà đâu tuỳ kích thước trang, kích thước lớn quá thì nó bị overflow hidden tràn dòng
# nó lủng 1 lỗ to đùng thấy ko. Do thg cuối bị trừ dư, nên mình phải cộng lại cho huề
    # từ đây set 2 thg dưới thì phụ thuộc vào y luôn.\
print('hiện tại',y)
pdf.drawString(50,y-50,"Phương thức thanh toán")
pdf.drawString(50,y-100,"Tổng tiền")
# bên trên là do chưa set pagesiz nên nó bị tràn viền luôn, fix size là dc
# dính dách luôn
# giờ trừ ra tiếp
# # 4. Sub title Món ăn
# from reportlab.pdfbase.ttfonts import TTFont
# from reportlab.pdfbase import pdfmetrics

# pdfmetrics.registerFont(
#     TTFont('subTitle5','Roboto-Regular.ttf')
# )
# pdf.setFont('subTitle5',14)
# # do nó là mảng( linh động, tại vì có người ăn nhiều ăn ít, mảng nó ko cố định, nên mình lưu vào mảng cho nó co giãn thoải mái)
# # mà đển in cái mảng ra thì dùng for
# # vd
# # này là lặp lấy từng phần tử trong mảng
# # tương tự như trên
# # do cái này là mảng có chứ object nên để lấy từng giá trị của object thì bỏ ["giá trị cần lấy"] cái này t tra gg ra chứ cũng ngồi mò sml với thg python

# pdf.line(0,200,600,200)
# # nó in ra từ 0 đến 5 vì ko lấy bằng 6 :D. Này kiến thức C nên bn chắc biết r
# # 7. Sub title phương thức thanh toán



# from reportlab.pdfbase.ttfonts import TTFont
# from reportlab.pdfbase import pdfmetrics

# pdfmetrics.registerFont(
#     TTFont('subTitle14','Roboto-Regular.ttf')
# )
# pdf.setFont('subTitle14',20)
# pdf.drawString(10, 150, subTitle14)
# pdf.drawString(285, 150, subTitle15)

# # 8. Sub title Tổng tiền
# from reportlab.pdfbase.ttfonts import TTFont
# from reportlab.pdfbase import pdfmetrics

# pdfmetrics.registerFont(
#     TTFont('subTitle16','Roboto-Regular.ttf')
# )
# pdf.setFont('subTitle16',25)
# pdf.drawString(10, 110, subTitle16)
# pdf.drawString(285, 110, subTitle17)



# # ####################################################
# # # 3) Draw a line
# # pdf.line(30,710, 550, 710)








# # ####################################################
# # 4) Text object :: for large amounts of text
# # from reportlab.lib import colors

# # text = pdf.beginText(40, 680)
# # text.setFont("Courier", 18)
# # text.setFillColor(colors.red)
# # for line in textLines:
# #     text.textLine(line)

# # pdf.drawText(text)





# # #################################################
# # 5) Draw a image
# # pdf.drawInlineImage(image,130,400)




pdf.save()