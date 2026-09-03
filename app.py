import streamlit as st
from groq import Groq

# Page Configuration
st.set_page_config(
    page_title="AI Content Assistant",
    page_icon="✍️",
    layout="centered"
)

st.title("✍️ AI Content Assistant")
st.write("Generate tailored posts, captions, and hashtags in seconds.")

# Read API key securely from Streamlit secrets or sidebar input
groq_api_key = st.secrets.get("GROQ_API_KEY", "")

if not groq_api_key:
    groq_api_key = st.sidebar.text_input("Enter Groq API Key:", type="password")

if not groq_api_key:
    st.info("💡 Please add your Groq API key in the sidebar (or secrets) to continue.")
    st.stop()

# Initialize Groq client
client = Groq(api_key=groq_api_key)

# Input Form
with st.form("content_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        platform = st.selectbox(
            "Platform", 
            ["LinkedIn", "Twitter / X", "Instagram", "Facebook", "Blog Post"]
        )
        content_type = st.selectbox(
            "Content Type", 
            ["Educational", "Promotional", "Storytelling", "Announcement", "Tips & Tricks"]
        )
        tone = st.selectbox(
            "Tone", 
            ["Professional", "Casual & Friendly", "Persuasive", "Humorous", "Inspirational"]
        )

    with col2:
        topic = st.text_input("Topic", placeholder="e.g., Remote Work Productivity")
        target_audience = st.text_input("Target Audience", placeholder="e.g., Software Developers, Freelancers")

    submit_button = st.form_submit_button("Generate Content 🚀")

# Generation Logic
if submit_button:
    if not topic or not target_audience:
        st.warning("Please fill in both the Topic and Target Audience fields.")
    else:
        with st.spinner("Generating content with Groq..."):
            prompt = f"""
            You are an expert social media manager and copywriter.
            Generate a complete post based on the following requirements:

            - Platform: {platform}
            - Content Type: {content_type}
            - Topic: {topic}
            - Target Audience: {target_audience}
            - Tone: {tone}

            Structure the response clearly as follows:
            1. **Main Post / Caption**: Engaging content tailored for the specified platform format.
            2. **Call to Action (CTA)**: A clear prompt encouraging viewer interaction.
            3. **Relevant Hashtags**: 5 to 10 popular and relevant hashtags.
            """

            try:
                # Using llama-3.3-70b-versatile model
                completion = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.7,
                    max_tokens=1000,
                )

                generated_content = completion.choices[0].message.content

                st.subheader("🎉 Generated Content")
                st.markdown(generated_content)

            except Exception as e:
                st.error(f"Error generating content: {e}")
