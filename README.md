# GenAI Course Project — Weeks 9–12

This repository tracks a multi-week Generative AI course project. Every lab uses
**Google's Gemini API** instead of OpenAI, and each week builds on the previous one
inside this single repo.

## Contents
- [Week 9 – GenAI Domain Assistant (Part 1)](#week-9--genai-domain-assistant-part-1--gemini-edition)
- [Week 10 – RAG (Retrieval Augmented Generation)](#week-10--rag-retrieval-augmented-generation--gemini-edition)
- [Week 11 – Vector Databases & Semantic Search](#week-11--vector-databases--semantic-search--gemini-edition)
- Week 12 – *(coming soon)*

---

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
3. **Repository name:** `ai-chatbot-rag-system`.
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
git remote add origin https://github.com/Raheel-Ijaz/ai-chatbot-rag-system.git

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

---
---

# Week 10 – RAG (Retrieval Augmented Generation) — Gemini Edition

This section covers Lab 10: teaching your chatbot to answer questions from your own
company documents instead of relying only on what the model already knows. Same
approach as Week 9 — every OpenAI call is replaced with Gemini.

New files added for this part:
```
company_docs/
├── hr_policy.txt
├── benefits.txt
└── it_policy.txt
week10_rag_system.ipynb
```

`requirements.txt` was also updated to include the LangChain + Gemini RAG libraries.

---

## 1. Install the new dependencies

The `requirements.txt` file already has everything from Week 9 plus the new RAG
libraries (`langchain`, `langchain-community`, `langchain-google-genai`, `pypdf`).
Just re-run:

```bash
pip install -r requirements.txt
```

This adds:
- `langchain` — the framework used to split and orchestrate document Q&A
- `langchain-core` — provides the `Document` object used to load your files
- `langchain-text-splitters` — provides `RecursiveCharacterTextSplitter`
- `langchain-google-genai` — the LangChain ↔ Gemini bridge (`ChatGoogleGenerativeAI`)
- `pypdf` — lets you extend this to read PDF files later, if you want to

Your existing `.env` file with `GEMINI_API_KEY` is reused — no new key needed.

> **Note:** the lab's original instructions use `langchain_community.document_loaders`
> (`DirectoryLoader`, `TextLoader`) to read the `.txt` files. That package has since
> been announced for sunset by the LangChain team, so this version instead loads files
> with a few lines of plain Python and wraps each one in a `langchain_core.documents.Document`
> object — same end result, but without depending on a deprecated package.

---

## 2. Sample company documents

Three sample policy files are already provided in `company_docs/`:
- `hr_policy.txt` — vacation, remote work, parental leave, sick leave, reviews
- `benefits.txt` — health insurance, 401(k), wellness stipend, professional development
- `it_policy.txt` — equipment, software access, passwords, VPN, equipment return

You can edit these freely or add more `.txt` files to the folder — the notebook loads
every `.txt` file it finds there automatically.

---

## 3. Part 1: Document Loading

**File to open:** `week10_rag_system.ipynb`

1. Launch Jupyter (same as before — via `jupyter notebook` or your `open_jupyter.bat`
   shortcut).
2. Open `week10_rag_system.ipynb`.
3. Run the **Task 1.1: Load Documents** cell — it loads all `.txt` files from
   `company_docs/` and prints how many documents were found plus a preview.
4. Run the **Task 1.2: Split into Chunks** cell — it breaks each document into ~500
   character chunks (with 50-character overlap so context isn't lost at chunk
   boundaries), and prints 3 sample chunks so you can see what they look like.

---

## 4. Part 2: Simple Retrieval

Still inside the notebook:

1. **Task 2.1 – Build Keyword Search:** run the cell defining `simple_search()`. This
   is a basic keyword-matching retriever — it scores each chunk by how many times the
   query's words appear in it, then returns the top matches. Test it with the sample
   query about vacation policy and confirm it pulls back the right chunk.
2. **Task 2.2 – Test Different Queries:** run the cell that loops through 3 test
   queries (vacation days, remote work, parental leave) and prints how many relevant
   chunks were found for each.

---

## 5. Part 3: RAG Pipeline

1. **Task 3.1 – Build RAG Function:** run the cell that initializes
   `ChatGoogleGenerativeAI` and defines `rag_query()`. This function does the full
   retrieve → generate flow: find relevant chunks, stuff them into a prompt as
   context, and ask Gemini to answer using *only* that context.
2. **Task 3.2 – Test RAG System:** run the cell testing 4 questions — 3 that are
   answerable from the docs, and one ("What is the dress code?") that deliberately
   isn't. Confirm the first 3 get accurate, specific answers and the 4th says the
   information isn't in the context.

---

## 6. Bonus: With vs. Without RAG

Run the final code cell — it asks Gemini the same vacation-policy question two ways:
directly (no context, generic answer) and through `rag_query()` (grounded in your
actual `hr_policy.txt`, correctly says 15 days). This side-by-side comparison is the
clearest demonstration of what RAG actually buys you.

---

## 7. Deliverables Checklist

- [x] Documents loaded from directory → Task 1.1
- [x] Text split into chunks (~500 chars each) → Task 1.2
- [x] Chunk preview showing 3 examples → Task 1.2 output
- [x] `simple_search()` function working → Task 2.1
- [x] Tested retrieval with 3+ queries → Task 2.2
- [x] `rag_query()` function implemented → Task 3.1
- [x] RAG system answers from documents → Task 3.2
- [x] Tested with 4+ questions → Task 3.2
- [x] Handles "not in context" correctly → Task 3.2, dress code question
- [x] Compared with vs without RAG → Bonus section
- [x] GitHub push completed → repo updated with company_docs/ and week10_rag_system.ipynb

---

## 8. Push the updated project to GitHub

Your repo already exists from Week 9, so this is just adding the new files to it —
no need to run `git init` or `git remote add` again.

```bash
git add .
git status | findstr .env
git commit -m "Week 10: RAG system with Gemini + LangChain"
git push
```

The `findstr .env` check should print nothing, same as before — confirming your API
key still isn't part of the commit.

Afterward, refresh your GitHub repo page and confirm you now see the `company_docs/`
folder (with its 3 `.txt` files) and `week10_rag_system.ipynb` alongside your Week 9
files.

---

## 9. Gemini vs. OpenAI — RAG-specific reference

| Lab's OpenAI concept | Gemini equivalent used here |
|---|---|
| `pip install langchain-openai` | `pip install langchain-google-genai` |
| `from langchain_openai import ChatOpenAI` | `from langchain_google_genai import ChatGoogleGenerativeAI` |
| `ChatOpenAI(model='gpt-3.5-turbo', temperature=0)` | `ChatGoogleGenerativeAI(model='gemini-2.5-flash', google_api_key=..., temperature=0)` |
| `llm.invoke(messages)` | Same method — `llm.invoke(...)` works identically for both |
| `response.content` | Same — `.content` works identically for both |

Document loading, chunking (`RecursiveCharacterTextSplitter`), and the keyword-search
retrieval logic are all pure LangChain / Python — they don't touch OpenAI or Gemini at
all, so that code is completely unchanged from the original lab.

---

## 10. Troubleshooting (RAG-specific)

- **`ModuleNotFoundError: No module named 'langchain_google_genai'`** → run
  `pip install -r requirements.txt` again.
- **`Loaded 0 documents`** → confirm `company_docs/` sits in the same folder as
  `week10_rag_system.ipynb`, and that the `.txt` files are directly inside it (not in
  a further subfolder).
- **RAG gives a vague or wrong answer** → try lowering `top_k` in `simple_search()` if
  irrelevant chunks are diluting the context, or check that your query shares actual
  keywords with the document text (keyword search only matches literal words — this
  is exactly the limitation that next week's semantic/embedding-based search fixes).
- **`API key not valid`** → same fix as Week 9 — double-check `.env` has
  `GEMINI_API_KEY=...` with no quotes or extra spaces.

---
---

# Week 11 – Vector Databases & Semantic Search — Gemini Edition

This section covers Lab 11: upgrading from exact keyword matching to **semantic
search** — where the system understands that "PTO" means the same thing as
"vacation," even though the words are completely different. Same approach as
before — OpenAI is swapped for Gemini throughout.

New files added for this part:
```
week11_semantic_search.ipynb
chroma_db/          (created automatically the first time you run the notebook)
```

`requirements.txt` was updated to include `chromadb` and `numpy`.

---

## 1. Install the new dependencies

```bash
pip install -r requirements.txt
```

This adds:
- `chromadb` — the vector database that stores embeddings and performs semantic
  similarity search
- `numpy` — used for the manual cosine similarity calculation in Part 1

Your existing `.env` file with `GEMINI_API_KEY` is reused — no new key needed. You
also need the `company_docs/` folder from Week 10 to already exist in this same
project folder (it should, if you completed Week 10).

---

## 2. Part 1: Embeddings

**File to open:** `week11_semantic_search.ipynb`

1. Run the **Task 1.1: Generate Embeddings** cell — it defines `get_embedding()`,
   which calls Gemini's `gemini-embedding-001` model and converts text into a list of
   numbers (a vector). Test it with `'vacation policy'` and confirm you get a long list
   of numbers back (3072 of them) plus a preview of the first 5.
2. Run the **Task 1.2: Calculate Similarity** cell — it defines `cosine_similarity()`,
   a standard formula for measuring how close two vectors are in meaning (1.0 =
   identical meaning, 0 = unrelated). It then compares `"vacation policy"` against 3
   other phrases and prints similarity scores.

**What to expect:** `"time off rules"` and `"PTO guidelines"` should score high
(roughly 0.85–0.95) since they mean the same thing as vacation. `"dress code
requirements"` should score low (roughly 0.1–0.3) since it's about something
unrelated. This is the entire point of embeddings — they capture *meaning*, not just
literal words.

---

## 3. Part 2: ChromaDB Setup

1. **Task 2.1 – Initialize ChromaDB:** run the cell. It creates a `GeminiEmbeddingFunction`
   class (a small adapter so ChromaDB knows how to turn your text into Gemini
   embeddings automatically), a persistent ChromaDB client that saves to a local
   `./chroma_db` folder, and a collection named `company_docs`. You should see
   `Count: 0` the first time you run it, since nothing's been added yet.
2. **Task 2.2 – Load and Index Documents:** run the cell. It loads the same 3 policy
   files from `company_docs/`, splits them into ~500-character chunks (identical
   logic to Week 10), and adds each chunk to ChromaDB. Behind the scenes, ChromaDB
   calls your `GeminiEmbeddingFunction` to convert every chunk into a vector before
   storing it. This step can take 30–60 seconds. Re-running this cell later won't
   duplicate anything — it checks `collection.count() == 0` first.

---

## 4. Part 3: Semantic RAG

1. **Task 3.1 – Test Vector Search:** run the cell defining `vector_search()`. Test it
   with 3 queries that deliberately use *different words* than the documents:
   `"time off policy"` (docs say "vacation"), `"WFH guidelines"` (docs say "remote
   work"), and `"maternity leave"` (docs say "parental leave"). Confirm each one still
   correctly finds the relevant chunk despite the word mismatch — this is semantic
   search working as intended.
2. **Task 3.2 – Build Semantic RAG Pipeline:** run the cell defining `semantic_rag()`,
   which combines vector search with `ChatGoogleGenerativeAI` (Gemini) to generate a
   full answer. Test it with 3 questions and confirm the answers are accurate and
   specific to your documents.

---

## 5. Bonus: Keyword vs. Semantic Comparison

Run the final code cell — it searches for `"PTO policy"` two ways: the old keyword
search from Week 10 (finds **0 results**, since the literal word "PTO" never appears
anywhere in your documents) and semantic search (still finds the vacation policy
chunk, since it understands PTO and vacation mean the same thing). This side-by-side
is the clearest demonstration of why semantic search is a real upgrade, not just a
fancier way of doing the same thing.

---

## 6. Deliverables Checklist

- [x] `get_embedding()` function working
- [x] `cosine_similarity()` function implemented
- [x] Similarity scores calculated for test phrases
- [x] ChromaDB client initialized
- [x] Documents indexed with embeddings
- [x] `vector_search()` function working
- [x] Semantic search finds synonyms correctly
- [x] `semantic_rag()` pipeline implemented
- [x] Tested with 3+ questions
- [x] Comparison: keyword vs semantic completed
- [x] GitHub push completed

---

## 7. Push the updated project to GitHub

```bash
git add .
git status | findstr .env
git commit -m "Week 11: Semantic search with Gemini embeddings + ChromaDB"
git push
```

The `findstr .env` check should print nothing, same as every previous week —
confirming your API key still isn't part of the commit. Note: the `chroma_db/` folder
that gets created locally contains your indexed vector database — it's fine to push
it (there's nothing secret in it), but if you'd rather keep the repo lighter, you can
add `chroma_db/` to your `.gitignore` instead and let each person regenerate it
locally by re-running Task 2.2.

---

## 8. Gemini vs. OpenAI — semantic search reference

| Lab's OpenAI concept | Gemini equivalent used here |
|---|---|
| `client.embeddings.create(model='text-embedding-ada-002', input=text)` | `client.models.embed_content(model='gemini-embedding-001', contents=text, config=...)` |
| `response.data[0].embedding` | `result.embeddings[0].values` |
| `embedding_functions.OpenAIEmbeddingFunction(...)` | Custom `GeminiEmbeddingFunction` class (defined in the notebook) |
| `from langchain_openai import ChatOpenAI` | `from langchain_google_genai import ChatGoogleGenerativeAI` |
| Embedding vector length: 1536 | Embedding vector length: 3072 |

`chromadb`, `cosine_similarity()`, and the overall retrieve → generate pipeline
structure are unchanged — only the embedding model and chat model providers differ.

---

## 9. Troubleshooting (Semantic search-specific)

- **`ModuleNotFoundError: No module named 'chromadb'`** → run
  `pip install -r requirements.txt` again.
- **Very slow on Task 2.2** → this is normal the first time (generating embeddings for
  every chunk takes real API calls); it should be fast on every subsequent run since
  the collection is already populated.
- **`Collection already has N documents` but you changed your `.txt` files** →
  ChromaDB doesn't auto-update existing chunks. Delete the `chroma_db/` folder
  entirely and re-run Task 2.1 and 2.2 to rebuild the index from scratch.
- **Similarity scores look reversed or all similar** → double check you're not
  accidentally comparing an embedding to itself, and confirm `get_embedding()` is
  actually being called fresh for each phrase (not reusing a cached value).
- **`API key not valid`** → same fix as previous weeks — double-check `.env` has
  `GEMINI_API_KEY=...` with no quotes or extra spaces.
