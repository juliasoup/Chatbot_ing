import json

with open("intents.json", "r", encoding="utf-8") as f:
    intents = json.load(f)

def match(text):
    text = text.lower()

    # se o usuário estiver dentro de triagem
    if "triagem" in intents:
        for cond, patterns in intents["triagem"].items():
            for p in patterns:
                if p in text:
                    return ("triagem", cond)

    # intents normais
    for intent, patterns in intents.items():
        if intent == "triagem":
            continue
        for p in patterns:
            if p in text:
                return (intent, None)

    return (None, None)
