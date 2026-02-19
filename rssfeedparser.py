import feedparser

# Define news sources and the RSS-addresses
UUTISLAHTEET = {
    "BBC News (World)": "http://feeds.bbci.co.uk/news/world/rss.xml",
    "Der Spiegel": "https://www.spiegel.de/index.rss",
    "Helsingin Sanomat": "https://www.hs.fi/rss/tuoreimmat.xml",
    "NYTimes": "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml",
    "Yle Uutiset": "https://yle.fi/rss/uutiset/paauutiset",
}

def hae_ja_nayta_uutiset():
    print("=" * 40)
    print(" PÄIVÄN TUOREIMMAT UUTISOTSIKOT ")
    print("=" * 40)

    for nimi, url in UUTISLAHTEET.items():
        print(f"\n--- {nimi.upper()} ---")
        
        # Let's parse the feed
        syote = feedparser.parse(url)
        
        # Let's check if we got news (and the addresses are correct)
        if not syote.entries:
            print("Uutisia ei voitu hakea juuri nyt.")
            continue

        # Show five latest news
        for i, uutinen in enumerate(syote.entries[:5], 1):
            print(f"{i}. {uutinen.title}")
            # print(f"   Lue lisää: {uutinen.link}") # Poista kommentti jos haluat linkit

    print("\n" + "=" * 40)

if __name__ == "__main__":
    hae_ja_nayta_uutiset()
