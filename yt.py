
from bs4 import BeautifulSoup
from requests import get
import json
from time import sleep
from os import system
from os.path import exists
from subprocess import check_output as co
from glob import glob
from os import rename
from subprocess import run

def parse_process_output(process_output):
    out = ""
    if process_output.stdout:
        out += process_output.stdout.decode("utf8")
    if process_output.stderr:
        out += "!!!!!!!!!\n"
        out += process_output.stderr.decode("utf8")
    print(out)
    print(f"Command {'ok' if process_output.returncode == 0 else 'K.O !'}")
    #return (process_output.returncode, out)
# end def

class Youtube():
    # CLASS VARS
    search_url = "https://www.youtube.com/results?search_query="
    base_url = "https://www.youtube.com"

    def search(str_data):
        url = Youtube.search_url + str_data
        resp = get(url)
        id = resp.text.find("/watch?v=")
        end_url = resp.text[id:id+20]
        return f"{Youtube.base_url}{end_url}"
    # end def

    def get_meta(yt_url):
        cmd = f"youtube-dl {yt_url} --get-filename --get-duration --get-format --get-id"
        return parse_process_output(run(cmd.split(" "),capture_output=True))
    # end def

    def download_music(yt_url, wait_end = False):
        # it will create a .mp3 file
        cmd = f"youtube-dl --audio-format mp3 -x {yt_url}".split(" ")
        return parse_process_output(run(cmd, capture_output=wait_end))

    def download_video(yt_url, wait_end = False):
        # it will create a .mp3 file
        cmd = f"youtube-dl {yt_url}".split(" ")
        return parse_process_output(run(cmd, capture_output=wait_end))

def main():
    print("# REQUESTING")
    url = Youtube.search("toto hold the line")
    print(f"URL is {url}")

    print("# META")
    Youtube.get_meta(url)

    print("# DL WAIT")
    #Youtube.download_music(url, wait_end=True)

    print("# DL NO WAIT")
    #Youtube.download_music(url, wait_end=False)

    
    print("# DL NO WAIT")
    #Youtube.download_video(url, wait_end=False)
# end def

if __name__ == "__main__":
    main()
# enf if
