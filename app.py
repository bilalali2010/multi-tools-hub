import streamlit as st
from pathlib import Path

# --- visual/theme ---
st.set_page_config(page_title="Multi-Tool AI Suite", layout="wide", initial_sidebar_state="expanded")
# minimal professional CSS
st.markdown(
    """
    <style>
    :root{--card-bg:#ffffff;--muted:#6b7280;--accent:#0f6fff;}
    body {background-color: #f6f7fb;}
    .card {background:var(--card-bg); border-radius:12px; padding:18px; box-shadow: 0 6px 18px rgba(22,28,37,0.06); }
    .tool-title {font-size:18px; font-weight:700; margin-bottom:6px;}
    .muted {color:var(--muted); font-size:13px;}
    .small {font-size:13px;}
    </style>
    """, unsafe_allow_html=True
)

st.sidebar.markdown("### ⚙️ Tools")
tool = st.sidebar.selectbox(
    "Select a tool",
    [
        "AI Chatbot",
        "Text Rewriter",
        "Meme Idea Generator",
        "AI Blog Generator",
        "News Article Writer",
        "Story Writer",
        "Social Media Caption Writer",
        "SEO Keyword Generator",
        "AI Email Writer"
    ],
)

# --- shared client ---
from tools.openrouter_client import call_openrouter

# helper: show generating placeholder + spinner
def generate_with_ui(prompt, timeout_text="Generating response…"):
    placeholder = st.empty()
    with st.spinner(timeout_text):
        placeholder.info(timeout_text)
        # call API (blocking) and then replace placeholder
        result = call_openrouter(prompt)
        placeholder.empty()
    return result

