import streamlit as st
from utils import call_openrouter

# ---------------- Page Config ----------------
st.set_page_config(page_title="AI Multi-Tool Suite", layout="wide")

# ---------------- CSS ----------------
st.markdown("""
<style>
.title { font-size:38px; font-weight:700; }
.sub { color:#666; margin-bottom:20px; }
.block {
    padding:20px;
    background:#fafafa;
    border-radius:12px;
    border:1px solid #eee;
}
</style>
""", unsafe_allow_html=True)

# ---------------- Header ----------------
st.markdown("<div class='title'>🛠 AI Multi-Tool Suite</div>", unsafe_allow_html=True)
st.markdown("<div class='sub'>Simple. Clean. Powerful.</div>", unsafe_allow_html=True)

# ---------------- Tool Selector (TOP) ----------------
tool = st.selectbox(
    "Select a tool",
    [
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
)

st.markdown("---")

# ---------------- Helper ----------------
def generate(prompt):
    with st.spinner("Generating..."):
        return call_openrouter(prompt)

# ---------------- Main Block ----------------
st.markdown("<div class='block'>", unsafe_allow_html=True)

# ---------- AI Chatbot ----------
if tool == "AI Chatbot":
    st.header("🤖 AI Chatbot")
    q = st.text_area("Ask anything", height=140)
    if st.button("Send"):
        st.text_area("Response", generate(q), height=300)

# ---------- Logo Prompt ----------
elif tool == "Logo Prompt Generator":
    st.header("📝 Logo Prompt Generator")
    brand = st.text_input("Brand Name")
    niche = st.text_input("Brand Niche")
    if st.button("Generate"):
        p = f"Create one professional logo prompt for {brand} in {niche} niche."
        st.text_area("Result", generate(p), height=200)

# ---------- Text Rewriter ----------
elif tool == "Text Rewriter":
    st.header("✍️ Text Rewriter")
    txt = st.text_area("Text", height=150)
    style = st.selectbox("Style", ["Simple", "Professional", "Casual", "SEO"])
    if st.button("Rewrite"):
        st.text_area("Rewritten", generate(f"Rewrite in {style} style:\n{txt}"), height=300)

# ---------- Meme Generator ----------
elif tool == "Meme Idea Generator":
    st.header("🤣 Meme Idea Generator")
    topic = st.text_input("Topic")
    if st.button("Generate"):
        st.text_area("Ideas", generate(f"Give 5 meme ideas about {topic}"), height=250)

# ---------- Blog ----------
elif tool == "AI Blog Generator":
    st.header("📝 Blog Generator")
    topic = st.text_input("Topic")
    if st.button("Generate Blog"):
        st.text_area("Blog", generate(f"Write a blog with headings on {topic}"), height=400)

# ---------- News ----------
elif tool == "News Article Writer":
    st.header("📰 News Article Writer")
    headline = st.text_input("Headline")
    if st.button("Generate"):
        st.text_area("Article", generate(f"Write a news article on {headline}"), height=400)

# ---------- Story ----------
elif tool == "Story Writer":
    st.header("📖 Story Writer")
    idea = st.text_area("Story idea")
    if st.button("Generate Story"):
        st.text_area("Story", generate(f"Write a creative story: {idea}"), height=400)

# ---------- Caption ----------
elif tool == "Social Media Caption Writer":
    st.header("📱 Caption Writer")
    desc = st.text_area("Post description")
    if st.button("Generate"):
        st.text_area("Captions", generate(f"Generate captions for {desc}"), height=300)

# ---------- SEO ----------
elif tool == "SEO Keyword Generator":
    st.header("🔍 SEO Keyword Generator")
    topic = st.text_input("Topic")
    if st.button("Generate"):
        st.text_area("Keywords", generate(f"Generate SEO keywords for {topic}"), height=300)

# ---------- Email ----------
elif tool == "AI Email Writer":
    st.header("📧 AI Email Writer")
    purpose = st.text_input("Email purpose")
    if st.button("Generate"):
        st.text_area("Email", generate(f"Write a professional email about {purpose}"), height=300)

st.markdown("</div>", unsafe_allow_html=True)
