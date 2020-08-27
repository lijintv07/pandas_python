import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://www.bankbazaar.com/reviews.html'
page = requests.get(url)
#print(page.text)
soup = BeautifulSoup(page.text,'html.parser')
#print(soup)
review_text = []
review_text_elem = soup.find_all(class_='text_here review-desc-more')
#print(review_text_elem)
for item in review_text_elem:
	review_text.append(item.text)
#print(review_text)

user_name = []
user_name_elem = soup.find_all(class_='js-author-name')
#print(user_name_elem)

for item in user_name_elem:
	user_name.append(item.text)
#print(user_name)

bank_name = []
#bank_name_elem = soup.find_all('div',{'itemprop': 'datepublished'})
bank_name_elem = soup.find_all(class_ ='review-bank-title')
for item in bank_name_elem:
	bank_name.append(item.text)
#print(bank_name)
final_array=[]
for text,user,bank in zip(review_text,user_name,bank_name):
	final_array.append({'Review_text':text,'User':user,'Bank':bank})
df = pd.DataFrame(final_array)
print(df)