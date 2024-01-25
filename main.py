import streamlit as st
import langchain_helper as gh

st.title("🍲 Monthly Grocery Planner")

family_size = st.sidebar.slider("How many members are in your family?", 1, 10)

dietary_preferences = st.sidebar.multiselect(
    "Select your dietary preferences",
    options=["Vegetarian", "Non-Vegetarian", "Vegan", "Gluten-Free", "Dairy-Free"],
)

with st.sidebar:
    api_key = st.text_input("API Key", key="grocery_planner_api_key", type="password")

if family_size and dietary_preferences:
    if not api_key:
        st.info("Please add your API key to continue.")
        st.stop()
    response = gh.generate_grocery_list(family_size, dietary_preferences, api_key)
    st.text(response['grocery_list'])