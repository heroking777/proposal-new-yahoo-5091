import csv
import requests
from datetime import datetime

# Define the API endpoint and your credentials
API_ENDPOINT = "https://api.yahoo.co.jp/auction/v1/user/bids"
YOUR_API_KEY = "your_api_key_here"

# Function to fetch auction bid history from Yahoo!オークション API
def fetch_auction_bids(api_key):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    response = requests.get(API_ENDPOINT, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return None

# Function to save the fetched data to a CSV file
def save_to_csv(data, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write headers
        writer.writerow(["Bid ID", "Item Name", "Bid Amount", "Bid Date"])
        # Write data rows
        for item in data.get("bids", []):
            writer.writerow([
                item["bidId"],
                item["itemName"],
                item["amount"],
                datetime.fromtimestamp(item["date"]).strftime("%Y-%m-%d %H:%M:%S")
            ])

# Main function to orchestrate the process
def main():
    data = fetch_auction_bids(YOUR_API_KEY)
    if data:
        save_to_csv(data, "auction_bids.csv")
        print("Data saved successfully to auction_bids.csv")

if __name__ == "__main__":
    main()
```

This script includes functions to fetch auction bid history from the Yahoo!オークション API and save it to a CSV file. Make sure to replace `your_api_key_here` with your actual API key. The CSV file will be named `auction_bids.csv`.