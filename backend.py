import requests

API_KEY = "ENTER YOUR API KEY"


def get_data(place, forecast_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}" 
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    values = 8 * forecast_days
    filtered_data = filtered_data[:values]
    return filtered_data

if __name__ == "__main__":
    print(get_data(place="New York", forecast_days=3))
