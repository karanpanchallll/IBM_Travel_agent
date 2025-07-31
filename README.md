# 🧭 AI Travel Planner Agent

Plan your dream trip with the power of AI! This is an intelligent, Gemini-powered travel planner that creates personalized, day-wise itineraries based on your destination, budget, duration, and interests.

---

## ✨ Features

- 🌍 Personalized travel itineraries
- 💸 Budget-aware activity planning
- 🎯 Custom suggestions based on your interests
- 🤖 Powered by Google Gemini (Gemini Pro)
- 🖥️ Simple, interactive Streamlit web UI

---

## 📁 Project Structure

travel_planner_streamlit/
├── app.py # Main Streamlit app
├── .env # Stores your Gemini API key
├── requirements.txt # Python dependencies
└── README.md # Project documentation

yaml
Copy
Edit

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/travel_planner_streamlit.git
cd travel_planner_streamlit
2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Configure API Key
Create a .env file in the root directory and paste your Google Gemini API key:

env
Copy
Edit
GOOGLE_API_KEY=your_google_gemini_api_key_here
🔑 You can get your API key from Google AI Studio.

4. Run the App
bash
Copy
Edit
python -m streamlit run app.py
Then open the browser at: http://localhost:8501

🧪 Sample Input
Destination: Paris

Days: 5

Budget: ₹50,000

Interests: Museums, cafes, art, photography

🔒 Environment Variables
Variable	Description
GOOGLE_API_KEY	Your Google Gemini API key

📌 Future Scope
🌤️ Real-time weather API integration

✈️ Flights & hotels via travel APIs

🗺️ Interactive map & routes

📄 Downloadable PDF itineraries

👤 User login and saved trips

