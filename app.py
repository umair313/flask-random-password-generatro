from flask import Flask, json, render_template, request
import json
import string
import random

app = Flask(__name__)
app.debug = True

@app.route('/')
def home():
    return render_template("index.html")


def generatePassword(pass_len):
    printable_chars = string.printable[:-2]
    for r in ['\t','\n','\r',' ']:
        printable_chars = printable_chars.replace(r,'')
    random_chars = random.sample(printable_chars, pass_len)
    return ''.join(random_chars)


@app.route('/genpass', methods=["POST"])
def passwordGenerateRequest():
    if request.method == "POST":
        try:
            pasword_length = int(request.json['length'])
            data = {
                "password" : generatePassword(pasword_length)
            }
        except:
            data = {
                'password' : False,
            }
        return json.dumps(data)
        

        