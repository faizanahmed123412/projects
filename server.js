// server.js
const express = require("express");
const axios = require("axios");
const cors = require("cors");

const app = express();
app.use(cors());
app.use(express.json());

const PYTHON_API_URL = "http://127.0.0.1:5000/ask";

app.post("/api/ask", async (req, res) => {
  try {
    const { text } = req.body;
    const response = await axios.post(PYTHON_API_URL, { text });
    res.json(response.data);
  } catch (error) {
    console.error("❌ Node error:", error.message);
    res.status(500).json({ error: "Server error" });
  }
});

app.listen(3000, () => {
  console.log("🚀 Node.js server running at http://localhost:3000");
});
