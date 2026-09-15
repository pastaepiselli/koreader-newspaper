# Koreader-newspaper
Python script extracting daily news from rss newspaper feeds, 
returing them as `.epub` than send to koreader via `SSH`.

## How it works 
1. It retrives rss feed links from `quotidiani.txt` file
2. Parses with [feedparser](https://pypi.org/project/feedparser/)
3. Extract articles from links with [requests](https://pypi.org/project/requests/) 
4. Extract only text with no ads with my love [trafilatura](https://pypi.org/project/trafilatura/)
5. Compiles `epub` with [epublib](https://pypi.org/project/epublib/).
6. Sends to Koreader with [paramiko](https://pypi.org/project/paramiko/)  

## Still in development
- [x] article extraction
- [ ] sending epubs to koreader via SSH
- [ ] better article visualization


