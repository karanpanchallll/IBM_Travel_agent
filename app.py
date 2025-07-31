import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Streamlit UI
st.set_page_config(page_title="🌍 AI Travel Planner", layout="wide")
st.title("✈️ AI Travel Planner Agent")

with st.sidebar:
    st.header("🧳 Plan Your Trip")
    destination = st.text_input("Destination", "Paris")
    days = st.slider("Trip Duration (in days)", 1, 21, 5)
    budget = st.number_input("Budget (₹)", value=50000)
    interests = st.text_area("Your Interests", "museums, food, beaches, shopping")
    submit = st.button("Plan My Trip")

# Gemini Prompt Template
def generate_itinerary(destination, days, budget, interests):
    prompt = f"""
    You are a smart travel planner agent.

    Plan a {days}-day trip to {destination} under a budget of ₹{budget}.

    The user is interested in: {interests}.

    Your response should be in the following format:
    - Day-wise itinerary with time slots.
    - Include 2–4 activities per day.
    - Add small notes for each activity (distance, time needed, entry fee if any).
    - Be realistic about travel time and budget.

    Make the output fun, personalized, and helpful.
    """
    
    model = genai.GenerativeModel("gemini-2.5-pro")
    response = model.generate_content(prompt)
    return response.text

# Display itinerary
if submit:
    with st.spinner("Generating your personalized travel plan..."):
        try:
            itinerary = generate_itinerary(destination, days, budget, interests)
            st.subheader(f"🗓️ Your {days}-Day Itinerary for {destination}")
            st.markdown(itinerary)
        except Exception as e:
            st.error(f"Failed to generate itinerary: {e}")
