from Combo_Simulator import combo_sim

def import_deck(filename):
    with open(filename) as f:
        deck = [line.strip() for line in f if not line.startswith('#')]
        return deck


# What decklist we want to import and how many hands we want to simulate
def main(deck_txt, n):
    print(deck_txt)
    deck = import_deck(deck_txt)
    combo_sim(deck, n)

# Using 25000 so it runs quicker as this is an online IDE
main("Decklists/Harpies_42", 300000)


