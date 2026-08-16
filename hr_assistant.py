"""
Task 3.1: HR Assistant (Gemini version)
----------------------------------------
Run this file directly in a terminal:  python hr_assistant.py
It will start an interactive chat in your terminal. Type 'quit' to exit.
"""

import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

# 1. Load the GEMINI_API_KEY from your .env file
load_dotenv()

# 2. Create the Gemini client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# 3. Model to use (fast + cheap, good for a lab/demo)
MODEL_NAME = "gemini-2.5-flash"

# 4. System prompt -> defines the assistant's personality + company policy knowledge
hr_system_prompt = """
You are an HR assistant for a technology company.

Company policies:
- Vacation: 15 days per year
- Sick leave: Unlimited (with manager approval)
- Remote work: 3 days per week
- Health insurance: Fully covered
- 401(k) matching: Up to 5%

Your role:
1. Answer employee questions about policies
2. Be friendly and supportive
3. If unsure, suggest contacting the HR department
4. Keep responses concise (2-3 sentences)
"""


def chat(history, user_message):
    """
    Sends the full conversation history + new user message to Gemini
    and returns the assistant's reply as plain text.
    """
    # Gemini keeps conversation turns as a list of {role, parts} dicts.
    history.append({"role": "user", "parts": [{"text": user_message}]})

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=history,
        config=types.GenerateContentConfig(
            system_instruction=hr_system_prompt,
            max_output_tokens=500,
            temperature=0.7,
        ),
    )

    assistant_reply = response.text
    history.append({"role": "model", "parts": [{"text": assistant_reply}]})
    return assistant_reply


def main():
    conversation_history = []  # holds the full back-and-forth
    print("HR Assistant ready! Type 'quit' to exit.\n")

    # Suggested test questions (from the lab):
    # - 'How many vacation days do I get?'
    # - 'Can I work from home?'
    # - 'What about health insurance?'
    # - 'How does 401(k) matching work?'

    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Goodbye!")
            break

        try:
            reply = chat(conversation_history, user_input)
            print(f"HR Assistant: {reply}\n")
        except Exception as e:
            print(f"[Error calling Gemini API]: {e}\n")


if __name__ == "__main__":
    main()
