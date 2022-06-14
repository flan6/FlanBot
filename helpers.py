from datetime import datetime

import requests


def get_nasa_picture(token):
    """ Access NASA API and retrive the picture of the day """

    # Contact API
    try:
        url = f"https://api.nasa.gov/planetary/apod?api_key={token}"
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        return None

    # Parse response
    try:
        get = response.json()
        return {
            'img': get["url"],
            'title': get["title"],
            'date': datetime.strptime(get["date"], '%Y-%m-%d'),
            'explanation': get["explanation"]
        }
    except (KeyError, TypeError, ValueError):
        return None
