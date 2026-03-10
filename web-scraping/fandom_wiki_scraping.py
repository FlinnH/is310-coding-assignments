# imports
from bs4 import BeautifulSoup
import cloudscraper
import csv
import os

URL = "https://sakamoto-days.fandom.com/wiki/List_of_Characters"
OUTPUT_FILE = "sakamoto_days_characters.csv"

# Create one cloudscraper instance to reuse for all requests
scraper = cloudscraper.create_scraper()

def fetch_page(url):
    response = scraper.get(url, timeout=10)
    return response

# Parse the characters from the response
def parse_characters(response):
    soup = BeautifulSoup(response.text, "html.parser")
    characters = []

    # Find all top-level portal divs — each one is a group block
    portals = soup.find_all("div", class_="portal")
    print(f"\nFound {len(portals)} portal block(s) on the page.")

    for portal in portals:

        # Get the group name 
        # The navbox div with class "sakadays-head" holds the group label
        navbox = portal.find("div", class_="sakadays-head")
        if not navbox:
            continue 

        # .get_text(strip=True) pulls out just the text, removing tags and whitespace
        group_name = navbox.get_text(strip=True)

        if not group_name:
            continue

        # Get all members in this group 
        # Each member card has a div.portal-caption containing a link
        captions = portal.find_all("div", class_="portal-caption")

        for caption in captions:
            # The member name is the text inside the <a> tag
            link = caption.find("a")
            if not link:
                continue

            member_name = link.get_text(strip=True)
            if not member_name:
                continue

            characters.append({
                "group_name":  group_name,
                "member_name": member_name,
            })

    print(f"Total characters extracted: {len(characters)}\n")
    return characters

# Save the results to a CSV file
def save_to_csv(characters, filename):
    filepath = os.path.abspath(filename)

    with open(filepath, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        # header row
        writer.writerow(["group_name", "member_name"]) 
        for character in characters:
            writer.writerow([character["group_name"], character["member_name"]])

    print(f"Saved to: {filepath}")
    print(f"Total rows: {len(characters)}")

# Preview the results
def preview_results(characters, n=10):
    print(f"Preview: First {n} entries")
    for character in characters[:n]:
        print(f"  {character['group_name']:<30}  {character['member_name']}")

def main():
    print("Sakamoto Days — Character List Scraper")

    response = fetch_page(URL)
    characters = parse_characters(response)
    preview_results(characters)
    save_to_csv(characters, OUTPUT_FILE)

if __name__ == "__main__":
    main()