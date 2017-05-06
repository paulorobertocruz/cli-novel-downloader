from bs4 import BeautifulSoup
import requests
import sys, cmd
import os

BASE_DIR = os.path.dirname( os.path.realpath(__file__))

class Download(cmd.Cmd):
    intro = "Intro Downloader"
    prompt = "(Downloader)"
    file = None

    def do_download_isekai(self, arg):

        home_url = "https://isekailunatic.wordpress.com/tsuki-ga-michibiku-isekai-douchuu/"
        response = requests.get(home_url)
        home_file = open( os.path.join(BASE_DIR, arg + ".html"), "w")
        home_file.write(response.text)
        home_file.close()

    def do_clean(self, arg):

        sdir = os.path.join(BASE_DIR, "isekai")

        home_file = open( os.path.join(BASE_DIR, arg + ".html"), "r+")
        so = BeautifulSoup(home_file.read(), "html.parser")
        l = so.find("div", {'class': 'entry-content'})
        links = l.find_all("a")

        for a in links:
            #save file
            href = a.get('href')
            file_name = str(a.string)

            if file_name is None or href is None:
                continue

            for a in "[].,;!@#$%&*()+=/\\ ":
                file_name = file_name.replace(a,'_')

            file_name = file_name.replace("https:",'')
            file_name = file_name.replace("http:",'')
            file_name = file_name.replace("www",'')
            file_name = file_name.replace("cojp",'')
            file_name = file_name.replace("com",'')
            file_name = file_name.replace(":",'-')


            response = requests.get(href)
            print(response)
            html_file = open( os.path.join(sdir, file_name + ".html"), "w")

            html_file.write(response.text)

            html_file.close()


        clean_html = "<html><body>{0}</body></html>"


    def homepage(self, arg):
        pass


    def close(self):
        if self.file:
            self.file.close()
            self.file = None

    def do_exit(self, arg):
        self.close()
        exit()

if __name__ == '__main__':
    Download().cmdloop()
