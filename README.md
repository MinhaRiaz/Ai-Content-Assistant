# ✍️ AI Content Assistant

An AI-powered **Content Generator** built with **Streamlit** and **Groq** that helps users create tailored social media posts, captions, calls-to-action, and relevant hashtags in seconds.

The application allows users to customize generated content based on the **platform, content type, topic, target audience, tone, and desired content length**.

## 🚀 Live Demo

🌐 **Try the AI Content Assistant:**
https://ai-content-assistant-app.streamlit.app/

---

## 📌 Overview

Creating engaging content for different social media platforms can be time-consuming. The **AI Content Assistant** simplifies this process by using a large language model through the Groq API to generate platform-specific content.

Users simply provide their content requirements, select their preferred options, and the application generates ready-to-use content.

---

## ✨ Features

### 🎯 Platform Selection

Generate content specifically for:

* LinkedIn
* Twitter / X
* Instagram
* Facebook
* Blog Post

### 📝 Content Type

Choose the type of content you want to generate:

* Educational
* Promotional
* Storytelling
* Announcement
* Tips & Tricks

### 🎨 Tone Selection

Customize the writing style:

* Professional
* Casual & Friendly
* Persuasive
* Humorous
* Inspirational

### 📏 Content Length

Control how detailed the generated content should be:

* **Short** — concise content
* **Medium** — moderately detailed content
* **Long** — detailed and comprehensive content

The selected length influences both the AI prompt and the maximum generation limit.

### 👥 Target Audience

Specify who the content is intended for, such as:

* Software Developers
* Freelancers
* Students
* Entrepreneurs
* Business Owners
* Marketing Professionals

### 📣 Automatic CTA

The AI generates a relevant **Call to Action (CTA)** designed to encourage audience interaction.

### #️⃣ Hashtag Generation

The application automatically generates **5–10 relevant hashtags** based on the selected topic and content.

### 🔐 Secure API Key Handling

The application supports loading the Groq API key through **Streamlit Secrets** or entering it through the sidebar.

---

## 🛠️ Technologies Used

| Technology       | Purpose                                  |
| ---------------- | ---------------------------------------- |
| **Python**       | Core programming language                |
| **Streamlit**    | Web application interface                |
| **Groq API**     | AI inference and content generation      |
| **GPT-OSS-120B** | Large language model used for generation |

The application uses Groq's OpenAI-compatible chat completion interface to generate the content.

---

## 🧠 How It Works

The application follows a simple workflow:

```text
User Input
    ↓
Select Platform
    ↓
Select Content Type
    ↓
Select Tone
    ↓
Enter Topic
    ↓
Enter Target Audience
    ↓
Select Content Length
    ↓
Generate Prompt
    ↓
Groq API
    ↓
AI Model
    ↓
Generated Content
    ↓
Post + CTA + Hashtags
```

---

## 📋 Generated Content Structure

Every generated response is organized into three main sections:

### 1. Main Post / Caption

The AI creates engaging content based on the selected platform, topic, audience, tone, and length.

### 2. Call to Action

A relevant CTA is generated to encourage users to interact with the content.

### 3. Relevant Hashtags

The application generates 5–10 relevant hashtags for the selected topic.

---

## 📏 Content Length Logic

The application dynamically adjusts the generation according to the selected length.

| Length | Approximate Main Content | Max Tokens |
| ------ | -----------------------: | ---------: |
| Short  |             80–150 words |        400 |
| Medium |            150–300 words |        700 |
| Long   |           300–500+ words |       1200 |

The token limit acts as a maximum generation boundary, while the prompt provides the model with the desired approximate word range.

---

## 📂 Project Structure

```text
AI-Content-Assistant/
│
├── app.py
├── requirements.txt
├── README.md
│
└── .streamlit/
    └── secrets.toml
```

### `app.py`

Contains the complete Streamlit application, user interface, prompt construction, Groq API integration, and content-generation logic.

### `requirements.txt`

Contains the Python dependencies required to run the application.

### `.streamlit/secrets.toml`

Stores the Groq API key securely when running locally or deploying through Streamlit Community Cloud.

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

Move into the project directory:

```bash
cd AI-Content-Assistant
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add Your Groq API Key

Create:

```text
.streamlit/secrets.toml
```

Add:

```toml
GROQ_API_KEY = "your_groq_api_key_here"
```

**Never upload your actual API key to GitHub.**

You can also enter the API key through the application's sidebar.

### 5. Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 🔑 API Key Configuration

For local development, use:

```toml
GROQ_API_KEY = "your_groq_api_key_here"
```

For Streamlit deployment, add the same secret through the application's **Secrets** settings instead of committing `secrets.toml` to GitHub.

Streamlit supports using secrets for API keys and other credentials in deployed applications.

---

## 🌐 Deployment

This application can be deployed using **Streamlit Community Cloud**.

General deployment steps:

1. Push the project to GitHub.
2. Open Streamlit Community Cloud.
3. Connect your GitHub repository.
4. Select `app.py` as the main file.
5. Add your `GROQ_API_KEY` under Streamlit Secrets.
6. Deploy the application.

After deployment, Streamlit provides a public URL that can be shared with others.

---

## 🔒 Security

The Groq API key should **never** be hardcoded into the source code.

❌ Do not do this:

```python
groq_api_key = "gsk_your_secret_key"
```

✅ Instead, use Streamlit Secrets:

```python
groq_api_key = st.secrets.get("GROQ_API_KEY", "")
```

Also make sure `.streamlit/secrets.toml` is included in `.gitignore`:

```text
.streamlit/secrets.toml
```

---

## 💡 Example

Suppose the user enters:

```text
Platform: LinkedIn
Content Type: Educational
Topic: Artificial Intelligence
Target Audience: Computer Science Students
Tone: Professional
Content Length: Medium
```

The AI generates a professional LinkedIn post about Artificial Intelligence specifically targeted toward Computer Science students, followed by a suitable CTA and relevant hashtags.

---

## 🎯 Use Cases

The AI Content Assistant can be useful for:

* 📱 Social media managers
* 💼 Freelancers
* 👩‍💻 Developers
* 🎓 Students
* 🚀 Entrepreneurs
* 📢 Digital marketers
* 🏢 Small businesses
* ✍️ Content creators
* 📈 Personal branding

---

## 🔮 Future Improvements

Possible future enhancements include:

* [ ] Custom word-count input
* [ ] Multiple content variations
* [ ] Content regeneration
* [ ] Copy-to-clipboard button
* [ ] Download generated content
* [ ] Save generation history
* [ ] Custom hashtag count
* [ ] Language selection
* [ ] Brand voice customization
* [ ] SEO optimization
* [ ] AI-powered content refinement
* [ ] Image generation for social media posts
* [ ] User authentication

---

## 📚 Learning Resources

* [Streamlit Documentation](https://docs.streamlit.io/?utm_source=chatgpt.com)
* [Streamlit Generative AI Resources](https://streamlit.io/generative-ai?utm_source=chatgpt.com)
* [Groq Documentation](https://console.groq.com/docs?utm_source=chatgpt.com)

---

## 👩‍💻 Author

**Minha Khan**

Computer Science Student | AI & Software Development

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

---

## 📄 License

This project is available for educational and personal use.
