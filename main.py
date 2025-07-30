from resume_parser import extract_text
from matcher import match_job
from notifier import send_alert
from utils import get_user_consent, save_output, setup_logging
import os

def main():
    setup_logging()

    print("🔍 Welcome to the AI Resume Analyzer")
    print("====================================\n")

    if not get_user_consent():
        print("❌ Consent not given. Exiting.")
        return

    resume_path = input("📁 Enter path to resume (PDF or DOCX): ").strip()
    if not os.path.exists(resume_path):
        print("❌ File does not exist. Exiting.")
        return

    try:
        print("\n📄 Extracting resume text...")
        resume_text = extract_text(resume_path)

        print("📋 Loading job description...")
        with open("job_description.txt", "r") as f:
            job_desc = f.read()

        print("🧪 Matching FULL resume with job description...")
        result = match_job(resume_text, job_desc)

        summary = "Full resume content used for matching."

        print("💾 Saving output to JSON file...")
        save_output(summary, result)

        print("📢 Sending notification (simulated)...")
        send_alert(summary, result)

        print("\n✅ All done! Your resume has been matched successfully.")
        print("📂 Check the 'output' folder for the result JSON file.\n")

    except Exception as e:
        print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    main()
