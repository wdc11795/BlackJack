CARD_VALUES = {
    '2': 1,
    '3': 1,
    '4': 2,
    '5': 2,
    '6': 2,
    '7': 1,
    '8': 0,
    '9': 0,
    '0': -2,  # use '0' for 10 to keep everything a single character
    'J': -2,
    'Q': -2,
    'K': -2,
    'A': -1,
    '*': -1,  # use '*' as an alias for 'A' to make using the number pad easier
}

DECKS = 8


def main():
    count = 0
    cards = 0
    user_input = True
    decks_played = 0
    while user_input:
        user_input = input(">>")
        cards += len(user_input)
        for card in user_input:
            count += CARD_VALUES[card.upper()]
        decks_played = cards / 52.0
        true_count = count / (DECKS - decks_played)
        print('Count: {}'.format(count))
        print('True Count: {}'.format(true_count))
    print('Decks played: {}'.format(decks_played))


if __name__ == '__main__':
    main()
