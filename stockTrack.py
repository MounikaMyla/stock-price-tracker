# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 09:14:22 2017

@author: mylam
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 13:55:54 2017

@author: mylam
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 12:30:37 2017

@author: mylam
"""
def send_mail(parameter,percent):
    import smtplib
    #from email.MIMEMultipart import MIMEMultipart
    #from email.MIMEText import MIMEText
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart


    fromaddr = "terry2012536@gmail.com"
    toaddr = "mt84536@gmail.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Price Alert!!"
    percent=round(percent,2)
    print(percent)
    percent1=str(percent)
    body = "Hello Mounika! The Price of "+name+parameter+" by "+percent1+"%. \nCheck your portfolio now. \nhttp://www.moneycontrol.com/bestportfolio/wealth-management-tool/stock_watchlist"
    print(body)
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("terry2012536@gmail.com", "terry536")
    #msg["subject"]="Price Alert!!"
    #msg = "Hello Mounika! The Price of Goa Carbon increased 4% or more"
    server.sendmail(fromaddr,toaddr, msg.as_string())
    server.quit()

import csv
name=request.GET['stock_name']
print("hello to git")
per=request.GET['percent']
L=[name,per]
fi=open("CSVstockList.csv")
for row in L:
  csv.writer(fi).writerow(row)    

import csv

f=open("stockList.csv",'r')
#f=csv.reader(file)
for line in csv.reader(f):
  #print(line[0])
  stock_name=line[0].replace(" ","")
  #print(stock_name)
  #stock_name=stock_name.strip('&')
  #print(stock_name)
  import requests
  import re
  category=r'[^\/]+'
  code=r'[^\/]+'
  #import re
 # https?://[^\s<>"]+|www\.[^\s<>"]+
 # reg=re.compile("http://www.moneycontrol.com/india/stockpricequote/([^\/]"+stock_name+"/([^\/]/")
  #link=reg.matches()
  #link=re.findall("[http://www.moneycontrol.com/india/stockpricequote/]+.*[/]+"+stock_name+"[/]+.*[/]+","")
  link="http://www.moneycontrol.com/india/stockpricequote/[a-zA-Z]/"+stock_name+"/"
  print(link)
  #import os
  #sURL = os.path.realpath('.')
  #print('sURL = ' + sURL + '<br />')
  #url = os.environ['HTTP_HOST']
  #uri = os.environ['REQUEST_URI']
  #print(uri)
  #import os
  #print(os.environ["REQUEST_URI"])
  page=requests.get(link)
  print(page)
  from bs4 import BeautifulSoup
  soup=BeautifulSoup(page.content,'html.parser')
  #print(soup.prettify())
  nametag_list=soup.find_all('div',class_='b_42 PT5 PR')
  nametag=nametag_list[0]
  #print(nametag.prettify())
  name=nametag.find().get_text()
  divtag=soup.find_all('div',class_='FL gL_13 PT15')
  divtag1=divtag[0]
  #print(divtag1.prettify())
  period = divtag1.find().get_text()
  print("Period is:",period)
  pricetag=soup.find_all('div',id='Bse_Prc_tick_div')
  price=pricetag[0]
  #print(price.prettify())
  currentprice=price.find().get_text()
  print("Current Price:",currentprice)
  a=float(period)
  b=float(currentprice)
  percent=((a/(b-a))*100)
  print(percent)
  required_percent=float(line[1])
  if required_percent<0:
      if percent<=required_percent:
          send_mail(" decreased",percent)
  else:
      if percent>=required_percent:
          send_mail(" increased",percent)
  #if percent:
    #msg1=

 # temp=soup.find_all('span', class_="gr_15 uparw_pc")
#print(temp)
f.close()