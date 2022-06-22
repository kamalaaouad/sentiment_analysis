from flask import Flask, request, jsonify
# import torch
import json
from transformers import pipeline

app = Flask(__name__)


classifier = pipeline("sentiment-analysis", model='rabindralamsal/BERTsent')


@app.route('/', methods=['GET'])
def home():
    print('hi')
    #return jsonify(message=str("index.html"))
    language = "Python"
    company = "Oreivaton"
    Itemid = 1
    price = 0.00

    # Create Dictionary
    value = {
        "language": language,
        "company": company,
        "Itemid": Itemid,
        "price": price
    }

    # Dictionary to JSON Object using dumps() method
    # Return JSON Object
    return json.dumps(value)
    #return json.dump({'message': "index.html"})


@app.route("/detect_sentiment", methods=['POST'])
def detect_sentiment():
    print('hello')
    print('hello')
    data_text = request.form.get('data_text')
    data = request.get_json(force=True)
    print(request.get_json())
    print(data["data_text"])
    res = classifier(data["data_text"])
    return json.dumps(res[0])
    #return json.dumps({"meg": data_text})


if __name__ == "__main__":
    from waitress import serve

    serve(app, host="0.0.0.0", port=8089)
    # app.run()
