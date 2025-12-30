import shap
from transformers import pipeline
class IntentExplainer:
    def __init__(self):
        self.model = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
        self.labels = ["greeting","goodbye","help","thanks","other"]
        self.explainer = shap.Explainer(lambda x:[self.model(t,self.labels)["scores"] for t in x], shap.maskers.Text())
    def explain(self, text):
        shap.plots.text(self.explainer([text]))
