from crewai import Crew , Process
from tools import yt_tool
from agents import blog_writer , blog_researcher
from tasks import research_task , write_task
from llm import llm

crew = Crew(
    agents = [blog_researcher , blog_writer],
    tasks = [research_task , write_task],
    process = Process.sequential,
    memory = True,
    cache = True,
    max_rpm = 100,
    share_crew = False,
    llm = llm,
    embedder={
        "provider": "huggingface",
        "config": {
            "model": "sentence-transformers/all-MiniLM-L6-v2"
        }
    }
)


result = crew.kickoff(inputs={'topic' :'https://youtu.be/0bHoB32fuj0?si=ifPhRTn2bPXXgRVU' })
print(result)

