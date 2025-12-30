def safe_response(text, confidence):
    return text if confidence > 0.4 else "I'm not confident. Can you rephrase?"
