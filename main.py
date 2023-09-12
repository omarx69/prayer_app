import requests

def fetch_prayer_time(city, country):
    
    url=f"http://api.aladhan.com/v1/timingsByCity?city={city}&country={country}&method=2"

    try:
        response = requests.get(url)
        info = response.json()
        if "data" in info:
            timings = info["data"]["timings"]
            return timings
        else:
            return None

    except Exception as e:
        return f"unexcepted error occurred {e}"
    

city = input("Enter your city: ")
country = input("Enter your country: ")

if city and country:
    prayer_timing=fetch_prayer_time(city, country)
    for name, time in prayer_timing.items():
        print(f"{name}:{time}")
else:
    print("unable to fetch prayer times :(")          