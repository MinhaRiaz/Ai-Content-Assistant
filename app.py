
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
    groq_api_key = st.sidebar.text_input(
        "Enter Groq API Key:",
        type="password"
    )

if not groq_api_key:
    st.info(
        "💡 Please add your Groq API key in the sidebar "
        "(or secrets) to continue."
    )
    st.stop()

# Initialize Groq client
client = Groq(api_key=groq_api_key)

# Input Form
with st.form("content_form"):

    col1, col2 = st.columns(2)

    with col1:
        platform = st.selectbox(
            "Platform",
            [
                "LinkedIn",
                "Twitter / X",
                "Instagram",
                "Facebook",
                "Blog Post"
            ]
        )

        content_type = st.selectbox(
            "Content Type",
            [
                "Educational",
                "Promotional",
                "Storytelling",
                "Announcement",
                "Tips & Tricks"
            ]
        )

        tone = st.selectbox(
            "Tone",
            [
                "Professional",
                "Casual & Friendly",
                "Persuasive",
                "Humorous",
                "Inspirational"
            ]
        )

    with col2:
        topic = st.text_input(
            "Topic",
            placeholder="e.g., Remote Work Productivity"
        )

        target_audience = st.text_input(
            "Target Audience",
            placeholder="e.g., Software Developers, Freelancers"
        )

        # Content Length
        length = st.selectbox(
            "Content Length",
            ["Short", "Medium", "Long"]
        )

    submit_button = st.form_submit_button(
        "Generate Content 🚀"
    )


# Generation Logic
if submit_button:

    if not topic or not target_audience:
        st.warning(
            "Please fill in both the Topic and Target Audience fields."
        )

    else:

        # Set token limit according to selected length
        if length == "Short":
            max_tokens = 400
            length_instruction = """
            Keep the content short and concise.
            Use approximately 80–150 words for the main content.
            Avoid unnecessary explanations.
            """

        elif length == "Medium":
            max_tokens = 700
            length_instruction = """
            Create a moderately detailed piece of content.
            Use approximately 150–300 words for the main content.
            Provide enough detail while remaining easy to read.
            """

        else:
            max_tokens = 1200
            length_instruction = """
            Create detailed and comprehensive content.
            Use approximately 300–500+ words for the main content.
            Include useful explanations, examples, or supporting details
            where appropriate.
            """

        with st.spinner("Generating content with Groq..."):

            prompt = f"""
            You are an expert social media manager and professional copywriter.

            Generate high-quality content based on the following requirements:

            - Platform: {platform}
            - Content Type: {content_type}
            - Topic: {topic}
            - Target Audience: {target_audience}
            - Tone: {tone}
            - Selected Length: {length}

            LENGTH REQUIREMENT:
            {length_instruction}

            IMPORTANT:
            The selected length must have a noticeable effect on the
            generated content. Do not generate a long response when
            Short is selected, and do not make a Long response too brief.

            Structure the response clearly as follows:

            1. **Main Post / Caption**
            Write engaging content specifically tailored to the selected
            platform, topic, audience, tone, and length.

            2. **Call to Action (CTA)**
            Provide a clear and relevant call to action that encourages
            the audience to interact.

            3. **Relevant Hashtags**
            Provide 5 to 10 relevant hashtags.

            Make the content natural, engaging, and ready to publish.
            """

            try:

                completion = client.chat.completions.create(
                    model="openai/gpt-oss-120b",
                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    temperature=0.7,
                    max_tokens=max_tokens,
                )

                generated_content = (
                    completion.choices[0].message.content
                )

                st.subheader("🎉 Generated Content")
                st.markdown(generated_content)

            except Exception as e:
                st.error(
                    f"Error generating content: {e}"
                )

