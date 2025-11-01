.PHONY: app

app:
	. ./.env && streamlit run src/main.py