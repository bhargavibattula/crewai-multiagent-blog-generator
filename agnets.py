from crewai import Agent
from tools import yt_tool
from llm import llm
from dotenv import load_dotenv 
import os 
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPEN_AI_MODEL_NAME"] = "gpt-4o"

## create a senior blog content researcher 
blog_researcher = Agent(
    role ='Blog Researcher from Youtube Videos',
    goal = 'get the relevant video content fot the topic {topic} from YouTube Channel',
    verbose = True,
    llm = llm,
    memory = True,
    backstory = """
    You are a senior blog content researcher with 5+ years of experience in the field.
    You have a proven track record of creating high-quality blog content that ranks well in search engines.
    You are an expert in SEO and have a deep understanding of how to create content that ranks well in search engines.
    You are also an expert in content marketing and have a deep understanding of how to create content that converts.
    """,
    tools = [yt_tool],
    allow_deligation = True

)


### creating a senior blog writer agent with yt tool 
blog_writer = Agent(

    role = 'Senior Blog Content Writer',
    goal = 'write a high quality blog post on the topic {topic} using the research from the blog researcher',
    verbose = True,
    memory = True,
    backstory = """
    You are a senior blog content writer with 5+ years of experience in the field.
    You have a proven track record of creating high-quality blog content that ranks well in search engines.
    You are an expert in SEO and have a deep understanding of how to create content that ranks well in search engines.
    You are also an expert in content marketing and have a deep understanding of how to create content that converts.
    """,
    tools = [yt_tool],
    allow_deligation = True
)



