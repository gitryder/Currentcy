import requests 
from bs4 import BeautifulSoup 

def current_dollar_rate():
	url = "https://goo.gl/CPDLmt"
	source_code = requests.get(url)
	plain_text = source_code.text 
	soup = BeautifulSoup(plain_text, "html.parser")
	for text in soup.findAll('span', {'class': 'uccResultAmount'}):
		return text.string

def currentcy_rate(FROM, TO, multiplier = 1):
	url_pOne = "https://www.xe.com/currencyconverter/convert/?Amount=1&From="
	url_pTwo = str(FROM)
	url_pThree = "&To="
	url_pFour = str(TO)
	rate = 1

	url = url_pOne + url_pTwo + url_pThree + url_pFour
	source_code = requests.get(url)
	plain_text = source_code.text 
	soup = BeautifulSoup(plain_text, "html.parser")
	for text in soup.findAll('span', {'class': 'uccResultAmount'}):
		rate = text.string
	todays_rate = rate
	total = float(multiplier) * float(todays_rate)

	return round(total, 2)
 









	


