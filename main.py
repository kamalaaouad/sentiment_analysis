import torch
from transformers import pipeline
#import torch

import torch as t

from transformers import AutoTokenizer, AutoModelForSequenceClassification

#tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")

#model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")

print(t.__version__)
x = torch.rand(3)
#classifier = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")
classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

pos_text = "I enjoy studying computational algorithms."
neg_text = "I dislike sleeping late everyday."

res = classifier(pos_text)
res2 = classifier(neg_text)
print(res)
print(res2)
print(x)