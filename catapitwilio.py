import requests
from PIL import Image
import io
from twilio.rest import Client
import datetime

def request_api_data():
	url = 'https://api.thecatapi.com/v1/images/search'
	payload = {}
	headers = {
	  ' ': ''
	}
	response = requests.request('GET', url, headers = headers, data = payload)
	'''
	print('--------------')
	print(response)
	print('--------------')
	print(response.text)
	print('--------------')
	'''

	data = response.json()

	'''
	print(data)
	print('--------------')
	'''

	image_url = data[0]['url']

	'''
	print(image_url)
	print('--------------')
	'''

	e = datetime.datetime.now()
	print(e.strftime('%a, %b, %d, %Y'))
	print(e.strftime('%I:%M:%S %p'))

	account_sid = ''
	auth_token = ''

	client = Client(account_sid, auth_token)
	message = client.messages.create(
		to = '', 
		from_ = '', 
		body = 'Good Morning! Today is ' + e.strftime('%a, %b, %d, %Y') + ' ' + e.strftime('%I:%M:%S %p') + ' Check this out: ' + image_url)

	if response.status_code != 200:
		raise RuntimeError(f'Error fetching: {response.status_code}, check the api and try again')
	return response

request_api_data()




