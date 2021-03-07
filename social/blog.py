import feedparser

from social import tool

START_COMMENT = '<!-- START_SECTION:blog -->'
END_COMMENT = '<!-- END_SECTION:blog -->'


def fetch(rss_link, limit) -> str:
    entries = feedparser.parse(rss_link)["entries"]
    arr = [
        {
            "title": entry["title"],
            "url": entry["link"].split("#")[0],
            "published": entry["published"].split("T")[0],
        }
        for entry in entries[:limit]
    ]

    return "\n".join(
        ["* <a href='{url}' target='_blank'>{title}</a> - {published}".format(**item) for item in arr]
    )


def generate(rss_link, limit, readme) -> str:
    content = fetch(rss_link, limit)
    return tool.generate_new_readme(START_COMMENT, END_COMMENT, content, readme)
