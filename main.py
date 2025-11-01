import streamlit as st

from scrapper import google_search


def main():
    results = google_search()
    st.write(results)


if __name__ == "__main__":
    main()
