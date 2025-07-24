import os
from openai import OpenAI

from utils.config_reader import read_config
from utils.openai_cleaner import extract_reviews


def run_review_cleaning_process():
    # === Load config ===
    config = read_config("/Users/ankitnayan/Downloads/final_web_v1/web_crawl/config/review_cleaning_config.json")

    input_folder = config["input_folder"]
    output_json_path = config["output_json_path"]
    model = config["model"]
    temperature = config["temperature"]
    max_tokens = config["max_tokens"]

    # === Setup OpenAI ===
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable is not set.")
    client = OpenAI(api_key=api_key)

    # === Process Files ===
    all_reviews = []
    for filename in os.listdir(input_folder):
        if filename.endswith(".txt"):
            path = os.path.join(input_folder, filename)
            print(f" Processing {filename}")
            with open(path, "r", encoding="utf-8") as f:
                text = f.read()
                try:
                    reviews = extract_reviews(text, client, model, temperature, max_tokens)
                    print("Cleaned reviews", reviews)
                    all_reviews.extend(reviews)
                    print(f" Extracted {len(reviews)} reviews.")
                except Exception as e:
                    print(f" Failed to process {filename}: {e}")

    # === Save Output ===
    print(f"\n Saving {len(all_reviews)} reviews to {output_json_path}")
    with open(output_json_path, "w", encoding="utf-8") as f:
        import json
        json.dump(all_reviews, f, ensure_ascii=False, indent=2)
    print(" Done!")

