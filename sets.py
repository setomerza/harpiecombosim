# Handtrap (will include function to draw 2 Card off Phantzamay later)
handtraps = ["Nibiru, the Primal Being", "Effect Veiler", "Fantastical Dragon Phantazmay",
             "Ghost Mourner & Moonlit Chill", "Ash Blossom & Joyous Spring", "Infinite Impermanence",
             "Ghost Ogre & Snow Rabbit", "PSY-Framegear Gamma", "Gizmek Uka, the Festive Fox of Fecundity",
             "Forbidden Droplet", "Dimension Shifter", "Dark Ruler No More", "Lightning Storm",
             "Harpie's Feather Duster", "Droll & Lock Bird", "Artifact Lancea"]

# Handtraps that can only be used once per turn
opt_handtraps = ["Nibiru, the Primal Being", "Fantastical Dragon Phantazmay", "Ghost Mourner & Moonlit Chill",
                 "Ash Blossom & Joyous Spring", "Ghost Ogre & Snow Rabbit","PSY-Framegear Gamma",
                 "Gizmek Uka, the Festive Fox of Fecundity", "Dimension Shifter", "Droll & Lock Bird"]

# List of Harpie cards you can normal summon
normal_summon_harpies = ["Harpie Queen", "Harpie Harpist", "Harpie Lady", "Harpie Channeler", "Harpie Perfumer",
                         "Harpie Oracle", "Harpie Lady 1", "Cyber Harpie Lady", "Harpie Dancer"]

# List of Non-Harpie Winged Beast/Dragons you need a no_monster_extender to combo with
normal_summon_non_harpies = ["Dragunity Phalanx", "World Chalice Guardragon"]

# List of cards that can be special summon a winged beast if you control a harpie
harpie_extender = ["Elegant Egotist", "Swallow's Nest", "Hysteric Sign"]

# List of cards that act like Egotist
egotist_extender = ["Elegant Egotist", "Hysteric Sign"]

# List of cards you can SS if you control no monsters
no_monster_extender = ["Lyrilusc - Turquoise Warbler", "Unexpected Dai", "Cockadoodledoo"]

# Access to vanilla harpie lady
vanilla_access = ["Harpie Lady", "Unexpected Dai"]

# List of lvl 4 winged beasts
lvl4_winged_beast = ["Golden Castle of Stromberg", "Glife the Phantom Bird"] + normal_summon_harpies

# List of extenders that work with lvl 4 winged beast
lvl4_winged_beast_extender = ["Swallow's Nest", "Unexpected Dai", "Lyrilusc - Turquoise Warbler", "Cockadoodledoo"]

# List of targets to discard/banish with tempest
wind_attribute = ["Lyrilusc - Truquoise Warbler", "Dragunity Phalanx", "World Chalice Guardragon",
                  "Garuda the Wind Spirit", "Cockadoodledoo", "Mist Valley Thunderbird",
                  "Mist Valley Apex Avian", "Droll & Lock Bird"] + lvl4_winged_beast

# Normal summons that can combo by themselves
normal_one_card_combo = ["Harpie Perfumer", "Chamber Dragonmaid", "Starliege Seyfert", "Black Metal Dragon",
                         "One For One"]

harpie_card = ["Harpies' Hunting Ground", "Harpie Queen", "Harpie Oracle", "Harpie Harpist", "Harpie Channeler",
               "Harpie Perfumer", "Harpie Lady", "Harpie's Feather Rest", "Cyber Harpie Lady",
               "Harpie Lady Sisters", "Harpie Dancer", "Harpie Lady 1", "Harpie's Pet Dragon", "Harpie's Feather Storm"
               "Harpie's Feather Duster"]

quick_launch_targets = ["Rokket Tracer", "Rokket Synchron", "Magnarokket Dragon", "Silverrokket Dragon",
                        "Rokket Recharger", "Anesthrokket Dragon", "Autorokket Dragon", "Exploderokket Dragon",
                        "Metalrokket Dragon", "Shelrokket Dragon"]

# Cards that play through Nibiru
vs_nibiru = ["Harpie's Feather Storm"]


def phalanx_brick(hand, deck):
    deck_count = deck.count("Dragunity Phalanx")
    hand_count = hand.count("Dragunity Phalanx")
    return hand_count == deck_count

def quick_launch_brick(hand, deck):
    target_found = False

    for k in quick_launch_targets:
        if k in deck:
            target_found = True
            break

    # No quick launch targets found in deck
    if not target_found:
        return True

    temp_deck = deck.copy()

    # Check for targets in hand
    for i in hand:
        if i in quick_launch_targets:
            temp_deck.remove(i)

    for j in temp_deck:
        if j in quick_launch_targets:
            return False

    return True

def remove_all(hand, used):
    return [card for card in hand if card != used]
