from crewai import Task
from tools import yt_tool
from agents import blog_writer , blog_researcher




### research task 
research_task = Task(
    description = """
    You are a senior blog content researcher with 5+ years of experience in the field.
    identify the video {topic}
    get detailed information about the video from channel
    """,
    expected_output = """
    a comprehensive 3 paragraphs long report based on {topic} of video  content 
    """,
    agent = blog_researcher,
    tools = [yt_tool],
    allow_deligation = True
)

write_task = Task(
    description = """
    get the info from youtube channel on topic {topic}
    """,
    expected_output = """
    summarize the info from youtube channel on topic {topic} and create the content for the blog
    """,
    agent = blog_writer,
    tools = [yt_tool],
    allow_deligation = True,
    async_execution = False,
    output_file = 'new-blog-post.md'


)