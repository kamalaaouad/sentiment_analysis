from flask import Flask, request
import torch
from transformers import pipeline





app = Flask(__name__)

@app.route("/addme", methods=['POST'])
def hello():
    classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

    pos_text = request.form.get('pos_text')
    neg_text = request.form.get('neg_text')

    res = classifier(pos_text)
    res2 = classifier(neg_text)
    return str(res)+" - "+str(res2)

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
    #app.run()