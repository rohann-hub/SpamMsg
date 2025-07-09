<!-- GitHub-Compatible README HTML -->

<h1 align="center">💬 WhatsApp Web Spam Bot using Python + PyAutoGUI</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?logo=python" />
  <img src="https://img.shields.io/badge/Library-pyautogui-yellow?logo=python" />
  <img src="https://img.shields.io/badge/Platform-WhatsApp_Web-green?logo=whatsapp" />
  <img src="https://img.shields.io/badge/Automation-Keyboard/Mouse-red?logo=python" />
</p>

<p align="center">
  <strong>🚀 A fun Python script that sends spam messages to any WhatsApp Web chat using GUI automation via <code>pyautogui</code>.</strong>
</p>

<hr>

<h2>✅ Features</h2>
<ul>
  <li>💥 Automates keyboard typing and sending messages</li>
  <li>📱 Works on any chat opened in WhatsApp Web</li>
  <li>⌛ Gives you time to manually click on a chat</li>
  <li>🧠 Uses <code>pyautogui</code> for cross-platform automation</li>
</ul>

<hr>

<h2>📦 Requirements</h2>
<ul>
  <li>Python 3.6 or higher</li>
  <li><code>pyautogui</code> installed</li>
</ul>

<p>
  <a href="https://pypi.org/project/pyautogui/" target="_blank">
    <img src="https://img.shields.io/badge/pip%20install-pyautogui-orange?logo=pypi" />
  </a>
  <pre><code>pip install pyautogui</code></pre>
</p>

<hr>

<h2>🚀 How to Use</h2>

<pre><code># 1. Clone the repo or copy the script
git clone https://github.com/your-username/whatsapp-spammer
cd whatsapp-spammer

# 2. Install required package
pip install pyautogui

# 3. Run the bot
python spam.py
</code></pre>

<p>
  🔹 The script gives you <strong>10 seconds</strong> to switch to your browser and click a WhatsApp chat.<br>
  🔹 Then it starts sending the message multiple times.
</p>

<hr>

<h2>💡 How It Works</h2>

<pre><code>import pyautogui
import time

message = "🔥 Spam message from Python!"
count = 10

time.sleep(10)  # Give user time to open chat
for i in range(count):
    pyautogui.typewrite(message)
    pyautogui.press("enter")
    time.sleep(0.1)
</code></pre>

<hr>

<h2>⚠️ Disclaimer</h2>
<ul>
  <li>This tool is for educational and fun purposes only.</li>
  <li>Do not use it to harass or spam others. Use responsibly.</li>
  <li>Works only if WhatsApp Web is open and focused.</li>
</ul>

<hr>

<h2>📁 File Structure</h2>

<pre><code>.
├── spam.py
├── README.md
</code></pre>

<hr>

<p align="center">
  ⭐ If you liked this project, give it a star on GitHub ⭐
</p>
