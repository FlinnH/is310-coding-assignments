# GETting Culture Across APIs Homework — Stranger Things x Europeana

## APIs Used
- **HawAPI** (Stranger Things): https://hawapi.theproject.id
- **Europeana**: https://pro.europeana.eu/page/apis

## Why HawAPI?

Because I'm a huge fan of *Stranger Things*? **Yes! Except for the finale** (fight me if you disagree 👊🏻)

Nonetheless, HawAPI is a free, open-source REST API. I chose it because it:
- Requires **NO** authentication for basic use, making it straightforward to work with as an introduction to APIs. 
- Has very clean and organized documentation.

My script fetches a list of **Stranger Things characters**, then searches the `Europeana` cultural heritage collection for items related to the first character returned.

## How to Run
1. Install dependencies:
```bash
pip install requests pyeuropeana python-dotenv Pillow
```
2. Fix numpy if needed: 
```bash
pip uninstall numpy
```
then
```bash
pip install "numpy==1.26.4"
```


3. Create a `.env` file in this folder with your Europeana API key: 
`EUROPEANA_API_KEY=your-key-here`


4. Run:
```bash
python3 getting_culture.py
```

## Output
Saves Europeana search results to `hawapi_europeana_data.json`.

## Important Notes
- `.env` is listed in `.gitignore` — My Europeana API key is never pushed to GitHub so **don't try to find it!**
- The script also filters out the API key from the Europeana response before saving the JSON file
