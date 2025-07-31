# 🧠 SpeakGenie – AI Voice Tutor for Kids

SpeakGenie is a real-time AI-powered voice tutor designed for children aged 6–16. It helps students practice speaking, comprehension, and vocabulary using live conversation, interactive **Roleplay Scenarios**, and multi-language support.

---

## ✨ Features

- 🎙️ Real-time speech-to-text using Web Speech API
- 🌐 Multi-language support for Indian regional languages
- 🤖 Gemini-powered AI tutor responses
- 🧑‍🏫 Roleplay Mode (School, Store, Home, etc.)
- 📜 Conversation history tracking
- 🎨 Light/Dark theme toggle and interactive UI

---

## 🗂️ Folder Structure
SpeakGenie/
│
├── backend/
│ └── app.py
│
├── node/
│ └── server.js
│
├── frontend/
│ └── test.html
│
├── start_all.bat
├── README.md
└── requirements.txt


---

## 🧪 How to Run Locally

### 1️⃣ Backend (Python + Gemini)

#### Prerequisites
- Python 3.8+
- Your Google Gemini API Key

#### Setup Steps

```bash
cd backend
python -m venv venv         # Optional: Create virtual environment
source venv/bin/activate    # or venv\Scripts\activate on Windows

# Install packages
pip install -r requirements.txt
If requirements.txt is missing, use:


pip install flask flask-cors google-generativeai


Add Your API Key
In app.py, replace with your own key:


genai.configure(api_key="YOUR_API_KEY")


Run the Flask App

python app.py
Flask server will run at: http://127.0.0.1:5000

Node.js Server (Proxy for API calls)
Prerequisites
Node.js and npm installed

Setup Steps

cd node-server


npm install express axios cors


node server.js
Node server will run at: http://localhost:3000

Frontend (HTML + JavaScript)
No installation required. Just:

Open the frontend directly in your browser:

👉 **[Open test.html](frontend/test.html)**  
(Or drag and drop the file into Chrome)

Allow microphone permissions when prompted
Make sure all the things given below:
- Python and Node servers are running
---

## ⚡ One-Click Start (Windows)

To launch everything with a single double-click:

1. Locate the file: `start_all.bat`
2. Double-click it
3. It will:
   - Start the Python backend (Flask)
   - Start the Node.js proxy server
   - Open `test.html` in your default browser

🧠 Make sure:
- You have `Python`, `Node.js`, and required packages installed.
- Your terminal paths are configured (`python`, `node`, `npm`, etc.)

---

## 🛠 Optional (Mac/Linux Users)

Mac/Linux users can create a `start_all.sh`:

```bash
#!/bin/bash
echo "🧠 Starting SpeakGenie..."

# Start Python backend
gnome-terminal -- bash -c "cd backend && python3 app.py; exec bash"

# Start Node.js server
gnome-terminal -- bash -c "cd node && node server.js; exec bash"

# Open frontend
xdg-open frontend/test.html

echo "✅ All systems launched!"
Make it executable:

bash
Copy
Edit
chmod +x start_all.sh
Then run:

bash
Copy
Edit
./start_all.sh

Start interacting with the AI Tutor!

🌍 Supported Languages
Language	Code
English	en-US
Hindi	hi-IN
Tamil	ta-IN
Telugu	te-IN
Bengali	bn-IN
Gujarati	gu-IN
Kannada	kn-IN
Malayalam	ml-IN
Marathi	mr-IN
Punjabi	pa-IN
Urdu	ur-IN

Select your preferred language from the dropdown before starting.

🎭 Roleplay Mode (Practice Speaking!)
Students can practice conversations based on scenes:

🏫 At School
vbnet
Copy
Edit
AI: “Good morning! What’s your name?”
Student: “My name is Aarav.”
AI: “Hi Aarav! Do you like school?”
🛒 At the Store
vbnet
Copy
Edit
AI: “Welcome! What do you want to buy today?”
Student: “I want a banana.”
AI: “One banana coming right up!”
👨‍👩‍👧 At Home
vbnet
Copy
Edit
AI: “Who do you live with?”
Student: “I live with my parents.”
AI: “Nice! Do you help them at home?”
Use the Roleplay button in the interface to begin a guided scenario.

🗃️ Conversation History
All conversations are saved in memory during the session

You can fetch them via: GET http://127.0.0.1:5000/history

📝 Sharing Instructions
To share with others:

Zip the entire SpeakGenie/ folder

Send via email, Google Drive, or GitHub



👩‍💻 Credits
Developed using:

Google Gemini API (via Python Flask)

Node.js Proxy Server

Web Speech API (Browser)

HTML + CSS + JavaScript frontend

SpeakGenie is built to help kids learn language through fun, interactive, spoken conversations!

