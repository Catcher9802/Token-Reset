import requests

def reset_tokenbot(token, id):
	head = {
	    "authorization": token
	    }
	r = requests.post(f"https://discord.com/api/v9/applications/{id}/bot/reset",headers=head)
	print(r.text)
	
reset_tokenbot("TOKEN ME", "BOT ID")

# สคริปต์รีเซ็ตโทเค็นบอท