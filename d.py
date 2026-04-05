import requests
import json
from datetime import datetime

class WeatherAnalyzer:
    def __init__(self, city):
        self.city = city
        self.api_key = "a87b4d98ae40c1e03962c3d44a15543e"  # Your new valid API key
        self.data = []

    def fetch_weather(self):
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={self.city}&appid={self.api_key}&units=metric"
        response = requests.get(url)

        if response.status_code == 200:
            self.data = response.json()["list"]
            print("✅ Data fetched successfully!")
        else:
            print("❌ Error fetching data")
            print("Status Code:", response.status_code)
            print("Response:", response.text)
            self.data = []  # Ensure data is empty on failure

    def save_to_file(self):
        if self.data:
            with open("weather_data.json", "w") as file:
                json.dump(self.data, file, indent=4)
            print("💾 Data saved to file!")
        else:
            print("⚠️ No data to save, skipping file write.")

    def load_from_file(self):
        try:
            with open("weather_data.json", "r") as file:
                self.data = json.load(file)
            print("📂 Data loaded from file!")
        except FileNotFoundError:
            print("⚠️ No saved data found.")

    def analyze(self):
        if not self.data:
            print("⚠️ No data to analyze.")
            return

        temps = [entry["main"]["temp"] for entry in self.data]
        avg_temp = sum(temps) / len(temps)
        max_temp = max(temps)
        min_temp = min(temps)

        print("\n📊 Weather Analysis:")
        print(f"Average Temp: {avg_temp:.2f}°C")
        print(f"Max Temp: {max_temp:.2f}°C")
        print(f"Min Temp: {min_temp:.2f}°C")

    def hottest_time(self):
        if not self.data:
            print("⚠️ No data available for hottest time.")
            return

        hottest = max(self.data, key=lambda x: x["main"]["temp"])
        time = datetime.fromtimestamp(hottest["dt"])
        temp = hottest["main"]["temp"]

        print(f"\n🔥 Hottest time: {time} with {temp}°C")


# 🚀 Run program
if __name__ == "__main__":
    city = input("Enter city: ")
    app = WeatherAnalyzer(city)

    app.fetch_weather()
    app.save_to_file()
    app.analyze()
    app.hottest_time()