from flask import Flask
from flask import request
from flask import Response
import requests

TOKEN = "TOKEN"
app = Flask(__name__)

def tel_send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendRichMessage'
    payload = {
                'chat_id': chat_id,
                'rich_message': {'markdown': text}
                }

    r = requests.post(url,json=payload)
    return r
    	

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        message = request.get_json()

        try:
        	chat_id = message['message']['chat']['id']
        	txt = message['message']['text']
        	tel_send_message(chat_id,txt)
        except KeyError:
        	print(message)
        	tel_send_message(chat_id,"Please send a plain text message, not forwarded from anyone")
        
        return Response('ok', status=200)
    else:
        return "<h1>Welcome!</h1>"

if __name__ == '__main__':
   app.run(debug=True,port=80,host='0.0.0.0')