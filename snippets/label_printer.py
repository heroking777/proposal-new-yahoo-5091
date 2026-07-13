import requests
from bs4 import BeautifulSoup
import barcode
from barcode.writer import ImageWriter

def fetch_auction_history(username, password):
    # Login to Yahoo!オークション and fetch the auction history
    login_url = 'https://auctions.yahoo.co.jp/mypage/login'
    session = requests.Session()
    response = session.get(login_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    csrf_token = soup.find('input', {'name': 'csrfToken'})['value']

    payload = {
        'username': username,
        'password': password,
        'csrfToken': csrf_token
    }
    session.post(login_url, data=payload)

    history_url = 'https://auctions.yahoo.co.jp/mypage/history'
    response = session.get(history_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    auction_items = soup.find_all('div', {'class': 'item'})

    return auction_items

def generate_barcode(text):
    # Generate a barcode for the given text
    EAN = barcode.get('ean13', text, writer=ImageWriter())
    filename = EAN.save('barcode')
    return filename

def save_receipt(auction_item):
    # Save the receipt for the given auction item
    title = auction_item.find('h2').text
    price = auction_item.find('span', {'class': 'price'}).text
    barcode_text = f"{title}{price}"
    barcode_filename = generate_barcode(barcode_text)
    with open(f"{barcode_filename}.txt", "w") as file:
        file.write(f"Title: {title}\nPrice: {price}\nBarcode: {barcode_text}")
    print(f"Receipt saved for {title} with barcode {barcode_filename}")

def main():
    username = 'your_yahoo_auction_username'
    password = 'your_yahoo_auction_password'

    auction_items = fetch_auction_history(username, password)
    for item in auction_items:
        save_receipt(item)

if __name__ == "__main__":
    main()
```

Please note that this script is a simplified example and may not work as expected due to changes in the Yahoo!オークション website's structure or security measures. Always ensure you comply with the terms of service of the website you are interacting with.