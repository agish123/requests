# app.py
from flask import Flask
import requests

app = Flask(__name__)

@app.route('/fetch-data')
def fetch_data():
    try:
        response = requests.get("https://httpbin.org/get", timeout=5)
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}, 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)