import requests


def cat_status_code(status_code: str) -> None | str:
    """ Request image from HTTP Cat API """

    # Contact API
    try:
        url = f"https://http.cat/{status_code}.jpg"
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        return None

    # Parse response
    try:
        return url
    except (KeyError, TypeError, ValueError):
        return None
