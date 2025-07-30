import json
import os
import logging
from datetime import datetime

def get_user_consent():
    consent = input("Do you allow us to process your data? (yes/no): ").strip().lower()
    return consent == "yes"

def save_output(summary, result):
    os.makedirs("output", exist_ok=True)
    with open("output/result.json", "w") as f:
        json.dump({"summary": summary, "result": result}, f, indent=4)
    print("Output saved to output/result.json")

def setup_logging():
    os.makedirs("logs", exist_ok=True)
    logging.basicConfig(filename="logs/app.log", level=logging.INFO,
                        format="%(asctime)s - %(levelname)s - %(message)s")
