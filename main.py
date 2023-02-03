import requests
from datetime import datetime
from bs4 import BeautifulSoup
import json
from files import *
from webhook import *


year = datetime.now().strftime('%Y')
month = datetime.now().strftime('%m')
month = "01"

url = f"https://pcampus.edu.np/wp-content/uploads/{year}/{month}/?C=M;O=A"

def scraper():
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')
    with open('files.txt', 'w', encoding="utf-8") as f:
        for a in soup.find_all('a', href = True):    
            if '.' in a['href']:
                file = a['href']        
                f.write(file)
                f.write("\n")

def checkForUpdate():
    file1 = open("files.txt", 'r')
    file2 = open("sent.txt", 'r')
    """
    Check both files for any change
    and trigger webhook if any change
    """


    file1.close()
    file2.close()

#scraper()
#createPDF("Namelist2-1.pdf")
#createWebHook("https://pcampus.edu.np/wp-content/uploads/2023/01/Namelist2-1.pdf")
checkForUpdate()