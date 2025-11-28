import streamlit as st
from utils import call_openrouter

# ------------------------------------------------
# Page Config
# ------------------------------------------------
st.set_page_config(
    page_title="AI Multi Writer Suite",
    layout="wide"
)

# ------------------------------------------------
# UI Styling
# ------------------------------------------------
st.markdown("""
<style>
body { font-family: 'Segoe UI', sans-serif; }
.big-title { font-size: 42px; font-weight: 700; margin-bottom: 10px; }
.sub { color: #666; margin-bottom: 30px; }
.box { padding: 20px; background: #f8f9fa; border-radius: 14px; }
button[kind="primary"] { border-radius: 10px !important; }
</style>
""", unsafe_allow_html=True)

# ------------------------------------------------
# Header
# ------------------------------------------------
st.markdown("<div class='big-title'>📝 AI Writing Studio</div>", unsafe_allow_html=True)
st.markdown("<div class='sub'>Generate blogs, news articles, and stories — powered by Grok 4.1 Fast.</div>", unsafe_allow_html=True)

st.markdown("---")

# ------------------------------------------------
# Sidebar
# ------------------------------------------------
st.sidebar.title("✍️ Tools")
tool = st.sidebar.radio(
    "Select a writing tool:",
    ["AI Blog Generator", "AI News Article Writer", "AI Story Writer"]
)

st.sidebar.markdown("---")
st.sidebar.info("Model: **x-ai/grok-4.1-fast:free**")

# ------------------------------------------------
# Tool Layout
# ------------------------------------------------
st.markdown("<div class='box'>", unsafe_allow_html=True)

if tool == "AI Blog Generator":
    st.header("📝 AI Blog Generator")
    topic = st.text_input("Enter blog topic:")
    words = st.slider("Blog Length (Words)", 200, 2000, 600)

    if st.button("Generate Blog"):
        with st.spinner("⏳ Generating blog..."):
            prompt = f"Write a detailed blog post of {words} words about: {topic}. Make it engaging, structured, and SEO friendly."
            output = call_openrouter(prompt)
        st.success("✔ Done!")
        st.write(output)

elif tool == "AI News Article Writer":
    st.header("📰 AI News Article Writer")
    event = st.text_input("Enter news event:")
    tone = st.selectbox("Tone:", ["Neutral", "Professional", "Breaking News", "Investigative"])

    if st.button("Generate News Article"):
        with st.spinner("⏳ Creating news report..."):
            prompt = f"Write a news article about: {event}. Tone: {tone}. Provide facts, quotes, and professional formatting."
            output = call_openrouter(prompt)
        st.success("✔ Done!")
        st.write(output)

elif tool == "AI Story Writer":
    st.header("📖 AI Story Writer")
    plot = st.text_area("Describe your story idea:")
    style = st.selectbox("Writing Style:", ["Fantasy", "Adventure", "Sci-Fi", "Horror", "Romantic", "Drama"])

    if st.button("Generate Story"):
        with st.spinner("⏳ Writing your story..."):
            prompt = f"Write a story in {style} style. Plot: {plot}. Make it creative, emotional, and descriptive."
            output = call_openrouter(prompt)
        st.success("✔ Done!")
        st.write(output)

st.markdown("</div>", unsafe_allow_html=True)
