import streamlit as st
import requests

st.title("GitHub Profile Viewer")

username = st.text_input(
    label="GitHub Username",
    value="techzonelearning",
    placeholder="Enter GitHub username"
)

API = f"https://api.github.com/users/{username}"

if st.button("Fetch Profile"):
    response = requests.get(API)

    if response.status_code == 200:
        data = response.json()

        avatar_url = data.get("avatar_url")
        bio = data.get("bio")
        name = data.get("name")

        if avatar_url:
            st.image(avatar_url, width=150)

        if name:
            st.subheader(name)

        if bio:
            st.write(bio)
        else:
            st.info("This user has no bio/description.")
            
    elif response.status_code == 404:
        st.error("User not found. Please check the username.")
    else:
        st.error("Something went wrong")