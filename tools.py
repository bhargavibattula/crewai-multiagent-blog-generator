import os
import re
from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi
from crewai.tools import tool

load_dotenv()

@tool("youtube_transcript_tool")
def yt_tool(video_url: str):
    """
    Get the transcript of a YouTube video given its URL.
    Useful for extracting content from a specific video for research or summarization.
    """
    try:
        # Extract video ID from URL using regex
        video_id = ""
        # Handle youtu.be/ID format
        if "youtu.be/" in video_url:
            video_id = video_url.split("youtu.be/")[-1].split("?")[0]
        # Handle youtube.com/watch?v=ID format
        elif "v=" in video_url:
            video_id = video_url.split("v=")[-1].split("&")[0]
        else:
            # Fallback regex for other cases
            match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11}).*", video_url)
            if match:
                video_id = match.group(1)
            else:
                return "Error: Could not extract video ID from URL."

        # Try to fetch transcript in priority: English, then Telugu, then Hindi
        transcript = YouTubeTranscriptApi().fetch(video_id, languages=['en', 'te', 'hi', 'en-US'])
        text = " ".join([t.text for t in transcript])
        return text
    except Exception as e:
        return f"Error: {str(e)}"
