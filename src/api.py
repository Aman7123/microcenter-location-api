from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route('/api/microcenterLocation', methods=['GET'])
def get_microcenter_locations():
    zip_code = request.args.get('zip')
    
    if zip_code:
        # Make the POST request to Microcenter
        url = 'https://www.microcenter.com/assets/ajax/storeZipCode.aspx'
        headers = {
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'https://www.microcenter.com',
            'Referer': 'https://www.microcenter.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
        }
        data = {
            'zip': zip_code,
            'url': 'https://www.microcenter.com/'
        }

        response = requests.post(url, headers=headers, data=data)

        if response.status_code == 200:
            # Parse the HTML response and extract store information
            soup = BeautifulSoup(response.text, 'html.parser')
            stores = []

            # Extract store information from HTML
            store_elements = soup.find_all('li', class_='inActiveStore')
            for store_element in store_elements:
                store_info = {
                    'storename': store_element.find(class_='storename').text.strip(),
                    'address1': store_element.find(class_='address1').text.strip(),
                    'city': store_element.find(class_='city').text.strip(),
                    'state': store_element.find(class_='state').text.strip(),
                    'zip': store_element.find(class_='zip').text.strip(),
                    'distance': store_element.find(class_='storedistance').text.strip(),
                    'storelink': store_element.find('a')['href'].strip()
                }
                stores.append(store_info)

            return jsonify(stores), 200
        else:
            return {"message": "Failed to retrieve data from Microcenter"}, 500
    else:
        return {"message": "Missing zip parameter"}, 400

if __name__ == '__main__':
    app.run()
