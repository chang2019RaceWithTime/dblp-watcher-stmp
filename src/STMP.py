# 需要使用到SMTPLIB库来进行邮箱的连接
import smtplib
# 处理邮件内容的库，email.mine
from email.mime.text import MIMEText

# 邮箱属性配置

# 邮箱服务端
def sendemail(msg):
    mailserver = 'smtp.qq.com'
    # 发件人-填写自己的邮箱
    userName_SendMail = '@qq.com'
    # 邮箱发件授权码-为发件人生成的授权码
    userName_AuthCode = 'XXXXX'
    # 定义邮件的接收者-我随便写的，若收件人较多，可用列表表示
    received_mail = ['XXXX','XXXXXXXXX']

    # 发送一封简单的邮件，处理邮件内容
    content = msg
    # 纯文本形式的邮件内容的定义，通过MIMEText进行操作，plain为默认的文本的展示形式
    email = MIMEText(content, 'plain', 'utf-8')
    email['Subject'] = '今日文献更新' # 定义邮件主题
    email['From'] = userName_SendMail  # 发件人
    email['To'] = ','.join(received_mail)  # 收件人（可以添加多个，若只有一个收件人，可直接写邮箱号）

    # 发送邮件

    # QQ邮箱的端口号是465，其他邮箱的端口号可自行百度，非QQ邮箱，一般使用SMTP即可，不需要有SSL
    smtp = smtplib.SMTP_SSL(mailserver, port=465)
    smtp.login(userName_SendMail, userName_AuthCode)
    smtp.sendmail(userName_SendMail, ','.join(received_mail), email.as_string())

    smtp.quit()
