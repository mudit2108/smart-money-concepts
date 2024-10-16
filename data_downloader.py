import requests

def download_data(
    instrument: str,
    start_date: str,
    end_date: str,
    interval: str,
):
    url = f"https://api.upstox.com/v2/historical-candle/{instrument}/{interval}/{end_date}/{start_date}"
    data = requests.get(url).json()
    if data["status"] == "error":
        raise ValueError(data["errors"][0]["message"])
    response = []
    for candle in data["data"]["candles"]:
        response.append({
            "Date": candle[0],
            "open": candle[1],
            "high": candle[2],
            "low": candle[3],
            "close": candle[4],
            "volume": candle[5],
            "oi": candle[6],
        })
    return response