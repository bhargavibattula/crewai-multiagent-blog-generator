import os
from dotenv import load_dotenv
from crewai import LLM

load_dotenv()

# Set placeholders for various API keys to bypass default checks 
# in libraries that still expect them, even when using Groq/Local models.
if 'OPENAI_API_KEY' not in os.environ:
    os.environ['OPENAI_API_KEY'] = 'NA'

if 'CHROMA_HUGGINGFACE_API_KEY' not in os.environ:
    os.environ['CHROMA_HUGGINGFACE_API_KEY'] = 'NA'

if 'HUGGINGFACE_API_KEY' not in os.environ:
    os.environ['HUGGINGFACE_API_KEY'] = 'NA'

# Initialize the Groq LLM (using the groq liteLLM provider syntax)
llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    api_key=os.environ.get("GROQ_API_KEY")
)
