from bs4 import BeautifulSoup
import requests
import sys
import os

show_traceback = True

BASE_DIR = os.path.dirname( os.path.realpath(__file__))
DOWNLOADS_DIR = os.path.join(BASE_DIR, "downloads")

folder = None

while folder is None:
    print("Onde deseja salvar os arquivos")
    folder_name = input("diretorio:")
    folder_name = os.path.join(DOWNLOADS_DIR, folder_name)

    if os.path.isdir(folder_name):
        usar = input("diretorio existe, usar?<s/N>") or "n"
        usar = usar.lower()
        if usar == "s":
            folder = folder_name
            print(folder)
    else:
        print("diretorio nao existe")
        try:
            os.makedirs(folder_name)
            folder = folder_name
            print(folder)
        except:
            if show_traceback:
                print(sys.exc_info())
            folder = None


htmlpage = None

while htmlpage is None:

    url = input("url:")

    if "http://" not in url and "https://" not in url:
        url = "http://" + url

    print("url:", url)

    try:
        htmlpage = requests.get(url)
        print(htmlpage)
    except requests.exceptions.ConnectionError:
        t, v, traceback = sys.exc_info()
        print("problema conectando com url")
        if show_traceback:
            print(t)
            print(v)
            print(traceback)
    except requests.exceptions.RequestException:
        htmlpage = None
        print(sys.exc_info())



div = input("tag:?")
print("tag:", div)

domcument = BeautifulSoup(htmlpage.text, "html.parser")
l = so.find(tag, {'class': 'entry-content'})
