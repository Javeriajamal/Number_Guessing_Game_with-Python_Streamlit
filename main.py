'''
import streamlit as st
import random

st.set_page_config(
    page_title="Number Guessing Game By Javeria Jamal",
)

st.title("Number Guessing Game-By Javeria Jamal!")

if 'random_number' not in st.session_state:
     st.session_state.random_number = 0

# Range of Guessing numbers

st.session_state.start_range = st.number_input("Range of numbers from: ",format="%d",step=1,key=1)
st.session_state.end_range  = st.number_input("to: ",format="%d",step=1,min_value=st.session_state.start_range+5,key=2)

if 'start_range_with_random' not in st.session_state and  'end_range_with_random' not in st.session_state: 
    st.session_state.start_range_with_random = 0
    st.session_state.end_range_with_random = 5

# Confirm the number of range and generating random number

if st.button("Confirm range"):
    st.session_state.generate_random_number=random.randint(st.session_state.start_range,st.session_state.end_range)
    st.session_state.start_range_with_random = st.session_state.start_range
    st.session_state.end_range_with_random = st.session_state.end_range


#generate_random_number = random.randint(1,100)

def guessing_check(user_input:int, generate_random_number:int,start_range:int,end_range:int):
        if(user_input<start_range):
            st.write("Your guess is lower than range")
        elif(user_input>end_range):
            st.write("Your guess is higher than range")

user_input: int = int(st.number_input("Guess the number:" ,format="%d",step=1,key=3))

if st.button("Confirm Guess"):
        if user_input < generate_random_number:
             st.warning("Your guess is a little low!")
        elif user_input > generate_random_number:
             st.warning("Your guess is a little high!")
        else:
             st.success("Bravo! You guessed the correct number!")
'''

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




        
