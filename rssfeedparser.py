import feedparser

# Define news sources and the RSS-addresses
NEWSSOURCES = {
    "BBC News (World)": "http://feeds.bbci.co.uk/news/world/rss.xml",
    "Al Jazeera": "https://www.aljazeera.com/xml/rss/all.xml",
    "Helsingin Sanomat": "https://www.hs.fi/rss/tuoreimmat.xml",
    "NYTimes": "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml",
    "Yle Uutiset": "https://yle.fi/rss/uutiset/paauutiset",
}

def fetch_and_show_news():
    print("=" * 40)
    print(" PÄIVÄN TUOREIMMAT UUTISOTSIKOT ")
    print("=" * 40)

    for name, url in NEWSSOURCES.items():
        print(f"\n   --- {name.upper()} ---")
        
        # Let's parse the feed
        feed = feedparser.parse(url)
        
        # Let's check if we got news (and the addresses are correct)
        if not feed.entries:
            print("Uutisia ei voitu hakea juuri nyt.")
            continue

        # Show five latest news
        for i, news in enumerate(feed.entries[:5], 1):
            print(f"   {i}. {news.title}")

    print("\n" + "=" * 40)

if __name__ == "__main__":
    fetch_and_show_news()
