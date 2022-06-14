from datetime import datetime

import requests


class Nasa:

    @staticmethod
    def get_nasa_picture(token, description=False):
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
            result = {
                'img': get["url"],
                'title': get["title"],
            }
            if description:
                result['explanation'] = get["explanation"]

            return result

        except (KeyError, TypeError, ValueError):
            return None
