import streamlit as st
from openai import OpenAI
import os

# -------------------------
# OpenAI setup
# -------------------------
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # Set your key as env variable
client = OpenAI(api_key=OPENAI_API_KEY)

# -------------------------
# Page config
# -------------------------
st.set_page_config(
    page_title="AI Multi-Tool Hub",
    page_icon="🛠️",
    layout="wide"
)

# -------------------------
# Mobile caution
# -------------------------
st.markdown(
    "<p style='color:orange; font-size:14px;'>⚠️ On mobile devices, click the &gt;&gt; icon at the top-left to select tools.</p>",
    unsafe_allow_html=True
)

# -------------------------
# Sidebar Tool Selection
# -------------------------
st.sidebar.title("Select Tool")
tool = st.sidebar.selectbox(
    "Choose a tool:",
    [
        "YouTube Script Writer",
        "Logo Generator",
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

# -------------------------
# Tool: YouTube Script Writer
# -------------------------
if tool == "YouTube Script Writer":
    st.title("🎬 YouTube Script Writer AI")
    st.markdown(
        "Generate professional, engaging YouTube video scripts in seconds. "
        "Just enter your topic and let AI do the rest!"
    )

    # Sidebar options
    tone = st.sidebar.selectbox("Script Tone", ["Informative", "Funny", "Persuasive", "Casual"])
    length = st.sidebar.slider("Script Length (approx words)", 200, 2000, 800, 50)

    topic = st.text_input("Enter your video topic here:", "")

    if st.button("Generate Script"):
        if not topic.strip():
            st.warning("Please enter a topic to generate the script.")
        else:
            with st.spinner("Generating your YouTube script..."):
                try:
                    prompt = (
                        f"Write a {length}-word YouTube video script on the topic: '{topic}'. "
                        f"The tone should be {tone}. Include an engaging intro, main points, and a call-to-action."
                    )

                    response = client.chat.completions.create(
                        model="gpt-4.1-mini",
                        messages=[
                            {"role": "system", "content": "You are a professional YouTube script writer."},
                            {"role": "user", "content": prompt}
                        ],
                        temperature=0.7,
                        max_tokens=length*2
                    )

                    script = response.choices[0].message.content
                    st.success("✅ Script Generated Successfully!")
                    st.text_area("Your YouTube Script", script, height=400)

                    # Download button
                    st.download_button("📥 Download Script", script, file_name=f"{topic[:20]}_script.txt")

                except Exception as e:
                    st.error(f"Error generating script: {e}")

# -------------------------
# Placeholders for other tools
# -------------------------
elif tool == "Logo Generator":
    st.title("🎨 Logo Generator")
    st.info("This tool is coming soon!")

elif tool == "Text Rewriter":
    st.title("✍️ Text Rewriter")
    st.info("This tool is coming soon!")

elif tool == "Meme Idea Generator":
    st.title("😂 Meme Idea Generator")
    st.info("This tool is coming soon!")

elif tool == "AI Blog Generator":
    st.title("📝 AI Blog Generator")
    st.info("This tool is coming soon!")

elif tool == "News Article Writer":
    st.title("📰 News Article Writer")
    st.info("This tool is coming soon!")

elif tool == "Story Writer":
    st.title("📖 Story Writer")
    st.info("This tool is coming soon!")

elif tool == "Social Media Caption Writer":
    st.title("💬 Social Media Caption Writer")
    st.info("This tool is coming soon!")

elif tool == "SEO Keyword Generator":
    st.title("🔑 SEO Keyword Generator")
    st.info("This tool is coming soon!")

elif tool == "AI Email Writer":
    st.title("📧 AI Email Writer")
    st.info("This tool is coming soon!")
