"""
Task 3.2: Customer Support Assistant (Gemini version)
-------------------------------------------------------
Run this file directly in a terminal:  python support_assistant.py
It will start an interactive chat in your terminal. Type 'quit' to exit.
"""

import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

MODEL_NAME = "gemini-2.5-flash"

support_system_prompt = """
You are a customer support agent for TechShop, an electronics retailer.

Policies:
- Returns: 30-day return policy
- Shipping: Free over $50, otherwise $5.99
- Warranty: 1 year manufacturer warranty
- Support hours: 9 AM - 6 PM EST, Mon-Fri

Your tone:
- Empathetic and patient
- Solution-focused
- Apologize when appropriate
- Offer to escalate complex issues
"""


def chat(history, user_message):
    history.append({"role": "user", "parts": [{"text": user_message}]})

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=history,
        config=types.GenerateContentConfig(
            system_instruction=support_system_prompt,
            max_output_tokens=500,
            temperature=0.7,
        ),
    )

    assistant_reply = response.text
    history.append({"role": "model", "parts": [{"text": assistant_reply}]})
    return assistant_reply


def main():
    conversation_history = []
    print("TechShop Support Bot ready! Type 'quit' to exit.\n")

    # Suggested test scenarios (from the lab):
    # - 'I want to return a product I bought 2 weeks ago'
    # - 'How much is shipping?'
    # - 'My laptop stopped working after 6 months'

    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Goodbye!")
            break

        try:
            reply = chat(conversation_history, user_input)
            print(f"Support Bot: {reply}\n")
        except Exception as e:
            print(f"[Error calling Gemini API]: {e}\n")


if __name__ == "__main__":
    main()
