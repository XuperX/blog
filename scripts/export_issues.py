import os
import requests
from pathlib import Path
import markdown  # pip install markdown

REPO = "XuperX/blog"
TOKEN = os.getenv("GH_TOKEN")

PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = PROJECT_ROOT / "docs"
INDEX_HTML_PATH = PROJECT_ROOT / "index.html"

def markdown_to_html(md_text):
    return markdown.markdown(md_text, extensions=['fenced_code', 'codehilite'])

def issue_to_markdown(issue):
    number = issue["number"]
    title = issue["title"]
    body_md = issue.get("body") or ""

    md_filename = OUTPUT_DIR / f"issue-{number}.md"
    with open(md_filename, "w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n{body_md}")

def fetch_issues():
    if not TOKEN:
        raise ValueError("Missing GH_TOKEN environment variable.")

    headers = {"Authorization": f"token {TOKEN}"}
    url = f"https://api.github.com/repos/{REPO}/issues?state=open"
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    return res.json()

def save_issue_as_html(issue):
    number = issue["number"]
    title = issue["title"]
    body_md = issue.get("body") or ""
    body_html = markdown_to_html(body_md)

    filename = f"issue-{number}.html"
    with open(OUTPUT_DIR / filename, "w", encoding="utf-8") as f:
        f.write(f"""<html>
<head>
    <title>{title}</title>
    <link rel="stylesheet" href="../css/style.css">
</head>
<body>
    <a href="../index.html" class="back-link">← Back to Home</a>
    <h1>{title}</h1>
    {body_html}
    <a href="../index.html" class="back-link">← Back to Home</a>
</body>
</html>
""")
    return filename, title

def update_index_html(new_links):
    """Replace links between markers in index.html."""
    if not INDEX_HTML_PATH.exists():
        raise FileNotFoundError("index.html not found at project root.")

    with open(INDEX_HTML_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    start_marker = "<!-- ISSUES_START -->"
    end_marker = "<!-- ISSUES_END -->"

    if start_marker not in content or end_marker not in content:
        raise ValueError(f"Markers '{start_marker}' and/or '{end_marker}' not found in index.html. Please add them.")

    start_idx = content.index(start_marker) + len(start_marker)
    end_idx = content.index(end_marker)

    updated_content = (
        content[:start_idx] +
        "\n" + "\n".join(new_links) + "\n" +
        content[end_idx:]
    )

    with open(INDEX_HTML_PATH, "w", encoding="utf-8") as f:
        f.write(updated_content)

def main():
    OUTPUT_DIR.mkdir(exist_ok=True)
    issues = fetch_issues()
    index_links = []

    for issue in issues:
        issue_to_markdown(issue)
        filename, title = save_issue_as_html(issue)
        rel_path = f"docs/{filename}"
        index_links.append(f'<li><a href="{rel_path}">{title}</a></li>')

    update_index_html(index_links)

    (OUTPUT_DIR / ".nojekyll").write_text("")

if __name__ == "__main__":
    main()
