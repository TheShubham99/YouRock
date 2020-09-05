# ARGS :
# 1. image url
# 2. username
# 3. rec_email
# 4. organization name.

import cv2
import json
from PIL import Image
import smtplib
import sys
from io import BytesIO
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from urllib.request import urlopen
import numpy as np
import os

parsed_json=json.loads(sys.argv[1])

image_url=str(parsed_json['user']['avatarUrl'])
email=str(parsed_json['user']['email'])
username=str(parsed_json['user']['login'])



html = urlopen(image_url)
img_array = np.array(bytearray(html.read()), dtype=np.uint8)
background = cv2.imdecode(img_array, -1)

org=str(sys.argv[2])
maskPath = 'glasses.png'
cascPath = "haarcascade_frontalface_default.xml"

faceCascade = cv2.CascadeClassifier(cascPath)

gray = cv2.cvtColor(background, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(gray, 1.15)

image = background
background = cv2.cvtColor(background, cv2.COLOR_BGR2RGB)

background = Image.fromarray(background)


is_face = False

for (x, y, w, h) in faces:

    is_face = True

    mask = Image.open(maskPath)

    mask = mask.resize((w, h), Image.ANTIALIAS)

    offset = (x, y)

    background.paste(mask, offset, mask=mask)


# email op

sender_email = "yourockopensource@gmail.com"
rec_email = email
password = str(os.environ['GKEY'])

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
msg = MIMEMultipart()
msg['Subject'] = '@'+username+', Thank you for your Contribution.'
msg['From'] = "Prathamesh"
msg['To'] = rec_email
msgText = MIMEText(
    '<center><h1>Thank you &#129351; @'+username+'&#129351; | You Rock!</h1><img style="width:100%;" src="https://thepracticaldev.s3.amazonaws.com/i/6hqmcjaxbgbon8ydw93z.png"></img><center><p><t>Hey there<b>'+username+'</b>, <br><br>Thanks for your contribution in <b>'+org+'</b>.&#128522;<br>Your contribution gives motivation to everyone and we really appreciate it.<br>So please keep contributing.<br><br><b>Note - Please find attached.</b><br><br>~ A Maintainer <b>@'+org+'</b></p><center><img style="width:20em; height:auto;" src="https://media.giphy.com/media/U2LqsKYUCXCZp5u2jP/giphy.gif"></img><br></br><br></br><br></br></center></center><div style="text-align:center;width:100%;padding:20px;background:black;color:white;">Powered by Github Actions &emsp; &emsp; &emsp; | &emsp; &emsp; &emsp; Made for DEV.to Hackathon.<div></div>', 'html')
msg.attach(msgText)


# attach image
if(is_face):
    s_back = BytesIO()
    background.save(s_back, format='PNG')
    s_back = s_back.getvalue()

    background = BytesIO(s_back)
    img = MIMEImage(background.read())
    img.add_header('Content-Disposition', 'attachment', filename="You.jpg")
    msg.attach(img)

# image 2
with open('gold.png', 'rb') as fp:
    badge = MIMEImage(fp.read())
    badge.add_header('Content-Disposition', 'attachment', filename="Badge.png")
    msg.attach(badge)


server.login(sender_email, password)
server.sendmail(sender_email, rec_email, msg.as_string())
print("Email has been sent")
