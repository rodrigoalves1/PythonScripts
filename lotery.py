from urllib.request import urlretrieve
from urllib.request import urlopen
import re
try:
	import urllib.request as urllib2
except ImportError:
	import urllib2
try:
	from http.cookiejar import CookieJar
except ImportError:
	from cookielib import CookieJar
from bs4 import BeautifulSoup
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def mail(body,sbj):
	me = "from"
	you = "to"
	# Create message container - the correct MIME type is multipart/alternative.
	msg = MIMEMultipart('alternative')
	msg['Subject'] = sbj
	msg['From'] = me
	msg['To'] = you

	# Create the body of the message (a plain-text and an HTML version).
	text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"

	# Record the MIME types of both parts - text/plain and text/html.
	part1 = MIMEText(text, 'plain')
	part2 = MIMEText(body, 'html')

	# Attach parts into message container.
	# According to RFC 2046, the last part of a multipart message, in this case
	# the HTML message, is best and preferred.
	msg.attach(part1)
	msg.attach(part2)
	# Send the message via local SMTP server.
	mail = smtplib.SMTP('smtp.gmail.com', 587)

	mail.ehlo()

	mail.starttls()

	mail.login('your email', 'password')
	mail.sendmail(me, you, msg.as_string())
	mail.quit()



mega = []
lotomania = []

email = ""
#add your bets to the array
Mega = []
#add your bets to the array
Loto = []


def conferir_loteria(resultado,jogo):
	result = []
	for n in jogo:
		if n in resultado:
			result.append(n)
	return result

try:
	cj = CookieJar()
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
	requestMega = urllib2.Request("http://www.loterias.caixa.gov.br/wps/portal/loterias/landing/megasena")
	responseMega = opener.open(requestMega)

	cj1 = CookieJar()
	opener1 = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj1))
	requestLoto = urllib2.Request("http://www.loterias.caixa.gov.br/wps/portal/loterias/landing/lotomania")
	responseLoto = opener1.open(requestLoto)
except urllib2.HTTPError as e:
	print(e)
else:
	if requestLoto is None:
		print("url not found")
	else:
		htmlMega = responseMega.read()
		bsObjMega = BeautifulSoup(htmlMega)
		ulMega = bsObjMega.find("ul",{"class":"numbers mega-sena"})
		concurso = bsObjMega(text=re.compile("^Concurso"))
		#print(concurso)
		for li in ulMega:
			mega.append(li.string)

		email = "<html><h1><b>RESULTADO MEGA-SENA: " +str(concurso).strip('[\'\']')+"</b></h1><br/>"
		email += "<b>Números sorteados: "+str(mega[0:6]).strip('[]')+"</b>"
		#conferir mega
		for x in range(len(Mega)):
			email +="<br/><br/>NO JOGO"+ str(x+1)+":<br/>"
			email += str(Mega[x]).strip('[]')
			email +="<br/>Você acertou: "
			res = conferir_loteria(mega,Mega[x])
			email += str(len(res))
			email +="<br/>"+str(res).strip('[]')
		print(email)

		premiacao = bsObjMega.find("div",{"class":"related-box gray-text no-margin"}).findAll("p",{"class":"description"})
		for p in premiacao:
			email +="<br/><br/>"+ re.sub('\s\s+',' ',p.getText())+"<br/>"


		htmlLoto = responseLoto.read()
		bsObjLoto = BeautifulSoup(htmlLoto)
		tableLoto = bsObjLoto.find("table",{"class":"simple-table lotomania"}).findAll("td")
		concursoLoto = bsObjLoto(text=re.compile("^Concurso"))
		for td in tableLoto:
			lotomania.append(td.string)

		email += "<br/><br/><h1><b>RESULTADO LOTOMANIA: "+str(concursoLoto).strip('[\'\']')+" <b/></h1><br/>"
		email += "<b>Números sorteados:  "+ str(lotomania).strip('[]')+"</b>"
		#conferir loto
		for x in range(len(Loto)):
			email +="<br/><br/>NO JOGO"+ str(x+1)+":<br/>"
			email += str(Loto[x]).strip('[]')
			email +="<br/>Você acertou: "
			res = conferir_loteria(mega,Loto[x])
			email += str(len(res))
			email +="<br/>"+str(res).strip('[]')
		#print(email)


		premiacaoLoto = bsObjLoto.find("div",{"class":"related-box gray-text no-margin"}).findAll("p",{"class":"description"})
		for p1 in premiacaoLoto:
			email += "<br/><br/>"+re.sub('\s\s+',' ',p1.getText())+"<br/>"

		#print(email)

		mail(email,"Mega-Sena "+ str(concurso).strip('[\'\']') + " - Lotomania "+ str(concursoLoto).strip('[\'\']'))