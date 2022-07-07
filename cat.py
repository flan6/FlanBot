import requests


def cat_status_code(status_code: str) -> None | str:
    """ Request image from HTTP Cat API """

    try:
        url = f"https://http.cat/{status_code}.jpg"
        response = requests.get(url)
        response.raise_for_status()
        return url
    except (requests.RequestException, KeyError, TypeError, ValueError):
        return None
