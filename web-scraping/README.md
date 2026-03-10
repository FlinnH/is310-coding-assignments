# Sakamoto Days — Fandom Wiki Character Scraper

## Wiki Chosen

**Wiki:** Sakamoto Days Fandom Wiki  
**Page scraped:** https://sakamoto-days.fandom.com/wiki/List_of_Characters  
**Robots.txt:** https://sakamoto-days.fandom.com/robots.txt  
**Content license:** CC-BY-SA

---

## Terms of Service & robots.txt

The `robots.txt` file at `https://sakamoto-days.fandom.com/robots.txt` was reviewed before scraping:

- `User-agent: *` — all crawlers are permitted by default
- `Allow: /wiki/*` — wiki article pages are explicitly allowed, which covers the List of Characters page used here
- `Disallow: /wiki/Special:` — Special: pages are off-limits and are **not** accessed by this script
- Content is published under a **CC-BY-SA license**, which permits use with attribution

This script complies with all stated rules.

---

## Why Sakamoto Days?

Sakamoto Days is **one of my favorite** manga/anime series! It's about a legendary assassin turned convenience store owner. The series features a large cast of characters organized into factions and groups — the [List of Characters](https://sakamoto-days.fandom.com/wiki/List_of_Characters) page on the fandom wiki catalogs every character alongside the group they belong to.

### What is being scraped?

For each character on the page, I create the the script to collects:

- `group_name` - the faction or group the character belongs to (e.g. "Sakamoto's Group", "JAA")
- `member_name` — the character's full name (e.g. "Taro Sakamoto", "Shin Asakura")

### Why might this data interest researchers (besides the fan like me)?

- **Network and social analysis** — the group/member structure maps directly onto a social network. Researchers studying character relationships in manga or anime could use this as a starting point for graph-based analysis.
- **Fandom documentation practices** — comparing how a newer series (Sakamoto Days began in 2020) documents its characters vs. a long-running series reveals how fan wikis grow and stabilize over time.
- **Narrative structure** — faction membership data can be used to study how stories organize characters into in-groups and out-groups, a common subject in media and narrative studies.

---

## Requirements

- Python 3.7+
- `cloudscraper` (used instead of plain `requests` which gives me **error** because fandom wikis are protected by Cloudflare, which blocks standard `requests.get()` calls with a 403 error)
- `beautifulsoup4`

Install dependencies with your virtual environment active:

```bash
pip install cloudscraper beautifulsoup4
```

---

## How to Run

```bash
source .is310-venv/bin/activate   # Mac/Linux

python3 fandom_wiki_scraping.py
```

The script will print progress to the terminal and save the output CSV in the same directory.

---

## Output

The script produces `sakamoto_days_characters.csv` with the following columns:

| Column | Description | Example |
|---|---|---|
| `group_name` | The faction the character belongs to | `Sakamoto's Group` |
| `member_name` | The character's full name | `Taro Sakamoto` |

Sample output:

```
group_name,member_name
Sakamoto's Group,Taro Sakamoto
Sakamoto's Group,Shin Asakura
JAA,Lu Xiaotang
```

---

### Thank you!


