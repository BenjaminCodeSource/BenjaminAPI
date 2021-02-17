from flask import Flask
import jsonify, requests, json, time


app = Flask(__name__)
@app.route('/<benjamin>', methods=['GET', 'POST'])
def spam(benjamin):
  return(benjamin)
if __name__=='__main__':
 app.run(debug=True)

