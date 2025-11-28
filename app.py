import streamlit as st
from utils import call_openrouter

# ------------------------- Page Config -------------------------
st.set_page_config(page_title="AI Multi-Tool Suite", layout="wide")

# ------------------------- CSS Styling -------------------------
st.markdown("""
<style>
body { font-family: 'Segoe UI', sans-serif; }
.big-title { font-size: 40px; font-weight: 700; margin-bottom: 5px; }
.sub { color: #555; margin-bottom: 20px; }
.card { padding: 18px; background: #f8f9fa; border-radius: 12px; box-shadow: 0 5px 15px rgba(0,0,0,0.05); margin-bottom: 15px; }
.small { font-size: 13px; color: #777; }
</style>
""", unsafe_allow_html=True)

# ------------------------- Header -------------------------
st.markdown("<div class='big-title'>🛠 AI Multi-Tool Suite</div>", unsafe_allow_html=True)
st.markdown("<div class='sub'>Generate blogs, news, stories, memes, captions, SEO keywords, emails, and more — all powered by Grok 4.1 Fast.</div>", unsafe_allow_html=True)
st.markdown("---")

# ------------------------- Sidebar -------------------------
st.sidebar.title("⚙️ Tools")
tool = st.sidebar.radio(
    "Select a tool:",
    [
        "Logo Prompt Generator",
        "AI Chatbot",
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

st.sidebar.info("Model: x-ai/grok-4.1-fast:free (via OpenRouter)")

# ------------------------- Helper Function -------------------------
def generate_with_spinner(prompt, message="⏳ Generating response..."):
    placeholder = st.empty()
    with st.spinner(message):
        placeholder.info(message)
        output = call_openrouter(prompt)
        placeholder.empty()
    return output

# ------------------------- Tool Inputs -------------------------
st.markdown("<div class='card'>", unsafe_allow_html=True)

if tool == "Logo Prompt Generator":
    st.header("📝 Logo Prompt Generator")
    brand = st.text_input("Brand Name:")
    niche = st.text_input("Brand Niche:")
    if st.button("Generate Prompt"):
        prompt = f"Generate a professional logo idea prompt for a brand named {brand} in the niche {niche}. Provide one high-quality prompt only."
        output = generate_with_spinner(prompt)
        st.text_area("Generated Logo Prompt", value=output, height=200)

elif tool == "AI Chatbot":
    st.header("🤖 AI Chatbot")
    user_text = st.text_area("Ask anything:", height=140)
    tone = st.selectbox("Response Style:", ["Helpful & Neutral", "Concise", "Detailed", "Friendly"])
    if st.button("Send"):
        style_prefix = {
            "Helpful & Neutral": "You are a helpful assistant.",
            "Concise": "Answer concisely and directly.",
            "Detailed": "Provide a detailed and thorough answer.",
            "Friendly": "Answer in a friendly and conversational tone."
        }[tone]
        prompt = f"{style_prefix}\n\nUser: {user_text}"
        output = generate_with_spinner(prompt)
        st.text_area("AI Response", value=output, height=300)

elif tool == "Text Rewriter":
    st.header("✍️ Text Rewriter")
    text = st.text_area("Enter text to rewrite:", height=160)
    style = st.selectbox("Rewrite Style:", ["Simple / Clear", "Professional", "Casual", "SEO-friendly"])
    if st.button("Rewrite"):
        prompt = f"Rewrite the following text in style: {style}.\n\n{text}"
        output = generate_with_spinner(prompt)
        st.text_area("Rewritten Text", value=output, height=300)

elif tool == "Meme Idea Generator":
    st.header("🤣 Meme Idea Generator")
    topic = st.text_input("Topic / image description", "e.g. coding, exams, remote work")
    tone = st.selectbox("Tone", ["Funny", "Sarcastic", "Relatable", "Wholesome"])
    count = st.slider("Number of ideas", 1, 10, 3)
    if st.button("Generate Meme Ideas"):
        prompt = f"Give {count} short meme captions/ideas for topic: {topic}. Tone: {tone}. Keep each <= 20 words."
        output = generate_with_spinner(prompt)
        st.text_area("Generated Meme Ideas", value=output, height=300)

elif tool == "AI Blog Generator":
    st.header("📝 AI Blog Generator")
    topic = st.text_input("Blog Topic:", "Benefits of Python")
    audience = st.text_input("Target Audience (optional):", "")
    wc = st.slider("Word Count:", 200, 2500, 600)
    seo = st.checkbox("SEO-friendly headings/meta", value=True)
    if st.button("Generate Blog"):
        seo_text = "Include SEO-friendly headings and a meta description." if seo else ""
        prompt = f"Write a detailed blog article about: {topic}.\nAudience: {audience}\nWord count: {wc}.\n{seo_text}\nInclude headings, intro, body, conclusion, and examples."
        output = generate_with_spinner(prompt)
        st.text_area("Generated Blog", value=output, height=400)

elif tool == "News Article Writer":
    st.header("📰 News Article Writer")
    headline = st.text_input("Headline:", "AI startup raises funding")
    category = st.selectbox("Category:", ["Technology", "World", "Business", "Science", "Sports"])
    tone = st.selectbox("Tone:", ["Neutral", "Breaking News", "Investigative"])
    length = st.selectbox("Length:", ["Short (300-400)", "Standard (400-700)", "Long (700-1200)"])
    if st.button("Generate Article"):
        length_map = {"Short (300-400)": 350, "Standard (400-700)": 550, "Long (700-1200)": 900}
        prompt = f"Write a news article.\nHeadline: {headline}\nCategory: {category}\nTone: {tone}\nLength: ~{length_map[length]} words.\nInclude lede, quotes, context, and closing paragraph."
        output = generate_with_spinner(prompt)
        st.text_area("Generated News Article", value=output, height=400)

elif tool == "Story Writer":
    st.header("📖 Story Writer")
    plot = st.text_area("Story Idea:", "A teenager discovers a hidden library beneath the city.")
    genre = st.selectbox("Genre:", ["Fantasy", "Adventure", "Sci-Fi", "Horror", "Romance", "Drama"])
    wc = st.slider("Story length (words):", 200, 4000, 800)
    if st.button("Generate Story"):
        prompt = f"Write a story in {genre} style based on: {plot}. Word count: {wc}. Make it creative, emotional, with characters and a satisfying ending."
        output = generate_with_spinner(prompt)
        st.text_area("Generated Story", value=output, height=400)

elif tool == "Social Media Caption Writer":
    st.header("📱 Social Media Caption Writer")
    platform = st.selectbox("Platform:", ["Instagram", "TikTok", "Facebook", "X / Twitter"])
    desc = st.text_area("Content Description:", "A cozy coffee shop on a rainy day.")
    vibe = st.selectbox("Vibe:", ["Aesthetic", "Funny", "Motivational", "Short & Catchy", "Informative"])
    count = st.slider("Number of captions:", 1, 10, 5)
    if st.button("Generate Captions"):
        prompt = f"Generate {count} captions for {platform}. Vibe: {vibe}. Content: {desc}. Keep short, catchy, and scroll-stopping."
        output = generate_with_spinner(prompt)
        st.text_area("Generated Captions", value=output, height=300)

elif tool == "SEO Keyword Generator":
    st.header("🔍 SEO Keyword Generator")
    topic = st.text_input("Topic / Seed Keyword:", "AI productivity tools")
    difficulty = st.selectbox("Difficulty:", ["Easy", "Medium", "Hard"])
    if st.button("Generate Keywords"):
        prompt = f"Generate SEO keywords for: {topic}. Difficulty: {difficulty}. Return 15 primary, 15 LSI, 10 long-tail, and 5 blog post ideas."
        output = generate_with_spinner(prompt)
        st.text_area("Generated Keywords", value=output, height=300)

elif tool == "AI Email Writer":
    st.header("📧 AI Email Writer")
    email_type = st.selectbox("Email Type:", ["Formal", "Casual", "Business", "Complaint", "Apology", "Job Application"])
    subject = st.text_input("Subject Line:", "Request for Collaboration")
    details = st.text_area("Email Details:", "Introduce yourself, explain the request, offer next steps.")
    if st.button("Generate Email"):
        prompt = f"Write a {email_type.lower()} email. Subject: {subject}. Include: {details}. Polite, actionable, and professional."
        output = generate_with_spinner(prompt)
        st.text_area("Generated Email", value=output, height=300)

st.markdown("</div>", unsafe_allow_html=True)
