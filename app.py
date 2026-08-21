"""
Lab 12 — Company Knowledge Assistant (Streamlit + Gemini + ChromaDB)
Project 3, Part 4 (FINAL)

This app is the Streamlit UI for the RAG pipeline already built in
week11_semantic_search.ipynb — it reuses the EXACT same GeminiEmbeddingFunction
and query pattern as that notebook's semantic_rag() function, so it reads the
existing ./chroma_db correctly (verified against the real notebook code).
"""

import os
import streamlit as st
import chromadb
from chromadb import Documents, EmbeddingFunction, Embeddings
from google import genai
from google.genai import types as genai_types
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# ------------------------------------------------------------------
# Config — matches week11_semantic_search.ipynb exactly
# ------------------------------------------------------------------
CHROMA_PATH = "./chroma_db"
COLLECTION_NAME = "company_docs"
GEMINI_EMBED_MODEL = "gemini-embedding-001"
GEMINI_EMBED_TASK_TYPE = "RETRIEVAL_DOCUMENT"  # notebook uses this for BOTH indexing and querying
GEMINI_CHAT_MODEL = "gemini-2.5-flash"

# ------------------------------------------------------------------
# Environment
# ------------------------------------------------------------------
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# ------------------------------------------------------------------
# Page config (must be the first Streamlit call)
# ------------------------------------------------------------------
st.set_page_config(
    page_title="AI Assistant",
    page_icon="🤖",
    layout="wide",
)


# ------------------------------------------------------------------
# Custom Gemini embedding function for ChromaDB
# Identical to the class defined in week11_semantic_search.ipynb, so it
# embeds queries the exact same way the collection was built.
# ------------------------------------------------------------------
class GeminiEmbeddingFunction(EmbeddingFunction):
    """Custom ChromaDB embedding function that uses Gemini's embedding model.
    ChromaDB calls this automatically whenever you add or query documents."""

    def __init__(self, api_key, model_name=GEMINI_EMBED_MODEL, task_type=GEMINI_EMBED_TASK_TYPE):
        self.client = genai.Client(api_key=api_key)
        self.model_name = model_name
        self.task_type = task_type

    def __call__(self, input: Documents) -> Embeddings:
        result = self.client.models.embed_content(
            model=self.model_name,
            contents=list(input),
            config=genai_types.EmbedContentConfig(task_type=self.task_type),
        )
        return [e.values for e in result.embeddings]


# ------------------------------------------------------------------
# Cached resources — each of these runs only ONCE per app session
# ------------------------------------------------------------------
@st.cache_resource
def init_chromadb():
    """Connect to the existing ChromaDB collection built in Week 11."""
    chroma_client = chromadb.PersistentClient(path=CHROMA_PATH)
    gemini_ef = GeminiEmbeddingFunction(api_key=GEMINI_API_KEY)
    collection = chroma_client.get_or_create_collection(
        name=COLLECTION_NAME,
        embedding_function=gemini_ef,
        metadata={"description": "Company policy documents"},
    )
    return collection


@st.cache_resource
def init_llm():
    """Create the Gemini chat model — same LangChain wrapper used in
    week11_semantic_search.ipynb's semantic_rag() function."""
    return ChatGoogleGenerativeAI(
        model=GEMINI_CHAT_MODEL,
        google_api_key=GEMINI_API_KEY,
        temperature=0,
    )


# ------------------------------------------------------------------
# RAG logic
# ------------------------------------------------------------------
def get_rag_response(query: str, n_results: int = 3) -> str:
    """Retrieve relevant chunks from ChromaDB, then ask Gemini to answer
    using ONLY that retrieved context (classic RAG pattern)."""
    try:
        results = collection.query(query_texts=[query], n_results=n_results)

        if not results["documents"][0]:
            return "No relevant information found in the documents."

        context = "\n\n---\n\n".join(results["documents"][0])

        prompt = f"""You are a helpful HR assistant. Answer using ONLY the context
below. If the answer is not in the context, say so clearly. Be concise and friendly.

Context:
{context}

Question: {query}

Answer:"""

        response = llm.invoke(prompt)
        return response.content

    except Exception as e:
        return f"Error: {str(e)}. Please try again."


# ------------------------------------------------------------------
# App body — wrapped in try/except per the lab's error-handling task
# ------------------------------------------------------------------
try:
    if not GEMINI_API_KEY:
        st.error("GEMINI_API_KEY not found. Make sure your .env file has GEMINI_API_KEY set.")
        st.stop()

    collection = init_chromadb()
    llm = init_llm()

    # ---- Title ----
    st.title("🤖 Company Knowledge Assistant")
    st.markdown("Ask me anything about company policies!")

    # ---- Sidebar ----
    with st.sidebar:
        st.header("About")
        st.markdown(
            """
This AI assistant can answer questions about:
- Vacation policies
- Remote work guidelines
- Parental leave
- Benefits information

**Powered by:**
- Google Gemini
- ChromaDB vector search
- Semantic RAG
            """
        )
        st.divider()
        st.metric("Documents Indexed", collection.count())
        st.metric("Messages in Chat", len(st.session_state.get("messages", [])))
        st.divider()
        if st.button("Clear Chat History"):
            st.session_state.messages = []
            st.rerun()

    # ---- Session state ----
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # ---- Welcome message (only before the first user message) ----
    if len(st.session_state.messages) == 0:
        welcome = """👋 Hi! I'm your company knowledge assistant. I can help you find
information about:
- Vacation and time off policies
- Remote work guidelines
- Parental leave benefits
- And more!

Just ask me a question to get started."""
        with st.chat_message("assistant"):
            st.write(welcome)

    # ---- Display chat history ----
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # ---- Chat input ----
    if prompt := st.chat_input("Ask a question..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Searching documents..."):
                response = get_rag_response(prompt)
            st.write(response)

        st.session_state.messages.append({"role": "assistant", "content": response})

except FileNotFoundError:
    st.error(
        """Error: ChromaDB not found.
Please run the Week 11 lab first to create the vector database, and make sure
the `chroma_db` folder sits next to this app.py file."""
    )
    st.stop()
except Exception as e:
    st.error(f"Error: {str(e)}")
    st.info("Make sure your .env file has GEMINI_API_KEY set, and that the collection name matches Week 11.")
    st.stop()
