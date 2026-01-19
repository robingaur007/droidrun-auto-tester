from droidrun import Droidrun
import time

def app_health_check():
    bot = Droidrun()

    print("Starting Mobile App Health Monitoring...")

    # Step 1: Launch app (example: Android Settings)
    bot.open_app("com.android.settings")
    time.sleep(3)

    # Step 2: Perform UI interactions
    bot.scroll(direction="down")
    time.sleep(2)
    bot.scroll(direction="up")
    time.sleep(2)

    # Step 3: Read screen content
    screen_text = bot.read_text()

    # Step 4: Health validation
    if screen_text and len(screen_text) > 20:
        status = "PASS"
        reason = "App responsive and UI loaded successfully"
    else:
        status = "FAIL"
        reason = "App unresponsive or UI not detected"

    # Step 5: Save health report
    with open("report.txt", "w") as f:
        f.write(f"APP HEALTH STATUS: {status}\n")
        f.write(f"DETAILS: {reason}\n")

    print("Health Check Result:", status)

    bot.close()

if __name__ == "__main__":
    app_health_check()
