import streamlit as st
import random

st.set_page_config(
    page_title="Number Guessing Game By Javeria Jamal",
)

st.title("Number Guessing Game By Javeria Jamal")

# Ensure ranges exist in session state
if 'start_range' not in st.session_state:
    st.session_state.start_range = 1
if 'end_range' not in st.session_state:
    st.session_state.end_range = 10
if 'random_number' not in st.session_state:
    st.session_state.random_number = None

# User selects range
start_range = st.number_input("Range of numbers from:", min_value=1, format="%d", step=1, key="start_range_input")
end_range = st.number_input("to:", min_value=start_range + 1, format="%d", step=1, key="end_range_input")

# Confirm range and generate a random number
if st.button("Confirm range"):
    st.session_state.start_range = start_range
    st.session_state.end_range = end_range
    st.session_state.random_number = random.randint(start_range, end_range)
    st.success(f"Number range set from {start_range} to {end_range}. Start guessing!")

# Ensure a number is generated before guessing
if st.session_state.random_number is None:
    st.warning("Please set the range first!")
else:
    user_guess = st.number_input("Guess the number:", min_value=start_range, max_value=end_range, format="%d", step=1, key="guess_input")

    if st.button("Confirm Guess"):
        if user_guess < st.session_state.random_number:
            st.warning("Your guess is a little low!")
        elif user_guess > st.session_state.random_number:
            st.warning("Your guess is a little high!")
        else:
            st.success("Bravo! You guessed the correct number!")
            # Reset the random number for a new game
            st.session_state.random_number = None




        
