from services.ai_client import generate_response
from services.memory_store import get_messages, add_message

SYSTEM_PROMPT = """
You are a professional sales assistant for an electronics store.

Your behavior:
- Be friendly and consultative
- Understand the customer's needs before suggesting products
- Recommend only products from the store
- Highlight benefits clearly
- Guide the conversation toward a purchase
- Never say you are an AI
"""

def handleAI(message):
    messages = get_messages()

    if not messages:
        messages.append({"role": "system", "content": SYSTEM_PROMPT})

    messages.append({"role": "user", "content": message})

    reply = generate_response(messages)

    messages.append({"role": "assistant", "content": reply})

    add_message(messages)

    return reply
