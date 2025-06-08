import os
import requests
from pathlib import Path
from html import escape

REPO = "XuperX/blog"
TOKEN = os.getenv("GH_TOKEN")
OUTPUT_DIR = Path("docs")

def markdown_to_html(md_text):
    # Optional: Use real markdown parser like markdown2
    return "<pre>" + escape(md_text) + "</pre>"

def main():
    if not TOKEN:
        raise ValueError("Missing GITHUB_TOKEN environment variable.")

    OUTPUT_DIR.mkdir(exist_ok=True)
    headers = {"Authorization": f"token {TOKEN}"}
    url = f"https://api.github.com/repos/{REPO}/issues?state=open"
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    issues = res.json()

    index_links = []

    for issue in issues:
        number = issue["number"]
        title = escape(issue["title"])
        body = markdown_to_html(issue["body"] or "")
        filename = f"issue-{number}.html"
        index_links.append(f'<li><a href="{filename}">{title}</a></li>')

        with open(OUTPUT_DIR / filename, "w", encoding="utf-8") as f:
            f.write(f"<html><head><title>{title}</title></head><body>")
            f.write(f"<h1>{title}</h1>")
            f.write(body)
            f.write("</body></html>")

    with open(OUTPUT_DIR / "index.html", "w", encoding="utf-8") as f:
        f.write("<html><head><title>Xure Blog</title></head><body>")
        f.write("<h1>Blog Posts</h1><ul>")
        f.write("".join(index_links))
        f.write("</ul></body></html>")

    # Disable Jekyll
    (OUTPUT_DIR / ".nojekyll").write_text("")

if __name__ == "__main__":
    main()
