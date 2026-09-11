import trafilatura
import requests

REQUEST_TIMEOUT = 15

def fetch_article_text(url: str) -> str | None:
    """
    Scarica la pagina dell'articolo ed estrare solo il contenuto testuale non descrizione
    :param url: url dell'articolo presente nel feed
    :return: contentuto testuale dell'articolo
    """
    if not url:
        return None

    try:
        resp = requests.get(
            url,
            timeout=REQUEST_TIMEOUT,
        )
        resp.raise_for_status()
    except requests.RequestException as e:
        print(f"    [!] Impossibile scaricare l'articolo ({url}): {e}")
        return None

    # goated
    text = trafilatura.extract(
        resp.text,
        url=url,
        include_comments=False,
        include_tables=True,
        include_images=False,
        favor_recall=True,
    )

    if not text:
        return None

    # deubga
    print(text)

    # trafilatura ritorna testo semplice con paragrafi separati da \n\n:
    # lo trasformiamo in HTML per l'ePub.
    paragraphs = [p.strip() for p in text.split("\n") if p.strip()]
    return "\n".join(f"<p>{p}</p>" for p in paragraphs)


def make_file_title(text: str) -> str:
    """Trasforma un titolo in un nome file sicuro."""
    # TODO: rimuovere caratteri speciali
    text = text.replace(" ", "-").lower()
    return text

