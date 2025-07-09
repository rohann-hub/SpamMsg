import pyautogui
import time

# Message and count
message = "🔥 Spam message from Python!"
count = 10  # Number of messages to send

print("⏳ You have 10 seconds to open WhatsApp Web and click the chat...")
time.sleep(10)  # Wait so user can click on a WhatsApp chat

for i in range(count):
    pyautogui.typewrite(message)
    pyautogui.press("enter")
    print(f"✅ Sent {i+1}")
    time.sleep(0.1)  # Optional: reduce this to spam faster (0.05 or 0.01)
