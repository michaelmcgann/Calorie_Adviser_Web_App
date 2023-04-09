import requests
from selectorlib import Extractor


class Temperature:

    def __init__(self, country, city):
        self.country = country
        self.city = city

    def get(self):

        """gets users local temperature"""

        response = requests.get(f'https://www.timeanddate.com/weather/{self.country}/{self.city}')
        content = response.text
        extractor = Extractor.from_yaml_file('temperature.yaml')
        result = int(extractor.extract(content)['temp'].split()[0])

        return result



