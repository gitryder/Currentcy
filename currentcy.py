import requests 
from bs4 import BeautifulSoup 

def current_dollar_rate():
	url = "https://goo.gl/CPDLmt"
	source_code = requests.get(url)
	plain_text = source_code.text 
	soup = BeautifulSoup(plain_text, "html.parser")
	for text in soup.findAll('span', {'class': 'uccResultAmount'}):
		return text.string




	


