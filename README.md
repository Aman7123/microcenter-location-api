# Microcenter Location API

This is a lightweight API that mimics the behavior of a cURL request to Microcenter's store location service. It accepts a `zip` parameter in the path and sends a POST request to Microcenter's server to retrieve location information. The API then parses the HTML response and sends back an array of JSON objects containing store information.

## Prerequisites

Before you can run this API script, ensure you have the following prerequisites installed:

- Python 3.x
- Flask (Python web framework)
- Requests library for making HTTP requests
- BeautifulSoup library for parsing HTML responses

You can install the required libraries by running the following commands:

```bash
pip3 install flask && \
pip3 install requests && \
pip3 install beautifulsoup4
```

## Usage

1. Clone this repository to your local machine:

```bash
git clone <repository_url>
cd microcenter-location-api
```

2. Run the API script:

```bash
python3 src/api.py
```

3. The API will start running locally at `http://127.0.0.1:5000/`.

4. To retrieve Microcenter location information, make a GET request to the following endpoint with the `zip` parameter:

```
http://127.0.0.1:5000/api/microcenterLocation?zip=<your_zip_code>
```

For example:

```
http://127.0.0.1:5000/api/microcenterLocation?zip=12345
```

5. The API will send a POST request to Microcenter's server and parse the HTML response to extract store information. It will then return an array of JSON objects, each representing a store's information.

Sample JSON response:

```json
[
    {
        "storename": "Fairfax",
        "address1": "3089 Nutley St",
        "city": "Fairfax",
        "state": "VA",
        "zip": "22031",
        "distance": "22.1 mi",
        "storelink": "https://www.microcenter.com/?storeID=081"
    },
    {
        "storename": "Rockville",
        "address1": "1776 E Jefferson ST Ste 203",
        "city": "Rockville",
        "state": "MD",
        "zip": "20852",
        "distance": "25.7 mi",
        "storelink": "https://www.microcenter.com/?storeID=085"
    }
]
```

## Contact
- Aaron Renner <aaron@aar.dev>