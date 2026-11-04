import requests

url = "https://api.open-meteo.com/v1/forecast"
params = {
"latitude": 25.03,
"longitude": 121.56,
"current": "temperature_2m",
"timezone": "Asia/Taipei"
}

response = requests.get(url, params=params, timeout=10)
response.raise_for_status()
data = response.json()
print(data)

current=data["current"]
temperature=current["temperature_2m"]
print(f"現在在緯度 {params['latitude']}，經度 {params['longitude']} 的溫度為 {temperature}°C")