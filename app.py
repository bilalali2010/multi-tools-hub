import streamlit as st
from utils import call_openrouter

# ---------------- Page Config ----------------
st.set_page_config(page_title="AI Multi-Tool Suite", layout="wide")

# ---------------- CSS ----------------
st.markdown("""
<style>
.title {
    font-size:40px;
    font-weight:700;
    background: linear-gradient(90deg,#6366f1,#22c55e);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.sub { color:#555; margin-bottom:20px; }

.box {
    padding:22px;
    background:#ffffff;
    border-radius:14px;
    border:1px solid #e5e7eb;
    box-shadow: 0 8px 24px rgba(0,0,0,0.05);
}

.label {
    font-weight:600;
    color:#374151;
}

hr {
    margin-top:20px;
    margin-bottom:20px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- Header ----------------
st.markdown("<div class='title'>✨ AI Multi-Tool Suite</div>", unsafe_allow_html=True)
st.markdown("<div class='sub'>Smart tools for writing, content & creativity</div>", unsafe_allow_html=True)

# ---------------- Tool Selector ----------------
tool = st.selectbox(
    "🧰 Choose a Tool",
    [
        "🤖 AI Chatbot",
        "🎨 Logo Prompt Generator",
        "✍️ Text Rewriter",
        "🤣 Meme Idea Generator",
        "📝 AI Blog Generator",
        "📰 News Article Writer",
        "📖 Story Writer",
        "📱 Social Media Caption Writer",
        "🔍 SEO Keyword Generator",
        "📧 AI Email Writer"
    ]
)

st.markdown("<hr>", unsafe_allow_html=True)

# ---------------- Helper ----------------
def generate(prompt):
    with st.spinner("✨ Working on it..."):
        return call_openrouter(prompt)

# ---------------- Content Box ----------------
st.markdown("<div class='box'>", unsafe_allow_html=True)

# ---------- AI Chatbot ----------
if tool.startswith("🤖"):
    st.header("🤖 AI Chatbot")
    q = st.text_area("💬 Ask anything", height=140)
    if st.button("🚀 Send"):
        st.text_area("📌 Response", generate(q), height=300)

# ---------- Logo Prompt ----------
elif tool.startswith("🎨"):
    st.header("🎨 Logo Prompt Generator")
    brand = st.text_input("🏷 Brand Name")
    niche = st.text_input("🎯 Brand Niche")
    if st.button("✨ Generate Prompt"):
        p = f"Create one professional logo prompt for {brand} in {niche} niche."
        st.text_area("🧠 Result", generate(p), height=220)

# ---------- Text Rewriter ----------
elif tool.startswith("✍️"):
    st.header("✍️ Text Rewriter")
    txt = st.text_area("📄 Original Text", height=160)
    style = st.selectbox("🎨 Rewrite Style", ["Simple", "Professional", "Casual", "SEO"])
    if st.button("♻️ Rewrite"):
        st.text_area("✅ Rewritten Text", generate(f"Rewrite in {style} style:\n{txt}"), height=300)

# ---------- Meme Generator ----------
elif tool.startswith("🤣"):
    st.header("🤣 Meme Idea Generator")
    topic = st.text_input("🔥 Topic")
    if st.button("😂 Generate Ideas"):
        st.text_area("💡 Meme Ideas", generate(f"Give 5 meme ideas about {topic}"), height=260)

# ---------- Blog ----------
elif tool.startswith("📝"):
    st.header("📝 AI Blog Generator")
    topic = st.text_input("🧠 Blog Topic")
    if st.button("✍️ Generate Blog"):
        st.text_area("📘 Blog Content", generate(f"Write a blog with headings on {topic}"), height=420)

# ---------- News ----------
elif tool.startswith("📰"):
    st.header("📰 News Article Writer")
    headline = st.text_input("🗞 Headline")
    if st.button("🖊 Write Article"):
        st.text_area("📄 Article", generate(f"Write a news article on {headline}"), height=420)

# ---------- Story ----------
elif tool.startswith("📖"):
    st.header("📖 Story Writer")
    idea = st.text_area("🌱 Story Idea")
    if st.button("✨ Generate Story"):
        st.text_area("📚 Story", generate(f"Write a creative story: {idea}"), height=420)

# ---------- Caption ----------
elif tool.startswith("📱"):
    st.header("📱 Social Media Caption Writer")
    desc = st.text_area("📸 Post Description")
    if st.button("🚀 Generate Captions"):
        st.text_area("💬 Captions", generate(f"Generate captions for {desc}"), height=300)

# ---------- SEO ----------
elif tool.startswith("🔍"):
    st.header("🔍 SEO Keyword Generator")
    topic = st.text_input("🌐 Topic")
    if st.button("📊 Generate Keywords"):
        st.text_area("📌 Keywords", generate(f"Generate SEO keywords for {topic}"), height=300)

# ---------- Email ----------
elif tool.startswith("📧"):
    st.header("📧 AI Email Writer")
    purpose = st.text_input("📬 Email Purpose")
    if st.button("✉️ Generate Email"):
        st.text_area("📝 Email Draft", generate(f"Write a professional email about {purpose}"), height=320)

st.markdown("</div>", unsafe_allow_html=True)
