
from utils.md_to_txt_utils import convert_md_to_txt
from utils.config_reader import read_config



def run_md_to_txt_conversion_process():
    # === Load config ===
    config = read_config("/Users/ankitnayan/Downloads/final_web_v1/web_crawl/config/md_to_txt_config.json")
    print("Config read completed")
    
    # === Convert Markdown to Text ===
    convert_md_to_txt(config["source_folder"], config["destination_folder"])
    print("Conversion from md to txt completed")
