import feedparser

from social import tool

START_COMMENT = '<!-- START_SECTION:douban -->'
END_COMMENT = '<!-- END_SECTION:douban -->'


def fetch(name, limit) -> str:
    entries = feedparser.parse("https://www.douban.com/feed/people/" + name + "/interests")["entries"]
    arr = [
        {
            "title": item["title"],
            "url": item["link"].split("#")[0],
            "published": tool.format_time(item["published"])
        }
        for item in entries[:limit]
    ]

    return "\n".join(
        ["* <a href='{url}' target='_blank'>{title}</a> - {published}".format(**item) for item in arr]
    )


def generate(username, limit, readme) -> str:
    content = fetch(username, limit)
    return tool.generate_new_readme(START_COMMENT, END_COMMENT, content, readme)
