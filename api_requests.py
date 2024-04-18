import praw
import datetime
import json

reddit = praw.Reddit(
    client_id = " ",#replace client_id
    client_secret = " ",#replace_client_secret
    user_agent = "my-app u/m_runthat",
)

subreddit = reddit.subreddit("datascience")

try:
    #to fetch up to 5,000 top posts from 2023
    top_posts = subreddit.top(time_filter="year",limit=1000)
    posts_data = []

    for post in top_posts:
        #only fetch top-level comments
        post.comments.replace_more(limit=0)
        comments_data = [comment.body for comment in  post.comments[:5]]

        post_info = {
            "id" : post.id,
            "datetime" : post.created_utc,
            "flair" : post.link_flair_text,
            "title" : post.title,
            "score" : post.score,
            "comment counts" : post.num_comments,
            "content" : post.selftext,
            "comments" : comments_data,
        }
        posts_data.append(post_info)

        #optional - for testing outputs
        #for post in  posts_data:
            #print(post)

except Exception as e:
    print("An error occurred:", e)

#specifying file path to store data
file_path = 'C:\\Yadanar\\Learning Resources\\Python\\WebScraping\\reddit_data.json'

#Write the data to a JSON file
with open(file_path, 'w', encoding='utf-8') as file:
    json.dump(posts_data, file, indent=4)

print("Data has been written to", file_path)
