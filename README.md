**🔐 PROJECT OVERVIEW**

This repository contains two educational Python-based tools: a **Keylogger** and an **Anti-Keylogger Detector**. The Keylogger captures keystrokes and sends them to a Telegram bot in real-time. The Anti-Keylogger detects suspicious processes and alerts users about potential keylogging behavior.

Both tools feature a simple and interactive GUI using Python’s `tkinter` module. 🎛️

---

**✨ KEY FEATURES**

🖥️ **KEYLOGGER**

* ⌨️ **Keystroke Logging** – Records all keyboard input from the system.
* 📩 **Telegram Integration** – Sends logs to a Telegram bot at set intervals.
* 🖼️ **GUI Interface** – Users can input bot credentials through an intuitive window.
* 🟢🔴 **Start/Stop Controls** – Start, stop, or clear logs using on-screen buttons.

🛡️ **ANTI-KEYLOGGER DETECTOR**

* 🔍 **Process Monitoring** – Scans system processes for potential keyloggers.
* ⚠️ **Real-Time Alerts** – Warns the user when suspicious activity is found.
* 📤 **Log Exporting** – Allows saving alerts and logs to a `.txt` file.
* 💻 **GUI Interface** – Provides controls to start/stop detection and view logs.

---

**📦 SYSTEM REQUIREMENTS**

Required Software:

* 🐍 Python 3.x

Required Python Libraries:

* `requests` 📡 – For Telegram communication
* `pynput` ⌨️ – For keystroke detection
* `psutil` 🛠️ – For process monitoring
* `tkinter` 🖥️ – For GUI (built-in on most systems)

Installation Command:
`pip install requests pynput psutil`

---

**🤖 TELEGRAM BOT SETUP**

1. Use **BotFather** to create a Telegram bot and obtain the token.
2. Retrieve your Telegram **chat ID**.
3. Launch the Keylogger GUI and input the token and chat ID to begin logging.

---

**▶️ HOW TO USE**

KEYLOGGER:

* Run the script `keylogger.py`
* Enter the bot token and chat ID
* Click **“Start Logging”** to begin keystroke monitoring
* Use **“Stop Logging”** to halt activity
* Press **“Clear Log”** to delete logs

ANTI-KEYLOGGER:

* Run the script `anti_keylogger.py`
* Click **“Start Detecting”** to initiate scanning
* Click **“Stop Detecting”** to stop it
* Use **“Export Logs”** to save detection data

---

**🧪 UNIT TESTING (OPTIONAL)**

To run tests for each component:

* `python -m unittest test_key_logger.py`
* `python -m unittest test_anti_keylogger.py`

These tests verify core functionalities of each module.

---

**⚖️ LEGAL AND ETHICAL NOTICE**

⚠️ **Important:**
The use of keyloggers can have serious **legal and ethical consequences**. This software is intended strictly for **educational purposes** and should only be used with the **explicit consent** of the user being monitored. Unauthorized usage may violate laws and result in criminal charges.

Always comply with applicable privacy laws and institutional policies.

---

**🙌 ACKNOWLEDGMENTS**

Special thanks to the maintainers of the following Python libraries:

* `pynput` 👨‍💻 – For keyboard input capture
* `psutil` ⚙️ – For process scanning
* `requests` 🌐 – For Telegram API communication
* `tkinter` 🧩 – For GUI creation

---

