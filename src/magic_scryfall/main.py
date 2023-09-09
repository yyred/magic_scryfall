from pprint import pprint

import requests


def main():
    print("Hello World")
    response = requests.get("https://www.google.com")
    print(response)
    pprint(response.headers)


if __name__ == "__main__":
    main()
