# 🎥 YouTube to Blog Multi-Agent Creator

A powerful multi-agent AI system built with **CrewAI** that automatically transforms YouTube video content into high-quality, SEO-optimized blog posts. Leveraging **Groq's Llama 3.3** for lightning-fast inference and custom transcript extraction tools.

---

## 🌟 Features

- **Automated Content Extraction**: Custom tool to fetch transcripts directly from YouTube URLs.
- **Multilingual Support**: Supports transcripts in English, Telugu, and Hindi.
- **Multi-Agent Workflow**: 
  - **Blog Researcher**: High-level analysis of video content.
  - **Blog Writer**: Professional summarization and blog post crafting.
- **SEO Optimized**: Generated content is structured for search engine visibility.
- **Local Memory**: Utilizes HuggingFace embeddings for local context management.
- **Groq Integration**: High-performance LLM execution via Groq Cloud.

---

## 🛠️ Tech Stack

- **Framework**: [CrewAI](https://www.crewai.com/)
- **LLM**: Groq Llama 3.3-70b-versatile
- **Embeddings**: HuggingFace (`sentence-transformers/all-MiniLM-L6-v2`)
- **Tools**: `youtube-transcript-api`, `python-dotenv`
- **Environment**: Python 3.12+

---

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have Python 3.12 or higher installed. This project uses `uv` for package management (recommended), but standard `pip` works as well.

### 2. Installation

Clone the repository and install the dependencies:

```bash
# Using pip
pip install crewai youtube-transcript-api python-dotenv langchain-huggingface

# Using uv
uv sync
```

### 3. Environment Setup

Create a `.env` file in the root directory and add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key_here
```

*Note: The system is configured to bypass OpenAI key requirements by using internal placeholders.*

---

## 💻 Usage

To generate a blog post from a YouTube video:

1. Open `crew.py`.
2. Update the video URL in the `kickoff` inputs:
   ```python
   result = crew.kickoff(inputs={'topic': 'https://youtu.be/your-video-id'})
   ```
3. Run the script:
   ```bash
   python crew.py
   ```
4. The final blog post will be saved as `new-blog-post.md` in the root directory.

---

## 📂 Project Structure

- `agents.py`: Defines the **Blog Researcher** and **Blog Writer** agents.
- `tasks.py`: Configuration for content research and writing tasks.
- `tools.py`: Custom `youtube_transcript_tool` implementation.
- `llm.py`: Groq LLM configuration and environment management.
- `crew.py`: The entry point that initializes the Crew and starts the workflow.
- `new-blog-post.md`: Output file for the generated blog content.

---

## 🤖 Meet the Agents

### 🔍 Blog Researcher
- **Role**: Senior Blog Content Researcher.
- **Goal**: Extract relevant insights and data from YouTube video transcripts.
- **Skills**: Expert in content analysis and SEO ranking factors.

### ✍️ Blog Writer
- **Role**: Senior Blog Content Writer.
- **Goal**: Transform research data into an engaging, professional blog post.
- **Skills**: Expert in content marketing and conversion-driven writing.

---

## 📄 License

[MIT License](LICENSE) *(Optional)*
