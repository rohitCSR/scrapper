import streamlit as st


def search_form():
    with st.container(horizontal=True, vertical_alignment="bottom"):
        position = st.text_input("Position")
        site = st.selectbox(
            "Choose site", options=["greenhouse.com", "jobs.lever.co", "glassdoor.com"]
        )
        location = st.selectbox(
            "Choose location",
            options=["Bengaluru", "Pune", "Mumbai", "Gurugram"],
        )
        submit_button = st.button("Search", use_container_width=True)

        if submit_button:
            return {"position": position, "site": site, "location": location}
        return None
