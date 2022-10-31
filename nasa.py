import requests


class Nasa:

    @staticmethod
    def get_nasa_picture(token: str) -> None | dict:
        """ Access NASA API and retrieve the picture of the day """

        try:
            url = f"https://api.nasa.gov/planetary/apod?api_key={token}"
            response = requests.get(url)
            response.raise_for_status()
            get = response.json()
            return {
                'img': get["url"],
                'title': get["title"],
                'explanation': get["explanation"],
            }
        except (requests.RequestException, KeyError, TypeError, ValueError):
            return None
