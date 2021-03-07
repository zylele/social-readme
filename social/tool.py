import datetime
import re


def generate_new_readme(start_comment: str, end_comment: str, content: str, readme: str) -> str:
    """Generate a new Readme.md"""
    pattern = f"{start_comment}[\\s\\S]+{end_comment}"
    stats_in_readme = f"{start_comment}\n{content}\n{end_comment}"
    return re.sub(pattern, stats_in_readme, readme)


def format_time(timestamp) -> str:
    gmt_format = '%a, %d %b %Y %H:%M:%S GMT'
    date_str = datetime.datetime.strptime(timestamp, gmt_format) + datetime.timedelta(hours=8)
    return date_str.date()

def test(i):
    i = i + 1
    print("fff:" + str(i))

if __name__ == "__main__":
    test(int("2"))