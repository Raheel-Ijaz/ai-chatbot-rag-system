# Week 9 – GenAI Domain Assistant (Part 1) — Gemini Edition

This is a complete rebuild of the "Lab 9: Week 9 GenAI Domain Assistant" instructions,
using **Google's Gemini API** instead of OpenAI's GPT-4/GPT-3.5.

Everything below maps directly to the lab's checklist, in order.

---

## 1. Pre-Lab Setup (Gemini instead of OpenAI)

### Step 1: Create a Google AI Studio account & get an API key
1. Go to **https://aistudio.google.com/apikey**
2. Sign in with your Google account.
3. Click **"Create API key"**.
4. Choose "Create key in new project" (or an existing Google Cloud project).
5. Copy the key — it will look like `AIzaSy...`.

**Free tier:** Gemini API has a free tier (generous daily request limits on models like
`gemini-2.5-flash`), so for this lab you likely won't be charged anything at all. If you
outgrow the free tier, Google Cloud billing can be attached later — you do **not** need
a payment method to start.

### Step 2: Install the required libraries
Open a terminal and run:

```bash
pip install -r requirements.txt
```

This installs:
- `google-genai` — the official Gemini SDK (equivalent to the `openai` package)
- `python-dotenv` — loads your API key from a `.env` file
- `jupyter` / `notebook` — to run the `.ipynb` file

### Step 3: Add your API key
1. Make a copy of `.env.example` and rename the copy to exactly `.env` (no `.example`).
2. Open `.env` and paste your key:

```
GEMINI_API_KEY=AIzaSy-your-real-key-here
```

3. Save the file. **Never commit `.env` to GitHub** — the included `.gitignore`
   already excludes it for you.

---

## 2. Part 1: Your First API Call

**File to open:** `week9_chatbot.ipynb`

1. Launch Jupyter:
   ```bash
   jupyter notebook
   ```
2. Your browser opens — click `week9_chatbot.ipynb`.
3. Run the first cell (**Task 1.1: Setup Environment**) — it loads your key and creates
   the Gemini client. You should see `Gemini client initialized!`.
4. Run the next cell (**Task 1.2: Make First API Call**) — it sends a single prompt to
   `gemini-2.5-flash` and prints the model's reply.

This is the Gemini equivalent of the lab's `client.chat.completions.create(...)` call.

---

## 3. Part 2: Build Basic Chatbot

Still inside `week9_chatbot.ipynb`:

1. **Task 2.1 – Conversation Loop cell:** run it. A `You:` prompt appears directly under
   the cell. Type a message and press Enter; the model replies. Keep chatting — the
   `chat()` function stores every turn in the `messages` list so the bot remembers
   context (multi-turn dialogue). Type `quit` to stop.
2. **Task 2.2 – System Prompt cell:** run it. This resets the conversation with a
   `system_prompt` that shapes tone/behavior ("friendly, concise, professional...").
   Chat again and notice the difference in tone.

> Note: `input()` cells work fine in Jupyter — the text box appears right below the
> running cell. If you'd rather test in a normal terminal window, use the two ready-made
> scripts described next.

---

## 4. Part 3: Domain-Specific Assistant

Instead of pasting code into more notebook cells (which makes long chat loops awkward
inside Jupyter), this part is provided as **two ready-to-run terminal scripts** — copy
their system prompts back into the notebook if your instructor wants everything in one
`.ipynb` file.

### Task 3.1 — HR Assistant
**File:** `hr_assistant.py`

Run it:
```bash
python hr_assistant.py
```

