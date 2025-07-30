def send_alert(summary, result):
    print("\n[SIMULATED WHATSAPP/EMAIL]")
    print("Summary:", summary)
    print("Match Result:", result['match_result'], f"({result['match_score']}%)")
