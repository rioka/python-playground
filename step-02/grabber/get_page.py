import requests
import sys

def grab(url: str) -> str:

    response = requests.get(url)
    if response.status_code != 200:
        print(f"Unable to get {url}")
        return None

    return response.text

if __name__ == "__main__":
    # argv[0] is the script name
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]}.py <url>")
        sys.exit(1)

    url = sys.argv[1]
    print(grab(url))
