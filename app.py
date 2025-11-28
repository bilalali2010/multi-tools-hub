import streamlit as st
import requests
import json
import os

st.set_page_config(page_title="Multi-Tool AI Web App", layout="wide")
st.title("🔥 Multi-Tool AI Web App (Free Grok Model)")

# Load API key from Streamlit secrets
API_KEY = st.secrets["OPENROUTER_API_KEY"]

# Central function to call OpenRouter Grok model
def call_grok(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    data = {"model": "x-ai/grok-4.1-fast:free", "messages":[{"role":"user","content":prompt}]}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    try:
        return response.json()["choices"][0]["message"]["content"]
    except:
        return "Error: Could not get response from OpenRouter."

# ----------------- Sidebar -----------------
tool = st.sidebar.selectbox("Select a tool", [
    "AI Logo Generator",
    "Logo Prompt Generator",
    "AI Chatbot",
    "Text Rewriter",
    "Meme Idea Generator",
    "AI Blog Generator",
    "News Article Writer",
    "Story Writer",
    "YouTube Script Generator",
    "Social Media Caption Writer",
    "SEO Keyword Generator",
    "AI Email Writer"
])

# ----------------- Tools -----------------

# 1. AI Logo Generator
if tool == "AI Logo Generator":
    st.header("🎨 AI Logo Generator")
    from utils import generate_logo_prompt
    brand = st.text_input("Brand Name")
    desc = st.text_area("Logo Description")
    if st.button("Generate Logo"):
        prompt = generate_logo_prompt(brand, desc)
        svg_code = call_grok(prompt)
        st.subheader("Your Generated Logo SVG:")
        st.code(svg_code, language="xml")

# 2. Logo Prompt Generator
elif tool == "Logo Prompt Generator":
    st.header("📝 Logo Prompt Generator")
    brand = st.text_input("Brand Name")
    niche = st.text_input("Brand Niche")
    if st.button("Generate Prompt"):
        prompt = f"Generate a professional logo idea prompt for a brand named {brand} in the niche {niche}. Only one high-quality prompt."
        output = call_grok(prompt)
        st.success(output)

# 3. AI Chatbot
elif tool == "AI Chatbot":
    st.header("🤖 AI Chatbot")
    user_text = st.text_area("Ask anything")
    if st.button("Send"):
        response = call_grok(user_text)
        st.info(response)

# 4. Text Rewriter
elif tool == "Text Rewriter":
    st.header("✍️ AI Text Rewriter")
    text = st.text_area("Enter text")
    if st.button("Rewrite"):
        prompt = f"Rewrite this text in simple, clear English:\n\n{text}"
        output = call_grok(prompt)
        st.success(output)

# 5. Meme Idea Generator
elif tool == "Meme Idea Generator":
    st.header("🤣 Meme Idea Generator")
    topic = st.text_input("Topic")
    if st.button("Generate Meme Idea"):
        prompt = f"Give a funny meme idea about: {topic}. Short, creative, and simple."
        output = call_grok(prompt)
        st.success(output)

# 6. AI Blog Generator
elif tool == "AI Blog Generator":
    st.header("📝 AI Blog Generator")
    topic = st.text_input("Blog Topic", "Benefits of Python")
    word_count = st.slider("Word Count", 100, 2000, 500)
    if st.button("Generate Blog"):
        prompt = f"Write a detailed blog article about: {topic}. Word count: {word_count}. Make it engaging and informative."
        output = call_grok(prompt)
        st.write(output)

# 7. News Article Writer
elif tool == "News Article Writer":
    st.header("📰 News Article Writer")
    headline = st.text_input("Headline", "AI Breakthrough Announced")
    category = st.selectbox("Category", ["Technology","World","Sports","Business","Science"])
    tone = st.selectbox("Tone", ["Neutral","Breaking News","Formal","Informative"])
    if st.button("Generate News Article"):
        prompt = f"Write a detailed news article.\nHeadline: {headline}\nCategory: {category}\nTone: {tone}\nLength: 400-600 words."
        output = call_grok(prompt)
        st.write(output)

# 8. Story Writer
elif tool == "Story Writer":
    st.header("📖 Story Writer")
    genre = st.selectbox("Genre", ["Fantasy","Horror","Sci-Fi","Romance","Adventure"])
    idea = st.text_area("Story Idea", "A child discovers a magical portal.")
    length = st.slider("Story Length (words)", 100, 3000, 500)
    if st.button("Generate Story"):
        prompt = f"Write a {genre} story based on this idea: {idea}. Length: {length} words. Make it creative and engaging."
        output = call_grok(prompt)
        st.write(output)

# 9. YouTube Script Generator
elif tool == "YouTube Script Generator":
    st.header("🎬 YouTube Script Generator")
    title = st.text_input("Video Topic", "How to Learn Python Fast")
    style = st.selectbox("Video Style", ["Educational","Motivational","Funny","Storytelling"])
    duration = st.selectbox("Video Duration", ["3 minutes","5 minutes","10 minutes","15 minutes"])
    if st.button("Generate Script"):
        prompt = f"Create a full YouTube script.\nTopic: {title}\nStyle: {style}\nDuration: {duration}\nInclude: Hook, Intro, Content, CTA, Ending."
        output = call_grok(prompt)
        st.write(output)

# 10. Social Media Caption Writer
elif tool == "Social Media Caption Writer":
    st.header("📱 Social Media Caption Writer")
    platform = st.selectbox("Platform", ["Instagram","TikTok","Facebook","YouTube Shorts"])
    desc = st.text_area("Describe your content", "Aesthetic sunset on the beach")
    vibe = st.selectbox("Caption Vibe", ["Aesthetic","Funny","Motivational","Short & Catchy","Trending"])
    if st.button("Generate Captions"):
        prompt = f"Generate 10 social media captions.\nPlatform: {platform}\nVibe: {vibe}\nContent: {desc}"
        output = call_grok(prompt)
        st.write(output)

# 11. SEO Keyword Generator
elif tool == "SEO Keyword Generator":
    st.header("🔍 SEO Keyword Generator")
    topic = st.text_input("Topic/Keyword", "AI tools for students")
    difficulty = st.selectbox("Keyword Difficulty", ["Easy","Medium","Hard"])
    if st.button("Generate SEO Keywords"):
        prompt = f"Generate SEO keywords for topic: {topic}.\nDifficulty: {difficulty}\nReturn 20 primary, 20 LSI, 10 long-tail keywords optimized for ranking."
        output = call_grok(prompt)
        st.write(output)

# 12. AI Email Writer
elif tool == "AI Email Writer":
    st.header("📧 AI Email Writer")
    email_type = st.selectbox("Email Type", ["Formal","Casual","Business","Complaint","Apology","Job Application"])
    subject = st.text_input("Subject", "Request for Information")
    details = st.text_area("Email Details", "I need details about your pricing and services.")
    if st.button("Generate Email"):
        prompt = f"Write a {email_type} email.\nSubject: {subject}\nDetails: {details}\nInclude polite opening, clear message, professional closing."
        output = call_grok(prompt)
        st.write(output)
