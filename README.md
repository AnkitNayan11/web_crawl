# Web Crawler / Review Extraction Project

This project is designed to scrape, convert, and clean product reviews using Python, Playwright, and OpenAI tools.

---

##  Python Environment

- **Recommended Python Version:** `Python 3.11`
- (Originally tested on `Python 3.9.23`, but newer version is used with conda)

---

##  Environment Setup

### 1. Create and activate virtual environment using Conda:

```bash
conda create -n aienv python=3.11
conda activate aienv

Install dependencies:
pip install -r requirements.txt
pip install playwright
playwright install


### 2. Project Folder Structure:

project_root/
│
├── config/                      # Configuration JSONs
│   ├── review_cleaning_config.json
│   └── md_to_txt_config.json
│
├── output/                      # Scraped and cleaned files
│   ├── scraped_files/
│   ├── scraped_files_txt/
│   └── cleaned_review/
│
├── webscraper_result/          # Final outputs (e.g., merged_reviews.md)
│
├── src/                         # Main source code
│   ├── run_converter.py
│   ├── run_cleaning.py
│   ├── programatic_login.py
│   ├── main.py
│   └── utils/                   # Utility functions
│       ├── md_to_txt_utils.py
│       ├── config_reader.py
│       └── openai_cleaner.py
│
├── product_page.html            # Input HTML
├── requirements.txt
└── README.md
