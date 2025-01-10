import json
import os
import praw
from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field

class RedditGetTopPostsToolInput(BaseModel):
    """Input schema for RedditGetTopPostsTool."""
    subreddit: str = Field(..., description="Name of the subreddit to get posts in. For r/funny/ just input 'funny'.")
    limit: int = Field(..., description="Number of post to retreive.")

class RedditGetTopPostsTool(BaseTool):
    name: str = "Reddit Get Top Posts Tool"
    description: str = (
        "This tool allows you to get top posts in a specified subreddit using reddit API."
    )
    args_schema: Type[BaseModel] = RedditGetTopPostsToolInput

    def _run(self, subreddit: str, limit: int) -> str:
        # Reddit API client initialization (replace with your own Reddit API credentials)
        reddit = praw.Reddit(
            client_id=os.environ['REDDIT_CLIENT_ID'],
            client_secret=os.environ['REDDIT_CLIENT_SECRET'],
            user_agent=os.environ.get('REDDIT_USER_AGENT',"YOUR_USER_AGENT")
        )

        try:
            # Perform the Reddit search on the specified subreddit
            posts = reddit.subreddit(subreddit).top(limit=limit)

            # Collect the results to return as a string
            result = "Top posts for '{}':\n".format(subreddit)
            # data = []
            for post in posts:
                # post = reddit.submission(id=post.id)

                result += json.dumps(post.__dict__, default=str) + "\n"
            
            return result


        except Exception as e:
            return f"Error occurred while searching: {str(e)}"


class RedditGetSubredditToolInput(BaseModel):
    """Input schema for RedditGetSubredditTool."""
    subreddit: str = Field(..., description="Name of the subreddit to get posts in. For r/funny/ just input 'funny'.")

class RedditGetSubredditTool(BaseTool):
    name: str = "Reddit Get Subreddit Tool"
    description: str = (
        "This tool allows you to get subreddit info using reddit API like : Count of subscribers, Name, Display name, Subreddit description in Markdown ."
    )
    args_schema: Type[BaseModel] = RedditGetSubredditToolInput

    def _run(self, subreddit: str) -> any:
        # Reddit API client initialization (replace with your own Reddit API credentials)
        reddit = praw.Reddit(
            client_id=os.environ['REDDIT_CLIENT_ID'],
            client_secret=os.environ['REDDIT_CLIENT_SECRET'],
            user_agent=os.environ.get('REDDIT_USER_AGENT',"YOUR_USER_AGENT")
        )
        try:
            sub = reddit.subreddit(subreddit)
            return json.dumps(sub.__dict__, default=str)

        except Exception as e:
            return f"Error occurred while searching: {str(e)}"
