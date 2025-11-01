import streamlit as st


def list_view(items: list):
    st.text("Search Results")

    if not items:
        st.info("No job results found.")
        return

    for item in items:
        with st.container():
            st.markdown(f"### [{item.get('title')}]({item.get('link')})")
            st.markdown(f"**Company:** {item.get('displayLink', 'N/A')}")
            snippet = item.get("snippet")
            if snippet:
                st.write(snippet)
            url = item.get("link")
            st.markdown(f"[Apply Here]({url})", unsafe_allow_html=True)
            st.markdown("---")
