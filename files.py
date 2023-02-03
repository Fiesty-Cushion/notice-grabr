import requests
import pdf2image
from datetime import datetime 
import os

year = datetime.now().strftime('%Y')
month = datetime.now().strftime('%m')

def createJPG(filename):
    month = "01"
    url = f"http://pcampus.edu.np/wp-content/uploads/{year}/{month}/{filename}"
    response = requests.get(url)
    images = pdf2image.convert_from_bytes(response.content)
    for i in range(len(images)):   
         images[i].save('images/'+'page'+ str(i) +'.jpg', 'JPEG')

def deleteImages():
    directory = os.fsencode("images")
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        path = f"images/{filename}"
        os.remove(path)
