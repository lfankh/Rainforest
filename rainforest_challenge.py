# -*- coding: utf-8 -*-

import requests

def rainforest_challenge(y):
	req_url = requests.get(y)
	main_url = "http://www.letsrevolutionizetesting.com/challenge.json?id="
	if 'follow' in req_url.json():
		next_url = req_url.json().get('follow')
		new = main_url + next_url.split("=")[-1]
		rainforest_challenge(new)
	else:
           	#Show output if it exists
		print y.text

if __name__ == "__main__":
	url = "http://www.letsrevolutionizetesting.com/challenge.json"
	rainforest_challenge(url)
