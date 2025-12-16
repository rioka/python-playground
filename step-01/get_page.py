import requests
import sys

def grab(url: str) -> None:

    response = requests.get(url)
    if response.status_code != 200:
        print(f"Unable to get {url}")
        return

    print(f"Content: {response.text}")

if __name__ == "__main__":
    # argv[0] is the script name
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} <url>")
        sys.exit(1)

    url = sys.argv[1]
    grab(url)
