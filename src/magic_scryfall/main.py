from pprint import pprint

import requests

from magic_scryfall.model.card import Card


def main():
    print("Hello World")
    card = Card("Mox")
    print(card)
    print(repr(card))
    print(f"bla_foo {card}")
    print(f"bla_foo {card!r}")
    for card in Card.search("bla"):
        print(card)


if __name__ == "__main__":
    main()
