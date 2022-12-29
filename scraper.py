import praw

reddit = praw.Reddit(
    client_id="Ez4A5nXmt2pmoegmrqLfTw",
    client_secret="Zo80022nFQPDyncV-8DyNJ11Z000Cg",
    password="GBakery4767",
    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 "
               "Safari/537.36",
    username="mightybaker1",
)


def news2Array(sub, time, upvoteScore):
    news = {}
    subreddit = reddit.subreddit(sub)
    global j
    j = 0
    for submission in subreddit.top(time_filter=time):
        if submission.score > upvoteScore:
            news[j] = submission.title, submission.url, submission.score
        j = j + 1
    return news
