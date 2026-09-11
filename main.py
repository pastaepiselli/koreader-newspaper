from src.create_epub import create_ebook
from src.rss_extraction_and_parsing import read_rss, parse_feed

if __name__ == "__main__":
    feeds: list[str] = read_rss("quotidiani.txt")

    for f in feeds:
        feed = parse_feed(f)
        if not feed:
            continue
        path = create_ebook(feed)
        print(path)

