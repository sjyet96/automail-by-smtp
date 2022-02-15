import smtplib
from email.message import EmailMessage

# 메일 제목, 보내는 사람, 받는 사람, 메시지 작성
msg = EmailMessage()
msg["Subject"] = "예) 테스트 메일 송부"
msg["sjyet96@kiria.org"] = "예) 본인@naver.com"
msg["sjyet96@kiria.org"] = "예) 상대@naver.com"
msg.set_content("예) 테스트 본문 내용입니다")

#파일첨부 (MIME Type)
#with open("예) files.xlsx", "rb") as f: 
#    msg.add_attachment(f.read(), maintype="예) application",\
#         subtype="예) vnd.ms-excel", filename=f.name)
    

# 메일송부
with smtplib.SMTP_TLS("mail.kiria.org", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("sjyet96", "Songjiyou@1")
    smtp.send_message(msg)