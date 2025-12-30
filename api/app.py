from fastapi import FastAPI
from models.intent_classifier import IntentClassifier
from models.response_generator import ResponseGenerator
from memory.context_manager import ContextManager
from ethics.safety import safe_response

app = FastAPI()
intent = IntentClassifier()
responder = ResponseGenerator()
context = ContextManager()

@app.post("/chat")
def chat(message:str):
    i,c = intent.predict(message)
    ctx = context.get_context()
    r = responder.generate(message+" "+ctx)
    r = safe_response(r,c)
    context.add_turn(message,r)
    return {"intent":i,"confidence":round(c,2),"response":r}
