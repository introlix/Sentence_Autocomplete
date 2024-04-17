import os
import sys
import praw
import requests
import wikipedia
from dotenv import load_dotenv
from praw.models import MoreComments

load_dotenv()

# Getting WikiPedia Data
wiki_data_path = "data/wiki_data/wiki_data.txt"
def fetch_data_from_wikipedia(title):
  wiki_data = wikipedia.page(title).content
  
  with open(wiki_data_path, "a", encoding="utf-8") as f:
     f.write(wiki_data)

# Getting Reddit Data
reddit_post_id = []
reddit_data_path = "data/reddit_data/reddit_data.txt"
def fetch_data_from_reddit(subreddit):
   reddit = praw.Reddit(
      client_id = os.getenv("CLIENT_ID"),
      client_secret=os.getenv("CLIENT_SECRET"),
      user_agent="introlix by u/CodingWithSatyam",
   )

   # Getting Reddit Post Title and Id

   subreddit = reddit.subreddit(subreddit)

   top_posts = subreddit.top(limit=50)

   for post in top_posts:
      with open(reddit_data_path, "a", encoding="utf-8") as f:
         f.write(post.title)
      reddit_post_id.append(post.id)

   # Getting Reddit Post Comments

   for post_id in reddit_post_id:
      submission = reddit.submission(id=post_id)

      for top_level_comment in submission.comments:
         if isinstance(top_level_comment, MoreComments):
            continue
         with open(reddit_data_path, "a", encoding="utf-8") as f:
            f.write(top_level_comment.body)

   

    


if __name__ == '__main__':
    # list_of_wiki_data = ["Python_(programming_language)", "JavaScript", "Java", "Computer_programming", "C_Sharp_(programming_language)", "Laptop", "Desktop_computer", "Biology"]

    # for title in list_of_wiki_data:
    #    fetch_data_from_wikipedia(title)

    list_of_reddit_subreddit = ['Programming', 'MachineLearning', 'deeplearning', 'webdev', 'blender', 'AskReddit']
    more_subreddit = ['science', 'askscience', 'space']

    for subreddit in more_subreddit:
       fetch_data_from_reddit(subreddit)