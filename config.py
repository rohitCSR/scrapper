import os


class Config:
    def __init__(self):
        self.SEARCH_API_BASE_URL = "https://www.googleapis.com/customsearch/v1"
        self.SEARCH_ENGINE_ID = os.getenv("SEARCH_ENGINE_ID")
        self.GOOGLE_SEARCH_API_KEY = os.getenv("GOOGLE_SEARCH_API_KEY")

    @property
    def search_api_base_url(self):
        return self.SEARCH_API_BASE_URL

    @property
    def search_engine_id(self):
        return self.SEARCH_ENGINE_ID

    @property
    def google_search_api_key(self):
        return self.GOOGLE_SEARCH_API_KEY


app_config = Config()
