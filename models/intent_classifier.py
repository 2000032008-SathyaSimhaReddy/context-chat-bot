from transformers import pipeline
class IntentClassifier:
    def __init__(self):
        self.classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
        self.labels = ["greeting","goodbye","help","thanks","other"]
    def predict(self, text):
        r = self.classifier(text, self.labels)
        return r["labels"][0], r["scores"][0]
