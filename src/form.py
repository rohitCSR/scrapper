import json

import streamlit as st

SITES_DATA = json.load(open("./src/job_sites.json", "r"))
SITES = [site["site"] for site in SITES_DATA]


def search_form():
    with st.container(horizontal=True, vertical_alignment="bottom"):
        position = st.text_input("Position")
        site = st.selectbox(
            "Choose site",
            options=SITES,
        )
        location = st.selectbox(
            "Choose location",
            options=["Bengaluru", "Pune", "Mumbai", "Gurugram"],
        )
        submit_button = st.button("Search", use_container_width=True)

        if submit_button:
            return {"position": position, "site": site, "location": location}
        return None
