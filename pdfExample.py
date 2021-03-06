#####################################
#help
from os import linesep
from typing import Text
from reportlab.lib import colors
from reportlab.lib.units import cm, inch



# này lè set cứng cái size, nhưng mà để nó auto theo danh sách thì tra gg đéo ra :D
# Nên mình chơi proplayer :D tự code




 
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
  {
    "name":"Cơm",
    "quantity":2,
    "price":1000
  }
]



#Sub title phương thức thanh toán
subTitle14 = 'Phương thức thanh toán:'

#Sub title kết quả
subTitle15 = 'MoMo'

#Sub title sum
subTitle16 = 'Tổng thanh toán:'

#Sub title kết quả sum
subTitle17 = '300.000 VNĐ'

# ######################################################
# 0)create document
from reportlab.pdfgen import canvas
# nó hơi còn phần trống nên mình cắt bới kích thước gốc cho nó gọn lại
_W, _H = (575, 450 + (50*len(textLines)))
# xét cứng xem nó dc bao nhiêu
A4 = (_W, _H)
pdf = canvas.Canvas(filename,pagesize=A4)
pdf.setTitle(documentTitle)

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
# VD cho cái trang này cao 770 đi ha
# nó bị tràn :D nên phải tăng lên tí
# Ok đẹp rồi giờ ngồi phân tích kích thước thg thằng
pdf.drawString(10, _H-20, title)
pdf.drawString(10, _H-40, title1)
pdf.drawString(10, _H-70, title2) 
pdf.line(0,_H-80,700,_H-80)

pdf.drawString(10, _H-100, title3)
pdf.drawString(10, _H-120, title4)

# Giờ tính cái kích thước của theo danh sách








# ################################################
# 2) Sub Title 1 :: tiêu đề
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

pdfmetrics.registerFont(
    TTFont(subTitle1,'Roboto-Bold.ttf')
)
pdf.setFont(subTitle1,30)
pdf.drawCentredString(290, _H-170, subTitle1)

#  3)Sub Title 2 :: tiêu đề bảng
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

pdfmetrics.registerFont(
    TTFont('subTitle2','Roboto-Regular.ttf')
)
pdf.setFont('subTitle2',25)
# pdf.setFont('subTitle2',25)
pdf.drawString(50, _H-220, subTitle2)

# subTitle 3 
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

pdfmetrics.registerFont(
    TTFont('subTitle3','Roboto-Regular.ttf')
)
pdf.setFont('subTitle3',25)
pdf.drawString(270,  _H-220, subTitle3)

# subTitle 4 
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

pdfmetrics.registerFont(
    TTFont('subTitle4','Roboto-Regular.ttf')
)
pdf.setFont('subTitle4',25)
pdf.drawString(410,  _H-220, subTitle4)

#gạch ngang (bắt đầu, khoảng cách x từ trên xuống, điểm kết thúc, khoảng cách x từ trên xuống)
pdf.line(0, _H-230,600, _H-230)
# dm ko thấy chỗ này
y=_H-270
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

pdfmetrics.registerFont(
    TTFont('name','Roboto-Regular.ttf')
)
pdf.setFont('name',14)
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
    # Tại đây mỗi thg sẽ thụt xuống 50 vậy nghĩa là thêm mỗi dòng sẽ + vào 50 chiều dài
    # vd thêm 2 thì sẽ cộng thêm 100 :D 3 thfi 150 nên chiều dài sẽ bằng chiều dài của đơn 1 hàng + chiều dài của 50 nhân với số lượng hàng
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
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

pdfmetrics.registerFont(
    TTFont('Phương thức thanh toán:','Roboto-Regular.ttf')
)
pdf.setFont('Phương thức thanh toán:',20)
pdf.drawString(50,y-50,"Phương thức thanh toán:")


# ##########################################################################
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

pdfmetrics.registerFont(
    TTFont('Tổng tiền:','Roboto-Regular.ttf')
)
pdf.setFont('Tổng tiền:',25)
pdf.drawString(50,y-100,"Tổng tiền:")
# bị dư ở dưới nên mình trừ cái viền ( thôi trừ thêm viền cho đẹp)
# Giờ xem thử đơn 1 hàng nó có chiều dài bao nhiêu nha
# @.@ lỗi chỗ nào rồi để t xem lại tẹo

# print(_H - (y-5))
# 355 là chiều dàu của đơn hàng 1 sản phẩm đã trừ viền dư ở đít :D

# bên trên là do chưa set pagesiz nên nó bị tràn viền luôn, fix size là dc
# dính dách luôn
# giờ trừ ra tiếp




pdf.save()