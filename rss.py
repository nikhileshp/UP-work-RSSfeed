import feedparser

NewsFeed = feedparser.parse("https://www.upwork.com/ab/feed/jobs/rss?api_params=1&amp;orgUid=<UID>&amp;securityToken=<SEC_TOKEN>&amp;sort=recency&amp;userUid=<USERUID>")
if(NewsFeed.status == 200):

    pub_list = NewsFeed.feed.published.split(" ")[0:-2]
    published = " ".join(pub_list)
    print("Updated on {}".format(published))
    print()
    for i in NewsFeed.entries:
        print(i.title)
        print(i.link)
    print(len(NewsFeed.entries))
else:
    print("Unable to Connect")
