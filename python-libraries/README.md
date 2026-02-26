# 🌍 Tasty Dishes Around The World - My CLI Data Entry Assignment

My command-line tool for collecting and saving people's favorite dishes from around the world. I Built with Python and my first time with the [Rich](https://rich.readthedocs.io/en/stable/) library for a clean, formatted terminal experience. First time working with this library so apologize if there's any potential issues.

---

## 📌 What It Does

This script allows users to:
- View a pre-loaded table of example dishes as a reference
- Enter one or more of their own favorite dishes interactively
- Review and confirm each entry before it is saved
- Export all confirmed entries to a timestamped `.csv` file

This script was built as part of a broader data curation project exploring food culture and immigrant cuisine transformations in the United States but **mostly due to my enormous love for food!**

---

## 🗂️ Fields Collected

| Field | Description | Example |
|---|---|---|
| `dish_name` | The name of the dish | Unagi |
| `origin_country` | The country the dish originates from | Japan |
| `contributor_nickname` | A made-up name for the contributor | Not A Weeb|
| `contributor_comment` | A brief personal comment about the dish | Whoever dislike eel need to try this... |

---

## ⚙️ Requirements

- Python 3.7 or higher
- The `rich` library

---

## 🚀 How to Install and Run

### 1a. Clone or download this repository

```bash
git clone <your-repo-url>
cd <your-repo-folder>
```
## 1b. Or just copy the code into a new .py file



### 2. Set up your virtual environment (recommended by professor)

```bash
python -m venv .is310-venv
```

Activate it:
- **Mac/Linux:** `source .is310-venv/bin/activate`
- **Windows:** `.is310-venv\Scripts\activate`

### 3. Install dependencies

```bash
pip3 install rich
```

### 4. Run the script
```bash
python [name of the script file].py
```


---

## 🖥️ How to Use It

Once the script is running, follow the on-screen prompts:

1. You'll first see a table of **example dishes** for reference
2. You'll be asked if you'd like to **add a dish** — type `yes` to proceed or `done` to exit without saving
3. Fill in each field when prompted
4. You'll see a **confirmation table** of what you entered — type `yes` if it looks correct, or `no` to re-enter
5. After confirming, you'll be asked if you want to **add another dish**
6. When you're done, all entries are saved to a `.csv` file

---

## 📄 Output

The script generates a `.csv` file named with a timestamp, for example:

```
favorite_dishes_20260226_143012.csv
```

It is saved in the **same folder** where you run the script. The file can be opened in Excel, Google Sheets, or any spreadsheet tool.

**Example output (as it appears in the CSV, shown here as a table):**

| dish_name | origin_country | contributor_nickname | contributor_comment |
|-----------|----------------|----------------------|---------------------|
| Pierogi | Poland | Dumplings4Ever | Soft and savory — perfect comfort food |
| Injera | Ethiopia | SpiceRoadTraveler | The sourdough flatbread that changed my life |

---

## 🗒️ Notes

- Please keep contributor nicknames appropriate and fun!
- Comments should be brief — a sentence or two is ideal
- Only publicly shareable data should be entered; do not include private or personal information
- The `.csv` file uses UTF-8 encoding to support special characters (e.g., `Bánh Cuốn`, `Börek`)
- The provided sample data will NOT be saved to csv file

---

## Thank you and happy eating 😋!