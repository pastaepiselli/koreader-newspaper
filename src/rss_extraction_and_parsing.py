import feedparser

def read_rss(path: str = "quotidiani.txt") -> list[str]:
    """Legge l'elenco degli URL dei feed RSS da un file di testo (uno per riga).
    Ignora righe vuote e righe che iniziano con '#' (commenti).
    """
    feed_rss: list[str] = []
    with open(path, "r") as file:
        for line in file:
            url = line.strip()
            if not url or url.startswith("#"):
                continue
            feed_rss.append(url)

    return feed_rss

def parse_feed(url: str) -> feedparser.FeedParserDict:
    """
    Da l'url del rss ritorna un dizionario per l' estrazione
    :param url: url del feed rss
    :return: feedparser.FeedParserDict
    """
    d = feedparser.parse(url)

    if d.bozo and not d.entries:
        print(f"  [!] Errore nel parsing di {url}: {d.bozo_exception}")
        return None

    if not d.entries:
        print(f"  [!] Nessun articolo trovato in {url}")
        return None

    return d
