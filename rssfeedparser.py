import feedparser

# Määritellään uutislähteet ja niiden RSS-osoitteet
UUTISLAHTEET = {
    "BBC News (World)": "http://feeds.bbci.co.uk/news/world/rss.xml",
    "Der Spiegel": "https://www.spiegel.de/index.rss",
    "Helsingin Sanomat": "https://www.hs.fi/rss/tuoreimmat.xml",
    "Yle Uutiset": "https://yle.fi/rss/uutiset/paauutiset",
}

def hae_ja_nayta_uutiset():
    print("=" * 40)
    print(" PÄIVÄN TUOREIMMAT UUTISOTSIKOT ")
    print("=" * 40)

    for nimi, url in UUTISLAHTEET.items():
        print(f"\n--- {nimi.upper()} ---")
        
        # Parsitaan syöte
        syote = feedparser.parse(url)
        
        # Tarkistetaan, saatiinko uutisia (varmistetaan ettei linkki ole rikki)
        if not syote.entries:
            print("Uutisia ei voitu hakea juuri nyt.")
            continue

        # Otetaan 5 ensimmäistä uutista
        for i, uutinen in enumerate(syote.entries[:5], 1):
            print(f"{i}. {uutinen.title}")
            # print(f"   Lue lisää: {uutinen.link}") # Poista kommentti jos haluat linkit

    print("\n" + "=" * 40)
    print("Haku valmis.")

if __name__ == "__main__":
    hae_ja_nayta_uutiset()
