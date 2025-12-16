import grabber.get_page
import sys

def main(url: str) -> None:
    print(grabber.get_page.grab(url))

if __name__ == "__main__":
    # argv[0] is the script name
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} <url>")
        sys.exit(1)

    url = sys.argv[1]
    main(url)
