import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()


url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:127.0) Gecko/20100101 Firefox/127.0",
            "Accept-Language": "en-US,en;q=0.5"}
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, "html.parser")

title = soup.title.string
whole_price = soup.find(class_="a-price-whole").text
fraction_price = soup.find(class_="a-price-fraction").text

print(f"Actual price: ${whole_price}{fraction_price}")


smtp_server = "smtp.office365.com"
smtp_port = 587  # Puerto para TLS
smtp_user = os.getenv("GMAILUSER")
smtp_password = os.getenv("GMAILPASS")

print(smtp_password)
print(smtp_user)
from_address = smtp_user
to_address = smtp_user 
subject = "Amazon Price Scraper"
body = f"Your product: {title}\nIs now at ${whole_price}{fraction_price}\n\n{url}"

msg = MIMEMultipart()
msg['From'] = from_address
msg['To'] = to_address
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Inicia la conexión TLS
    server.login(smtp_user, smtp_password)
    text = msg.as_string()
    server.sendmail(from_address, to_address, text)
    print("Correo enviado exitosamente")
except Exception as e:
    print(f"Error al enviar el correo: {e}")
finally:
    server.quit()