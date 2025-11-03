from typing import Any, Dict

import requests

from src.config import app_config


def google_search(data: Dict[str, Any]):
    if not data:
        return None

    query = f'site:{data["site"]} "{data["position"]}" "{data["location"]}"'  # -senior -staff -lead

    results = requests.get(
        app_config.search_api_base_url,
        params={
            "key": app_config.google_search_api_key,
            "cx": app_config.search_engine_id,
            "q": query,
        },
    )

    return results.json()
