from bs4 import BeautifulSoup
import requests
import re

def remove_tags(text):
	return re.compile(r'<[^>]+>').sub('', text)


def getHoro(char, date):
	headers = requests.utils.default_headers()
	headers.update({'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/532.1.0 (KHTML, like Gecko) Chrome/34.0.822.0 Safari/532.1.0',})
	url = requests.get('https://horo.mail.ru/prediction/' + char + '/' + date + '/', headers=headers)
	s = BeautifulSoup(url.text, 'html.parser')
	title = s.find("h1", {"data-qa": "Title"}).getText()
	date = s.find("span", {"data-qa": "Text"}).getText()
	text = s.find("main", {"data-qa": "ArticleLayout"})
	text = re.sub(r'<a(.*?)</a>', '', str(text))
	text = remove_tags(text)
	content = '<b>☀️ <a href="https://horo.mail.ru/prediction/">' + title + '</a></b>\n\n<b>🗓' + date + '</b>\n\n💬 ' + text
	return content