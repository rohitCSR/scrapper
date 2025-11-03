.PHONY: app

app:
	. ./.env && streamlit run main.py
