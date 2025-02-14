import requests

BASE_URL = "http://127.0.0.1:8000"

def test_search():
    query = "What is Boolean unite ?"
    response = requests.get(f"{BASE_URL}/search/", params={"query": query})
    print(response.json())

if __name__ == "__main__":
    test_search()