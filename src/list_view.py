import streamlit as st


def list_view(items: list):
    st.text("Search Results")

    if not items:
        st.info("No job results found.")
        return

    for item in items:
        with st.container():
            url: str = item.get("link")
            st.markdown(
                f"<a href='{item.get('link')}' target='_blank' style='text-decoration: none; color: #3d9df3; font-size: 16px;'>{item.get('htmlTitle')}</a>",
                unsafe_allow_html=True,
            )
            snippet = item.get("htmlSnippet")
            if snippet:
                st.markdown(snippet, unsafe_allow_html=True)
            st.markdown("---")
