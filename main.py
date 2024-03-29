import base64
import os
import sys
from github import Github, GithubException

import social

REPOSITORY = os.getenv('INPUT_REPOSITORY')
GH_TOKEN = os.getenv('INPUT_GH_TOKEN')

COMMIT_MESSAGE = os.getenv("INPUT_COMMIT_MESSAGE")

FILE_PATH = os.getenv("INPUT_FILE_PATH")

BLOG_RSS_LINK = os.getenv('INPUT_BLOG_RSS_LINK')
BLOG_LIMIT = int(os.getenv('INPUT_BLOG_LIMIT'))

DOUBAN_NAME = os.getenv('INPUT_DOUBAN_NAME')
DOUBAN_LIMIT = int(os.getenv('INPUT_DOUBAN_LIMIT'))


def decode_readme(data: str) -> str:
    """Decode the contents of old readme"""
    decoded_bytes = base64.b64decode(data)
    return str(decoded_bytes, 'utf-8')


if __name__ == "__main__":
    g = Github(GH_TOKEN)
    try:
        repo = g.get_repo(REPOSITORY)
    except GithubException as e:
        print(
            "Authentication Error. Try saving a GitHub Token in your Repo Secrets or Use the GitHub Actions Token, "
            "which is automatically used by the action.")
        print(e)
        sys.exit(1)

    try:
        if FILE_PATH is not None and len(FILE_PATH.strip()) > 0:
            print("FILE_PATH:" + FILE_PATH)
            contents = repo.get_contents(FILE_PATH)
        else:
            contents = repo.get_readme()
    except GithubException as e:
        print("Get file Error. Please check the file path")
        print(e)
        sys.exit(1)

    old_readme = decode_readme(contents.content)
    new_readme = old_readme

    if BLOG_RSS_LINK is not None and len(BLOG_RSS_LINK.strip()) > 0 and BLOG_LIMIT > 0:
        print("BLOG_RSS_LINK:" + BLOG_RSS_LINK)
        print("BLOG_LIMIT:" + str(BLOG_LIMIT))
        new_readme = social.generate_blog(BLOG_RSS_LINK, BLOG_LIMIT, new_readme)

    if DOUBAN_NAME is not None and len(DOUBAN_NAME.strip()) > 0 and DOUBAN_LIMIT > 0:
        print("DOUBAN_NAME:" + DOUBAN_NAME)
        print("DOUBAN_LIMIT:" + str(DOUBAN_LIMIT))
        new_readme = social.generate_douban(DOUBAN_NAME, DOUBAN_LIMIT, new_readme)

    if new_readme == old_readme:
        print("nothing changed")
    else:
        print("readme change, start update...")
        repo.update_file(path=contents.path, message=COMMIT_MESSAGE,
                         content=new_readme, sha=contents.sha)
        print("your readme update completed!")