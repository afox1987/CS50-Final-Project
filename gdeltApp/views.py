import json
from django.shortcuts import render
from django.views import  View
from django.views.decorators.csrf import csrf_exempt
import smtplib
import requests
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from django.http.response import HttpResponse, JsonResponse
import os
import re
import json
import objectpath
import requests
from collections import Counter
import pycountry
from bs4 import BeautifulSoup
from pathlib import Path

# Create your views here.

class index(View):
	return_url = None
	def get(self , request,Id=0):
		return render(request , 'index.html')

class Map_View(View):
	return_url = None
	def get(self , request,Id=0):
		return render(request , 'mapview.html')

class Article_View(View):
	return_url = None
	def get(self , request,Id=0):
		return render(request , 'articleview.html')

class Contact_view(View):
	return_url = None
	def get(self , request,Id=0):
		return render(request , 'contactus.html')

	@csrf_exempt
	def post(self , request,Id=0):
		cname = request.POST.get('contact_name')
		cemail = request.POST.get('contact_email')
		csubject = request.POST.get('contact_subject')
		cmessage = request.POST.get('contact_message')
		sender_address = 'infoswap90@gmail.com'
		sender_password = 'Swapna@234'
		gmail_port = 587
		mail_content = '''
<html>
  <head></head>
  <body>
  <h1>Hi One-News</h1
  <p>UserName : ''' + cname + ''' </p>
  <p>Email : ''' + cemail + ''' </p>
  <p>Subject : ''' + csubject + ''' </p>
  <p>Messagee : ''' + cmessage + ''' </p>
  <b><p>Thank you <br/> One-News </p></b>
  </body>
</html>
'''
		receiver_address = 'infoswap90@gmail.com'
		message = MIMEMultipart()
		message['From'] = 'infoswap90@gmail.com'
		message['To'] = receiver_address
		message['Subject'] = 'Contact Inquiry Reached'
		message.attach(MIMEText(mail_content, 'html'))
		data_folder = str(os.path.join(Path.home(), "Downloads"))
		session = smtplib.SMTP('smtp.gmail.com', 587)
		session.starttls() # enable security
		session.login(sender_address, sender_password)
		#text = message.as_string()
		session.sendmail('infoswap90@gmail.com', receiver_address, message.as_string())
		session.quit()
		print('Email Sent')
		return render(request, 'contactus.html', {'message': "Thank you for Contacting us we will contact you soon."})

def GetMapView(request):
	if(request.method == "GET"):
		keywrd1 = request.GET['keywrd']
		url = "https://api.gdeltproject.org/api/v2/doc/doc?query="+keywrd1+"&format=json"
		response = requests.get(url)
		data = []
		data2 = json.loads(response.content)
		if(len(data2)!=0):
			for i in data2['articles']:
				dateParam = i['seendate']
				dateParam =  dateParam[ 0 : 8 ]
				dtyr = dateParam[ 0 : 4 ]
				dtm = dateParam[ 4 : 6 ]
				dtd = dateParam[ 6 : 8 ]
				data.append({
					"url":i['url'],
					"title":i['title'],
					"date": dtd + "-" + dtm + "-" + dtyr,
					"image":i['socialimage'],
					"domain":i['domain'],
					"sourcecountry":i['sourcecountry'],
					"language":i['language'],
					})
		else:
			data.append({
					"url":"",
					"title":"",
					"date": "",
					"image":"",
					"domain":"",
					"sourcecountry":"",
					"language":"",
				})
		responseData = {
				"data":data,
			}
		return JsonResponse(responseData) 

def GetMainView(request):
	if(request.method == "GET"):
		solditems = requests.get('https://api.gdeltproject.org/api/v1/gkg_geojson?QUERY=WB_133_INFORMATION_AND_COMMUNICATION_TECHNOLOGIES&TIMESPAN=60') # (your url)
		data = solditems.json()
		with open('data.txt', 'w') as f:
			json.dump(data, f)
		
		with open('data.txt') as jsonfile:
			data = json.load(jsonfile)
			jsonnn_tree = objectpath.Tree(data['features']) 
			result = jsonnn_tree.execute('$.properties')
		countries = {}
		for country in pycountry.countries:
			countries[country.name] = country.alpha_2
		names = []
		urllst =[]
		for pr in result:
			title = pr['name']
			url = pr['url']
			for country in pycountry.countries:
				if country.name in title:
					names.append(country.name)
					urllst.append({"name":country.name,"url":url})
		
		cname = []
		cvalues = []
		cgeoval = []
		mainurls = []
		for ckey in Counter(names).keys():
			cname.append(ckey)
		for cvalue in Counter(names).values():
			cvalues.append(cvalue)
		codes = [countries.get(country, 'Unknown code') for country in cname]
		for name in cname:
			filtered = list(filter(lambda f: (f["name"] == name), urllst))
			urlname = ''
			inturl = []
			for furl in filtered:
				if furl['url'] not in inturl:
					inturl.append(furl['url'])
					urlname += "<a href=" +furl['url']+ " target='_blank'>" +furl['url']+ "</a><br>"
				mainurls.append(urlname)
		for val in cvalues:
			codeval = val/len(names)
			cgeoval.append(round(codeval, 4))
		responseData = {
			"names":cname,
			"values":cgeoval,
			"codes":codes,
			"urls":mainurls
			}
		return JsonResponse(responseData) 