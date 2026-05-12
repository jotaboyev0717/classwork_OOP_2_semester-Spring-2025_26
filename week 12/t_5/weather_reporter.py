import requests


class WeatherReporter:
    def __init__(self, api_url: str):
        self.api_url = api_url

    def get_report(self, city: str) -> str:
        response = requests.get(f"{self.api_url}/weather", params={"city": city})
        if response.status_code != 200:
            raise RuntimeError(f"Failed to fetch weather for {city}")
        data = response.json()
        return f"{city}: {data['temp']}°C, {data['condition']}"
