from flask import Flask, request, jsonify
from ghettobird import fly
import json
from selenium import webdriver
from pprint import pprint
import os

app = Flask(__name__)

@app.route('/', methods=["POST"])
def main():
    routine = request.json
    options = None
    browser = None
    if "options" in routine.keys():
        options = routine["options"]
        if "browser" in options.keys():
            if options["browser"] == True:
                chrome_options = webdriver.ChromeOptions()
                chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
                chromedriver_location = 'c:/chromedriver.exe'
                options["browser"] = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    result = fly(routine)
    if browser:
        browser.quit()
    return jsonify(result["results"])

if __name__ == '__main__':
    app.run()

# export FLASK_APP=main.py
