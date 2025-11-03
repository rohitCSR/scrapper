from typing import Any, Dict, Optional

import streamlit as st

from src.scrapper import google_search
from src.form import search_form
from src.list_view import list_view


def main():
    st.write(":gray[ATS domain-based job search using Google dorks.]")
    form_values: Optional[Dict[str, str]] = search_form()
    data: Dict[str, Any] = google_search(form_values)

    if not data:
        return

    list_view(data.get("items", []))


if __name__ == "__main__":
    main()
