import requests
import json

def fetch_data(mode, url_or_query):
    if mode == 'r':
        full_url = f"https://r.jina.ai/{url_or_query}"
        response = requests.get(full_url)
        with open("response.txt", "w", encoding="utf-8") as file:
            file.write(response.text)
        return response.status_code, response.text
    elif mode == 's':
        full_url = f"https://s.jina.ai/{url_or_query}"
        headers = {"Accept": "application/json"}
        response = requests.get(full_url, headers=headers)
        with open("response.json", "w", encoding="utf-8") as file:
            json.dump(response.json(), file, indent=4)
        return response.status_code, response.json()
    else:
        return "invalid input"

if __name__ == "__main__":
    mode = input("Enter 'r' for reading a URL or 's' for searching a query: ").strip().lower()
    if mode == 'r':
        url = input("Input url to read: ").strip()
        fetch_data(mode, url)
    elif mode == 's':
        query = input("Enter the search query:  ").strip()
        fetch_data(mode, query)
    else:
        print("invalid input. Please enter 'r' or 's'.")
