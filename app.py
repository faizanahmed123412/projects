# app.py
from flask import Flask, request, jsonify
import google.generativeai as genai
import os
import re
from flask_cors import CORS

# Setup
app = Flask(__name__)
CORS(app)

# Gemini API key
genai.configure(api_key="YOUR-GEMINI-API-KEY")

# Model
model = genai.GenerativeModel('models/gemini-2.0-flash')

# In-memory conversation history
conversation_history = []

@app.route("/ask", methods=["POST"])
def ask():
    try:
        user_input = request.json.get("text")
        mode = request.json.get("mode", "default")
        scenario = request.json.get("scenario", "")

        print("📥 Received from frontend:", user_input)
        if mode == "roleplay":
            prompt = (
                f"You are simulating a real-life roleplay scenario with a student. "
                f"Scenario: {scenario}\n"
                f"Ask follow-up questions and help them speak more. Keep it friendly and simple.\n\n"
                f"Student: {user_input}"
            )
        else:
            prompt = (
                "You are a friendly AI tutor for children. "
                "Explain clearly, step-by-step and use simple language.\n\n"
                f"Student said: {user_input}"
            )


        response = model.generate_content(prompt)
        gemini_text = response.text.strip()

        cleaned_response = re.sub(r'[*_`#]', '', gemini_text)

        # Save to history
        conversation_history.append({
            "user": user_input,
            "gemini": cleaned_response
        })

        return jsonify({"response": cleaned_response})

    except Exception as e:
        print("❌ Error:", e)
        return jsonify({"error": str(e)}), 500

@app.route("/history", methods=["GET"])
def get_history():
    return jsonify(conversation_history)

if __name__ == "__main__":
    app.run(debug=True)
