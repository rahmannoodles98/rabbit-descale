import os
from flask import Flask
app = Flask(__name__)
import requests
import json
from dotenv import load_dotenv
load_dotenv()


@app.route('/')
def get():
  headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
  # input your api key
  data = {
      'grant_type': 'urn:ibm:params:oauth:grant-type:apikey',
      'apikey': os.environ.get("API_KEY")
      }

  # refresh iam token
  response = requests.post(
      'https://iam.cloud.ibm.com/identity/token', headers=headers, data=data)
  iam_token = response.json()['access_token']

  url = "https://api.us-south.databases.cloud.ibm.com/v5/ibm/deployments/crn:v1:bluemix:public:messages-for-rabbitmq:us-south:a%2Fcdefe6d99f7ea459aacb25775fb88a33:e5b49219-b7c1-461f-83cb-cf9eaab94ddf::/groups/member"

  payload = json.dumps({
      "memory": {
          "allocation_mb": 3840
      }
  })
  headers = {
      'Authorization': f"{iam_token}",
      'Content-Type': 'application/json'
  }

  response = requests.request("PATCH", url, headers=headers, data=payload)
  return "done" + str(response.status_code)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3500)
