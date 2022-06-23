from typing import Union

import requests


class Nasa:

    @staticmethod
    def get_nasa_picture(token: str) -> Union[None, dict]:
        """ Access NASA API and retrieve the picture of the day """

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
                'explanation': get["explanation"]
            }
        except (KeyError, TypeError, ValueError):
            return None
