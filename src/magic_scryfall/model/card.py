import requests


class Card:
    name: str

    def __init__(self, name: str):
        self.name = name

    def __repr__(self) -> str:
        return f"card: {self.name=}"

    def __str__(self) -> str:
        return f"card: {self.name}"

    @staticmethod
    def search(name: str) -> list["Card"]:
        response = requests.get(
            "https://api.scryfall.com/cards/search",
            params={"order": "cmc", "q": "c:red pow=3"},
        )
        # response.raise_for_status()
        if not response.ok:
            print(response.text)
            return []
        data = response.json()
        output = []
        for item in data["data"]:
            output.append(Card(item["name"]))
        return output
