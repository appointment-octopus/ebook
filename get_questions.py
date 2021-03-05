import urllib.request
from bs4 import BeautifulSoup
import sys


def fetch_links(tag):
    questions = []
    for filter in ['Votes', 'Frequent']:
        url = f"https://stackoverflow.com/questions/tagged/{tag}?tab={filter}"
        html = urllib.request.urlopen(url)

        soup = BeautifulSoup(html, features="html.parser")

        links = [i['href'] for i in soup.find_all('a', href=True) if '/questions/' in i['href'] and ('https://' not in i['href']) and ('/questions/tagged/' not in i['href']) and ('/questions/ask' not in i['href'])]
        questions.extend(links[:10])
    return list(dict.fromkeys(questions).keys())[:10]


def main():
    print(fetch_links(sys.argv[1]))


if __name__ == "__main__":
    main()
