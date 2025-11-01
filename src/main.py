import streamlit as st

from scrapper import google_search
from form import search_form
from list_view import list_view

from typing import Any, Dict, Optional


def main():
    form_values: Optional[Dict[str, str]] = search_form()
    data: Dict[str, Any] = google_search(form_values)

    if not data:
        return

    list_view(data.get("items", []))


if __name__ == "__main__":
    main()
