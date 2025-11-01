import requests
import json

from config import app_config


def google_search():
    query = 'site:greenhouse.io "software engineer" "Bangalore" -senior -staff -lead'
    results = requests.get(
        app_config.search_api_base_url,
        params={
            "key": app_config.google_search_api_key,
            "cx": app_config.search_engine_id,
            "q": query,
        },
    )
    return results.json()