# layout: two columns, left for inputs, right for output
col_left, col_right = st.columns([1, 1.25])
with col_left:
    if tool == "AI Chatbot":
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="tool-title">🤖 AI Chatbot</div>', unsafe_allow_html=True)
        user_text = st.text_area("Ask anything", height=140, placeholder="Type a question or instruction...")
        tone = st.selectbox("Tone / System style", ["Helpful & Neutral", "Concise", "Detailed", "Friendly"])
        if st.button("Send"):
            system_prompt = {
                "Helpful & Neutral": "You are a helpful assistant.",
                "Concise": "Answer concisely and directly.",
                "Detailed": "Provide a thorough, well-structured answer.",
                "Friendly": "Write in a friendly and conversational tone."
            }[tone]
            prompt = f"{system_prompt}\n\nUser: {user_text}"
            output = generate_with_ui(prompt)
            st.session_state.setdefault("last_response", output)
        st.markdown('</div>', unsafe_allow_html=True)

    elif tool == "Text Rewriter":
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="tool-title">✍️ Text Rewriter</div>', unsafe_allow_html=True)
        text = st.text_area("Enter text to rewrite", height=160)
        style = st.selectbox("Rewrite style", ["Simple / Clear", "Professional", "Casual", "SEO-friendly"])
        if st.button("Rewrite Text"):
            prompt = f"Rewrite the following text in style: {style}.\n\nText:\n{text}"
            output = generate_with_ui(prompt)
            st.session_state.setdefault("last_response", output)
        st.markdown('</div>', unsafe_allow_html=True)

    elif tool == "Meme Idea Generator":
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="tool-title">🤣 Meme Idea Generator</div>', unsafe_allow_html=True)
        topic = st.text_input("Topic / image description", "e.g. remote work, exams, coding")
        tone = st.selectbox("Tone", ["Funny", "Sarcastic", "Relatable", "Wholesome"])
        amount = st.slider("Ideas (count)", 1, 10, 3)
        if st.button("Generate Meme Ideas"):
            prompt = f"Give {amount} short meme captions/ideas for topic: {topic}. Tone: {tone}. Keep each one <= 20 words."
            output = generate_with_ui(prompt)
            st.session_state.setdefault("last_response", output)
        st.markdown('</div>', unsafe_allow_html=True)

    elif tool == "AI Blog Generator":
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="tool-title">📝 AI Blog Generator</div>', unsafe_allow_html=True)
        topic = st.text_input("Blog topic / title", "Benefits of Python for beginners")
        audience = st.text_input("Target audience", "Beginners / Students (optional)")
        wc = st.slider("Target word count", 200, 2500, 800)
        seo = st.checkbox("SEO-friendly structure (headings + meta)", value=True)
        if st.button("Generate Blog"):
            seo_text = "Include SEO-friendly headings and a meta description." if seo else ""
            prompt = f"Write a detailed blog article about: {topic}.\nAudience: {audience}\nTarget words: {wc}.\n{seo_text}\nMake it well-structured with headings, intro, body, conclusion, and examples when relevant."
            output = generate_with_ui(prompt)
            st.session_state.setdefault("last_response", output)
        st.markdown('</div>', unsafe_allow_html=True)

    elif tool == "News Article Writer":
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="tool-title">📰 News Article Writer</div>', unsafe_allow_html=True)
        headline = st.text_input("Headline / Topic", "Local AI startup secures funding")
        category = st.selectbox("Category", ["Technology", "World", "Business", "Science", "Sports"])
        tone = st.selectbox("Tone", ["Neutral", "Breaking News", "Investigative"])
        length = st.selectbox("Length", ["Short (300-400)", "Standard (400-700)", "Long (700-1200)"])
        if st.button("Generate Article"):
            length_map = {"Short (300-400)": "350", "Standard (400-700)": "550", "Long (700-1200)": "900"}
            prompt = f"Write a news article.\nHeadline: {headline}\nCategory: {category}\nTone: {tone}\nLength: ~{length_map[length]} words.\nWrite in a factual, journalistic style with a lede, quotes (invented if needed), and context."
            output = generate_with_ui(prompt)
            st.session_state.setdefault("last_response", output)
        st.markdown('</div>', unsafe_allow_html=True)

    elif tool == "Story Writer":
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="tool-title">📖 Story Writer</div>', unsafe_allow_html=True)
        genre = st.selectbox("Genre", ["Fantasy", "Horror", "Sci-Fi", "Romance", "Adventure", "Drama"])
        idea = st.text_area("Story idea / prompt", "A teenager discovers a hidden library beneath the city.")
        wc = st.slider("Story length (words)", 200, 4000, 800)
        if st.button("Write Story"):
            prompt = f"Write an original {genre} short story based on: {idea}.\nTarget words: {wc}. Make it vivid, with characters, conflict, and a satisfying end."
            output = generate_with_ui(prompt)
            st.session_state.setdefault("last_response", output)
        st.markdown('</div>', unsafe_allow_html=True)

    elif tool == "Social Media Caption Writer":
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="tool-title">📱 Social Media Caption Writer</div>', unsafe_allow_html=True)
        platform = st.selectbox("Platform", ["Instagram", "TikTok", "Facebook", "X / Twitter"])
        desc = st.text_area("Describe the post (image/video) ", "A cozy coffee shop rainy window shot.")
        vibe = st.selectbox("Vibe", ["Aesthetic", "Funny", "Motivational", "Short & Catchy", "Informative"])
        count = st.slider("Number of captions", 1, 10, 5)
        if st.button("Generate Captions"):
            prompt = f"Generate {count} captions for {platform}. Vibe: {vibe}. Post description: {desc}. Keep them short and scroll-stopping."
            output = generate_with_ui(prompt)
            st.session_state.setdefault("last_response", output)
        st.markdown('</div>', unsafe_allow_html=True)

    elif tool == "SEO Keyword Generator":
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="tool-title">🔍 SEO Keyword Generator</div>', unsafe_allow_html=True)
        topic = st.text_input("Topic / Seed keyword", "ai productivity tools")
        difficulty = st.selectbox("Difficulty goal", ["Easy", "Medium", "Competitive"])
        if st.button("Generate Keywords"):
            prompt = f"Generate SEO keywords for: {topic}. Difficulty goal: {difficulty}. Return: 15 primary keywords, 15 LSI keywords, 10 long-tail phrases, and 5 blog post ideas."
            output = generate_with_ui(prompt)
            st.session_state.setdefault("last_response", output)
        st.markdown('</div>', unsafe_allow_html=True)

    elif tool == "AI Email Writer":
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="tool-title">📧 AI Email Writer</div>', unsafe_allow_html=True)
        email_type = st.selectbox("Email type", ["Formal", "Casual", "Business", "Complaint", "Apology", "Job Application"])
        subject = st.text_input("Subject line", "Request for collaboration")
        details = st.text_area("Details to include", "Introduce yourself, explain the request, offer next steps.")
        if st.button("Generate Email"):
            prompt = f"Write a {email_type.lower()} email with subject: {subject}. Include: {details}. Keep it polite and actionable."
            output = generate_with_ui(prompt)
            st.session_state.setdefault("last_response", output)
        st.markdown('</div>', unsafe_allow_html=True)

with col_right:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="tool-title">Output</div>', unsafe_allow_html=True)
    st.markdown('<div class="small muted">Model: x-ai/grok-4.1-fast:free (via OpenRouter) — API key from Streamlit Secrets</div>', unsafe_allow_html=True)
    result = st.session_state.get("last_response", "")
    if result:
        st.text_area("Generated output", value=result, height=520)
        # quick actions
        c1, c2, c3 = st.columns([1,1,1])
        with c1:
            if st.button("Copy to clipboard"):
                st.write("Select the text and copy (browser support varies).")
        with c2:
            if st.button("Clear output"):
                st.session_state["last_response"] = ""
                st.experimental_rerun()
        with c3:
            st.download_button("Download .txt", result, file_name="ai_output.txt", mime="text/plain")
    else:
        st.markdown("No output yet. Use the left panel to generate content.", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# footer
st.markdown(
    """
    <div style="padding:10px 0; text-align:center; color:var(--muted); font-size:13px;">
    Multi-Tool AI Suite · model: x-ai/grok-4.1-fast:free · keep your OPENROUTER_API_KEY in Streamlit secrets
    </div>
    """, unsafe_allow_html=True
)
