import feedparser
from datetime import datetime
from ebooklib import epub
import os

from src.extract_text import fetch_article_text, make_file_title

"""
metodo per la creazione del file epub
"""

OUTPUT_DIR = "ebooks"

def create_ebook(feed: feedparser.FeedParserDict) -> str | None:
    """
    Crea un epub da gli rss parsati con da feedparser
    :param feed: rss url
    :return: path del salvataggio TODO: da rivedere questo ritorno
    """
    feed_title = feed["feed"].get("title", "Quotidiano")
    today = datetime.now().strftime("%Y-%m-%d")

    book = epub.EpubBook()
    book.set_identifier(f"{make_file_title(feed_title)}-{today}")
    book.set_title(f"{feed_title} - {today}")
    book.set_language("it")
    book.add_author(feed_title)

    chapters = []
    total = len(feed.entries)
    for i, entry in enumerate(feed.entries, start=1):
        title = entry.get("title", f"Articolo {i}")
        link = entry.get("link", "")
        published = entry.get("published", "")

        print(f"({i}/{total}) Scarico articolo completo: {title}")
        body = fetch_article_text(link)

        if not body:
            # se non riesco a scaricare/estrarre l'articolo, usa riassunto dell'rss
            summary = entry.get("summary", entry.get("description", ""))
            body = f"{summary}<p><em>(Testo completo non disponibile, mostrato il riassunto RSS)</em></p>"

        content_html = f"""
        <h1>{title}</h1>
        <p><em>{published}</em></p>
        {body}
        <p><a href="{link}">Link all'articolo originale</a></p>
        """

        chapter = epub.EpubHtml(
            title=title,
            file_name=f"articolo_{i}.xhtml",
            lang="it",
        )
        chapter.content = content_html
        book.add_item(chapter)
        chapters.append(chapter)

    if not chapters:
        return None

    # indice
    book.toc = tuple(chapters)
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())
    book.spine = ["nav"] + chapters

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    filename = os.path.join(OUTPUT_DIR, f"{make_file_title(feed_title)}-{today}.epub")
    epub.write_epub(filename, book)

    return filename
