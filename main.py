import requests
from bs4 import BeautifulSoup

#sending email libraries
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "jonsnow9091.fs@gmail.com"  # Enter your address
receiver_emails = ['kenan9091.fs@gmail.com', 'semraarik91@gmail.com',
                   'gsarik1414@gmail.com', 'frank9091.johansen@gmail.com']  # Enter receiver address
password = "piqsebtpohevyzin"


URL = 'https://www.amazon.com/Invoxia-Real-Time-GPS-Tracker/dp/B0B8K2CKDH/ref=sr_1_6?crid=1XDCM4ZAIT3RM&keywords=gps+tracker+for+bikes&qid=1677767749&sprefix=gsp+tracker+for%2Caps%2C172&sr=8-6'

headers = {'Accept-Language': 'en-US,en;q=0.9,tr-TR;q=0.8,tr;q=0.7,el-GR;q=0.6,el;q=0.5',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}

response = requests.get(url=URL, headers=headers)


soup = BeautifulSoup(response.text, 'html.parser')

price_item = soup.select_one('span.a-price-whole')
price_item_decimal = soup.select_one('span.a-price-fraction')
price_item_dollar_symbol = soup.select_one('span.a-price-symbol')
price_item_img = soup.select_one('div.imgTagWrapper > img')

print(price_item.getText() + price_item_decimal.getText() + price_item_dollar_symbol.getText())
print(soup.title.getText())
print(price_item_img.get('src'))

print(price_item.getText().replace('.', ''))
modified_price = int(price_item.getText().replace('.', ''))





final_price_msg = price_item.getText() + price_item_decimal.getText() + price_item_dollar_symbol.getText()
title_item = soup.title.getText()
item_src_img = price_item_img.get('src')

message = MIMEMultipart("alternative")
message["Subject"] = "Opportunity Lady and Gentlemen"
message["From"] = sender_email
message["To"] = ", ".join(receiver_emails)

# Create the plain-text and HTML version of your message


text = """\

                 The Best Advertising!!

                """

html = """\
                    <html>
                      <body>
                       <h1>
                       Great Cheapest Price Chance On AMAZON!!!
                        </h1>

                      </body>
                    </html>
                    """ + f'{title_item}\n'\
                        + f'{final_price_msg}\n'\
                        + f'{item_src_img}\n'

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

context = ssl.create_default_context()
if modified_price < 60:
    print('The price is down!!')
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_emails, message.as_string())