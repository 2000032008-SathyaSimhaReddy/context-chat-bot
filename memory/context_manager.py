import math, time
class ContextManager:
    def __init__(self, max_turns=6, decay_lambda=0.6):
        self.max_turns = max_turns
        self.decay_lambda = decay_lambda
        self.history = []
    def add_turn(self, user, bot):
        self.history.append({"user": user, "bot": bot, "time": time.time()})
        if len(self.history) > self.max_turns:
            self.history.pop(0)
    def get_context(self):
        ctx = []
        for i, h in enumerate(self.history):
            w = math.exp(-self.decay_lambda * (len(self.history)-i))
            ctx.append(f"[w={round(w,2)}] User:{h['user']} Bot:{h['bot']}")
        return " ".join(ctx)