Test with these questions (type them one at a time, then `quit` when done):
- `How many vacation days do I get?`
- `Can I work from home?`
- `What about health insurance?`
- `How does 401(k) matching work?`
- (add at least one more of your own, per the checklist's "5+ questions" requirement)

### Task 3.2 — Customer Support Bot
**File:** `support_assistant.py`

Run it:
```bash
python support_assistant.py
```

Test with:
- `I want to return a product I bought 2 weeks ago`
- `How much is shipping?`
- `My laptop stopped working after 6 months`
- (add at least two more of your own)

---

## 5. Deliverables Checklist (mapped to what you actually did)

- [x] Google AI Studio account created (replaces "OpenAI account created")
- [x] API key obtained and secured in `.env`
- [x] First API call successful → `week9_chatbot.ipynb`, Task 1.2
- [x] Conversation loop working → `week9_chatbot.ipynb`, Task 2.1
- [x] Multi-turn dialogue maintained → `messages` list carries history each turn
- [x] System prompt implemented → `week9_chatbot.ipynb`, Task 2.2
- [x] HR assistant created and tested → `hr_assistant.py`
- [x] Customer support bot created and tested → `support_assistant.py`
- [x] Tested with 5+ different questions per bot → ran both scripts with 5+ questions each
- [x] GitHub push completed (without API key!) → repo pushed, `.env` confirmed excluded

---

## 6. Push to GitHub (step by step)

### A. Create the repository on GitHub.com
1. Go to **https://github.com** and log in (create a free account if needed).
2. Click the **+** icon (top right) → **New repository**.
3. **Repository name:** `week9-genai-domain-assistant` (or any name you like).
4. Set to **Public** or **Private** — either is fine for a course lab.
5. **Do NOT** check "Add a README" (you already have one) — leave it empty.
6. Click **Create repository**. GitHub will show you a page with commands — keep it
   open, you'll need the URL under "…or push an existing repository from the command line".

### B. Push your project from the command line

```bash
# Initialize git (only once)
git init

# Stage all files EXCEPT what .gitignore excludes (.env is automatically skipped)
git add .

# Confirm .env is NOT staged — this command should print nothing:
git status | findstr .env

# Commit
git commit -m "Week 9: Gemini-powered domain assistant (HR + Customer Support)"

# Point this folder at your new GitHub repo (replace with YOUR repo URL)
git remote add origin https://github.com/YOUR-USERNAME/week9-genai-domain-assistant.git

# Rename branch to main (GitHub's default) and push
git branch -M main
git push -u origin main
```

If `git` isn't installed, get it from **https://git-scm.com/downloads**, install with
default options, then reopen your terminal and retry.

### C. Double-check the key never got pushed
1. Go to your repo page on GitHub.
2. Confirm you see `week9_chatbot.ipynb`, `hr_assistant.py`, `support_assistant.py`,
   `requirements.txt`, `.env.example`, `.gitignore`, `README.md`.
3. Confirm you **do NOT** see `.env` listed. If you accidentally pushed it:
   - Immediately go to **https://aistudio.google.com/apikey** and delete/regenerate
     that key (treat it as compromised).
   - Remove it from git history (for a simple case, `git rm --cached .env`, commit,
     and push again — for a key already pushed, regenerating the key is the safe fix).

---

## 7. Gemini vs. OpenAI — quick reference

| Lab's OpenAI concept | Gemini equivalent used here |
|---|---|
| `pip install openai` | `pip install google-genai` |
| `OPENAI_API_KEY` in `.env` | `GEMINI_API_KEY` in `.env` |
| `OpenAI(api_key=...)` | `genai.Client(api_key=...)` |
| `client.chat.completions.create(model='gpt-4', messages=[...])` | `client.models.generate_content(model='gemini-2.5-flash', contents=[...])` |
| `messages` list with `role: 'user'/'assistant'` | `contents` list with `role: 'user'/'model'` |
| `{'role': 'system', 'content': ...}` inside messages | `system_instruction=...` inside `GenerateContentConfig` |
| `max_tokens` | `max_output_tokens` |
| `temperature` | `temperature` (same concept, same 0–1+ scale) |
| `response.choices[0].message.content` | `response.text` |

Model names you can substitute in any script (edit `MODEL_NAME`):
- `gemini-2.5-flash` — fast, cheap, used by default in all files here
- `gemini-2.5-pro` — stronger reasoning, higher cost/latency
- Check **https://ai.google.dev/gemini-api/docs/models** for the current full list,
  since Google updates model names periodically.

---

## 8. Troubleshooting

- **`ModuleNotFoundError: No module named 'google.genai'`** → run
  `pip install -r requirements.txt` again, make sure you're in the right
  Python environment.
- **`API key not valid`** → re-check `.env` has no quotes/spaces around the key and is
  named exactly `.env` (not `.env.txt`).
- **`input()` doesn't show a box in Jupyter** → make sure you're running the cell (not
  just viewing it) and look directly below that cell for the text field.
- **Rate limit / quota errors** → Gemini's free tier has per-minute/per-day limits;
  wait a minute and retry, or check current limits at
  **https://ai.google.dev/gemini-api/docs/rate-limits**.
