import pandas as pd
import requests


def tidy_format(record: dict) -> dict[str, str | float]:
    """Turn a nested yr forecast record into a flat one-level dict"""
    tidy_dict = {"time": record["time"]}
    for section, sub_dict in record["data"].items():
        for _, fields in sub_dict.items():
            for sub_key, value in fields.items():
                if section == "instant":
                    key = sub_key
                else:
                    key = f"{section}_{sub_key}"
                tidy_dict[key] = value
    return tidy_dict


def locate_city(city: str, country: str = "Norway") -> tuple[float, float]:
    """return (lat, long) for a city"""
    r = requests.get(
        "https://geocode.maps.co/search",
        params={"city": city, "country": country},
    )
    matches = r.json()
    if len(matches) < 1:
        raise ValueError(f"No match for {city}, {country}")

    location = matches[0]
    return (float(location["lat"]), float(location["lon"]))


def city_forecast(city: str, country: str = "Norway") -> pd.DataFrame:
    """Given a city name, return a DataFrame of the weather forecast

    1. resolves gps for city
    2. fetches forecast
    3. tidies data
    4. wraps in DataFrame
    """
    lat, lon = locate_city(city, country)
    url = "https://api.met.no/weatherapi/locationforecast/2.0/compact"
    r = requests.get(
        url,
        params={"lat": lat, "lon": lon},
        headers={
            "User-Agent": "uio-in3110 https://github.com/uio-in3110/uio-in3110.github.io"
        },
    )
    tidy_records = [
        tidy_format(record) for record in r.json()["properties"]["timeseries"]
    ]
    df = pd.DataFrame.from_dict(tidy_records)
    df["time"] = pd.to_datetime(df["time"])
    # clean symbols
    for n in (1, 6, 12):
        df[f"next_{n}_hours_symbol_code"] = df[f"next_{n}_hours_symbol_code"].str.split(
            "_", n=1, expand=True
        )[0]
    # df = df.set_index("time")
    df["city"] = city
    return df
