import streamlit as st
from utils import call_openrouter

# ------------------------- Page Config -------------------------
st.set_page_config(page_title="AI Multi-Tool Suite", layout="wide")

# ------------------------- Session State -------------------------
if "tool" not in st.session_state:
    st.session_state.tool = "AI Chatbot"

# ------------------------- CSS -------------------------
st.markdown("""
<style>
.big-title { font-size: 40px; font-weight: 700; }
.sub { color: #555; margin-bottom: 20px; }
.card {
    padding: 18px;
    background: #f8f9fa;
    border-radius: 14px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.06);
    margin-bottom: 20px;
}
.tool-btn {
    width: 100%;
    padding: 14px;
    border-radius: 12px;
    border: none;
    background: #ffffff;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    font-size: 15px;
    cursor: pointer;
}
.tool-btn:hover {
    background: #eef2ff;
}
</style>
""", unsafe_allow_html=True)

# ------------------------- Header -------------------------
st.markdown("<div class='big-title'>🛠 AI Multi-Tool Suite</div>", unsafe_allow_html=True)
st.markdown("<div class='sub'>All-in-one AI tools powered by OpenRouter</div>", unsafe_allow_html=True)

# ------------------------- TOOL CARDS -------------------------
st.markdown("### 🔧 Choose a Tool")

tools = [
    "AI Chatbot",
    "Logo Prompt Generator",
    "Text Rewriter",
    "Meme Idea Generator",
    "AI Blog Generator",
    "News Article Writer",
    "Story Writer",
    "Social Media Caption Writer",
    "SEO Keyword Generator",
    "AI Email Writer"
]

cols = st.columns(5)
for i, tool_name in enumerate(tools):
    with cols[i % 5]:
        if st.button(tool_name, use_container_width=True):
            st.session_state.tool = tool_name

st.markdown("---")

tool = st.session_state.tool

# ------------------------- Sidebar (Info only) -------------------------
st.sidebar.info("Model: arcee-ai/trinity-mini\nvia OpenRouter")

# ------------------------- Helper -------------------------
def generate_with_spinner(prompt):
    with st.spinner("⏳ Generating..."):
        return call_openrouter(prompt)

# ------------------------- Tool Output Card -------------------------
st.markdown("<div class='card'>", unsafe_allow_html=True)

# -------- AI Chatbot --------
if tool == "AI Chatbot":
    st.header("🤖 AI Chatbot")
    q = st.text_area("Ask anything", height=150)
    if st.button("Send"):
        out = generate_with_spinner(q)
        st.text_area("Response", out, height=300)

# -------- Logo Prompt Generator --------
elif tool == "Logo Prompt Generator":
    st.header("📝 Logo Prompt Generator")
    brand = st.text_input("Brand Name")
    niche = st.text_input("Brand Niche")
    if st.button("Generate"):
        p = f"Create one professional logo prompt for {brand} in {niche} niche."
        out = generate_with_spinner(p)
        st.text_area("Result", out, height=200)

# -------- Text Rewriter --------
elif tool == "Text Rewriter":
    st.header("✍️ Text Rewriter")
    txt = st.text_area("Text", height=160)
    style = st.selectbox("Style", ["Simple", "Professional", "Casual", "SEO"])
    if st.button("Rewrite"):
        out = generate_with_spinner(f"Rewrite in {style} style:\n{txt}")
        st.text_area("Rewritten", out, height=300)

# -------- Meme Generator --------
elif tool == "Meme Idea Generator":
    st.header("🤣 Meme Generator")
    topic = st.text_input("Topic")
    if st.button("Generate"):
        out = generate_with_spinner(f"Give 5 funny meme ideas on {topic}")
        st.text_area("Memes", out, height=300)

# -------- Blog Generator --------
elif tool == "AI Blog Generator":
    st.header("📝 Blog Generator")
    topic = st.text_input("Topic")
    if st.button("Generate Blog"):
        out = generate_with_spinner(f"Write a blog on {topic} with headings.")
        st.text_area("Blog", out, height=400)

# -------- News Writer --------
elif tool == "News Article Writer":
    st.header("📰 News Writer")
    headline = st.text_input("Headline")
    if st.button("Generate"):
        out = generate_with_spinner(f"Write a news article on: {headline}")
        st.text_area("Article", out, height=400)

# -------- Story Writer --------
elif tool == "Story Writer":
    st.header("📖 Story Writer")
    idea = st.text_area("Story Idea")
    if st.button("Generate Story"):
        out = generate_with_spinner(f"Write a creative story: {idea}")
        st.text_area("Story", out, height=400)

# -------- Caption Writer --------
elif tool == "Social Media Caption Writer":
    st.header("📱 Caption Writer")
    desc = st.text_area("Post description")
    if st.button("Generate"):
        out = generate_with_spinner(f"Generate 5 captions for: {desc}")
        st.text_area("Captions", out, height=300)

# -------- SEO Keyword Generator --------
elif tool == "SEO Keyword Generator":
    st.header("🔍 SEO Keywords")
    topic = st.text_input("Topic")
    if st.button("Generate"):
        out = generate_with_spinner(f"Generate SEO keywords for {topic}")
        st.text_area("Keywords", out, height=300)

# -------- Email Writer --------
elif tool == "AI Email Writer":
    st.header("📧 Email Writer")
    purpose = st.text_input("Purpose")
    if st.button("Generate"):
        out = generate_with_spinner(f"Write a professional email about {purpose}")
        st.text_area("Email", out, height=300)

st.markdown("</div>", unsafe_allow_html=True)
