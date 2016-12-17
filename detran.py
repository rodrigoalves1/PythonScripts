import requests
from bs4 import BeautifulSoup as bs
import sys, re

if len(sys.argv) > 1:
	url = "http://online7.detran.pe.gov.br/ServicosWeb/Veiculo/frmConsultaPlaca.aspx?placa=" + sys.argv[1];
	fields = {
	'__VIEWSTATE':'/wEPDwUKMTk0NzUzNTkyOA9kFgICAQ9kFgICBQ9kFgICAw9kFhwCBQ8PFgIeBFRleHQFB0tITDQxOTFkZAIHDw8WAh8ABRE5QkQxNzIwNkc4MzM5OTg5NGRkAgkPDxYCHwAFGFBBUyZuYnNwOyZuYnNwO0FVVE9NT1ZFTGRkAgsPDxYCHwAFCkFMQ08vR0FTT0xkZAINDw8WAh8ABRRGSUFUL1NJRU5BIEZJUkUgRkxFWGRkAg8PDxYCHwAFBDIwMDhkZAITDw8WAh8ABQQyMDA4ZGQCFQ8PFgIfAAUJNS82Ni8xMDAwZGQCFw8PFgIfAAUGUEFSVElDZGQCGQ8PFgIfAAUFQ0lOWkFkZAIjDw8WBB8ABRpBTC4gRklELiBCQiBBRE0gREUgQ09OUyBTQR4HVmlzaWJsZWdkZAInDw8WBB8AZR8BZ2RkAikPDxYEHwBlHwFnZGQCKw8PFgQfAAWsBEJhaXhhIGRvIGdyYXZhbWUgYXV0b3JpemFkbyBwZWxvIFNpc3RlbWEgTmFjaW9uYWwgZGUgR3JhdmFtZXMuIEFnZW5kZSBhIHZpc3RvcmlhIGUgcG9zdGVyaW9yIGF0ZW5kaW1lbnRvIGRlIHZlw61jdWxvIHBhcmEgcmVhbGl6YcOnw6NvIGRvIHNlcnZpw6dvIGRlIEJhaXhhIGRlIEdyYXZhbWUgYXByZXNlbnRhbmRvIENSViBvcmlnaW5hbCwgZm90b2PDs3BpYXMgZGEgaWRlbnRpZGFkZSBlIENQRiwgY29tcHJvdmFudGVzIGRlIHBhZ2FtZW50b3MgZGUgdGF4YXMgZSBtdWx0YXMsIHNlIGhvdXZlci4gTsOjbyBzZW5kbyBvIHByb3ByaWV0w6FyaW8sIGFwcmVzZW50YXIgYSBwcm9jdXJhw6fDo28gZGVudHJvIGRhcyBub3JtYXMgZXhpc3RlbnRlcy48YnIgLz4gTm8gY2FzbyBkZSBMZWFzaW5nLCBhbnRlcyBkb3MgcGFzc29zIGFudGVyaW9yZXMsIHNpZ2EgYXMgb3JpZW50YcOnw7VlcyBkbyBCYW5jby9GaW5hbmNlaXJhLCBiZW0gY29tbywgb2J0ZW5oYSBvcyBkb2N1bWVudG9zIHBhcmEgcmVhbGl6YXIgYSBUcmFuc2ZlcsOqbmNpYSBkZSBQcm9wcmllZGFkZSBkbyBWZcOtY3Vsby4fAWdkZGRpf6JYPXTf9sRF8/mIW4kW/CblVJPTGV9BUgB1UbWBFQ==',
	'__EVENTVALIDATION':'/wEWAwKItLzvAgKwyr6sDQL56bmBBsRTeL0qYVFXs03fIy2WFr/bnTus1xoV12Qj7jgCndUv',
	'btnDetalhamento':'Detalhamento de Débito'}

	r = requests.post(url, fields);

	print(r.status_code, r.reason)

	print(r.content)

	s = bs(r.content, "html.parser")
	print(s.find("table",{"class":"grid"}))
	print(s.find(re.compile("^MULTAS")))
	#TODO: send mail with informations in a mora readable format
else:
	 print("[ ! ] Executar o script junto com a placa do carro: ./detran.py <placa>  | ./detran.py XXX1234")