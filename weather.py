import requests
import sys
import os

def test_weather_api(api_key, location="London"):
    """Test if the Weather API is working"""
    try:
        # Configure console output for Windows
        if sys.stdout.encoding != 'utf-8':
            import io
            sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
        
        # Step 1: Geocoding API call
        geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={location}&limit=1&appid={api_key}"
        geo_response = requests.get(geo_url)
        geo_response.raise_for_status()
        geo_data = geo_response.json()
        
        if not geo_data:
            print(f"[ERROR] Geocoding failed for {location}")
            return False
        
        lat, lon = geo_data[0]['lat'], geo_data[0]['lon']
        
        # Step 2: Weather API call
        weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
        weather_response = requests.get(weather_url)
        weather_response.raise_for_status()
        weather_data = weather_response.json()
        
        if weather_data.get('cod') != 200:
            print(f"[ERROR] Weather API failed. Response: {weather_response.text[:100]}...")
            return False
        
        # Print results (using ASCII characters only)
        print(f"[SUCCESS] API is working! Current weather in {location}:")
        print(f"- Temperature: {weather_data['main']['temp']}°C")
        print(f"- Conditions: {weather_data['weather'][0]['description']}")
        print(f"- Humidity: {weather_data['main']['humidity']}%")
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] API request failed: {str(e)[:100]}")
        return False
    except (KeyError, IndexError) as e:
        print(f"[ERROR] Unexpected response format: {e}")
        return False

# Your API key here
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY") # Replace with your actual API key as a string with "os.getenv("NEWS_API_KEY")"

# Test the API
test_weather_api(WEATHER_API_KEY)