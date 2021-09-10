import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
import time

i = 201390105001
pd.set_option("display.max_rows",None)

name_list = []
en_list = []
mobile_list = []
gmail_list = []



headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0'}


# page = requests.get(url,headers=headers)
# soup = BeautifulSoup(page.content,'html.parser')
# result = soup.find('table',class_ = 'feesTable')
# print(result.text[8: (result.text.index('Enrollment No : ')-1)])
# print(result.text[(result.text.index('Enrollment No : ')+15):(result.text.index('Semester :')-3)])
# print(result.text[(result.text.index('Mobile :') + 8): result.text.index('Email :')-3])
# print(result.text[(result.text.index('Email :')+7):(result.text.index('Fees Details')-3)])

# print(result.text)

while i < 201390105100:
	url = 'http://27.54.181.205/bmef/online_fees_collection.php/?enrollment_no={}'.format(i)
	page = requests.get(url,headers=headers)
	soup = BeautifulSoup(page.content,'html.parser')
	result = soup.find('table',class_ = 'feesTable')
	name = (result.text[8: (result.text.index('Enrollment No : ')-1)]).strip()
	en = (result.text[(result.text.index('Enrollment No : ')+15):(result.text.index('Semester :')-3)]).strip()
	mobile = (result.text[(result.text.index('Mobile :') + 8): result.text.index('Email :')-1]).strip()
	gmail = (result.text[(result.text.index('Email :')+7):(result.text.index('Fees Details')-3)]).strip()
	
	if result == None :
		print('None')
	else:
		if name == '':
			print('No No {}'.format(i)) 
		else:
			name_list.append(name)
			en_list.append(en)
			mobile_list.append(mobile)
			gmail_list.append(gmail)



	i +=1

data = {'Name':name_list,'En No':en_list,'Mobile':mobile_list,'Email':gmail_list}

df = pd.DataFrame(data)

print(df)

time.sleep(60)
