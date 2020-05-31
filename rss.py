import feedparser

NewsFeed = feedparser.parse("https://www.upwork.com/ab/feed/jobs/rss?api_params=1&amp;orgUid=817028735655936002&amp;securityToken=19190f2eab51942de3094fa07e26242cf8752ef30dc8b4f04bb224d6471fcb7d14d8ad372f0cefbc6a61b530427bf6cf41eda3797456197a301757483886904d&amp;sort=recency&amp;userUid=817028735655936000")
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