# Handtrap (will include function to draw 2 Card off Phantzamay later)
handtraps = ["Nibiru, the Primal Being", "Effect Veiler", "Fantastical Dragon Phantazmay",
             "Ghost Mourner & Moonlit Chill", "Ash Blossom & Joyous Spring", "Infinite Impermanence",
             "Ghost Ogre & Snow Rabbit", "PSY-Framegear Gamma", "Gizmek Uka, the Festive Fox of Fecundity",
             "Forbidden Droplet", "Dimension Shifter", "Dark Ruler No More", "Lightning Storm",
             "Harpie's Feather Duster", "Droll & Lock Bird", "Artifact Lancea", "D.D. Crow",
             "Ghost Belle & Haunted Mansion"]

# Handtraps that can only be used once per turn
opt_handtraps = ["Nibiru, the Primal Being", "Fantastical Dragon Phantazmay", "Ghost Mourner & Moonlit Chill",
                 "Ash Blossom & Joyous Spring", "Ghost Ogre & Snow Rabbit", "PSY-Framegear Gamma",
                 "Gizmek Uka, the Festive Fox of Fecundity", "Dimension Shifter", "Droll & Lock Bird",
                 "Ghost Belle & Haunted Mansion"]

# Cards that can be sent to draw with Magicians' Souls
spell_traps = ["Infinite Impermanence", "Forbidden Droplet", "Dark Ruler No More", "Lightning Storm",
               "Harpie's Feather Duster", "Dragunity Divine Lance", "Preparation of Rites", "Small World",
               "Elegant Egotist", "Hysteric Sign", "Unexpected Dai"]

# List of cards that behave like Magicians' Souls
magicians_souls = ["Magicians' Souls", "Illusion of Chaos", "Preparation of Rites"]

# Cards that Combo with Small World into Perfumer
small_world_perfumer_targets = ["Effect Veiler", "Ghost Mourner & Moonlit Chill", "Ash Blossom & Joyous Spring",
                                "Ghost Ogre & Snow Rabbit", "PSY-Framegear Gamma", "Droll & Lock Bird", "D.D. Crow",
                                "Ghost Belle & Haunted Mansion", "Tenyi Spirit - Adhara"] + magicians_souls

# List of Harpie cards you can normal summon
normal_summon_harpies = ["Harpie Queen", "Harpie Harpist", "Harpie Lady", "Harpie Channeler", "Harpie Perfumer",
                         "Harpie Oracle", "Harpie Lady 1", "Cyber Harpie Lady", "Harpie Dancer"]

# List of tuners you need a no_monster_extender to combo with
normal_summon_tuners = ["Creation Resonator", "Dragunity Phalanx", "Effect Veiler",
                        "Ghost Mourner & Moonlit Chill", "Ash Blossom & Joyous Spring",
                        "Ghost Ogre & Snow Rabbit", "Ghost Belle & Haunted Mansion"]

normal_summon_non_tuners = ["Destiny HERO - Celestial", "Droll & Lock Bird", "D.D. Crow",
                            "Mecha Phantom Beast Coltwing"] + normal_summon_harpies

# List of cards that can be special summon a winged beast if you control a harpie
harpie_extender = ["Elegant Egotist", "Swallow's Nest", "Hysteric Sign"]

# List of cards that act like Egotist
egotist_extender = ["Elegant Egotist", "Hysteric Sign"]

# List of cards treated as vanilla harpie lady
vanilla_access = ["Unexpected Dai", "Harpie Lady"]

# List of non tuner extenders
non_tuner_extender = ["Lyrilusc - Turquoise Warbler", "Unexpected Dai"] + magicians_souls

# List of tuner extenders
tuner_extender = ["Emergency Teleport", "Tenyi Spirit - Adhara", "Cockadoodledoo"]

# Normal summons that can combo by themselves
normal_one_card_combo = ["Harpie Perfumer", "Plaguespreader Zombie", "Deep Sea Diva"]

harpie_card = ["Harpies' Hunting Ground", "Harpie Queen", "Harpie Oracle", "Harpie Harpist", "Harpie Channeler",
               "Harpie Perfumer", "Harpie Lady", "Harpie's Feather Rest", "Cyber Harpie Lady",
               "Harpie Lady Sisters", "Harpie Dancer", "Harpie Lady 1", "Harpie's Pet Dragon", "Harpie's Feather Storm"
                                                                                               "Harpie's Feather Duster"]

# Cards that play through Nibiru
vs_nibiru = ["Harpie's Feather Storm"]


def phalanx_brick(hand, deck):
    deck_count = deck.count("Dragunity Phalanx")
    hand_count = hand.count("Dragunity Phalanx")
    return hand_count == deck_count


def coltwing_brick(hand, deck):
    deck_count = deck.count("Mecha Phantom Beast Coltwing")
    hand_count = hand.count("Mecha Phantom Beast Coltwing")
    return hand_count == deck_count


# Magicians Souls draw cards
def souls_draw(hand, deck):
    debug = False
    temp_hand = hand.copy()
    if "Magicians' Souls" in hand:
        temp_hand.remove("Magicians' Souls")
    elif "Illusion of Chaos" in hand:
        temp_hand.remove("Illusion of Chaos")

    st_count = 0
    for i in temp_hand:
        if i in spell_traps:
            if st_count < 2:
                hand.remove(i)
                top_card = deck[st_count]
                hand.append(top_card)
                if debug:
                    print("Souls send " + i + " to draw " + top_card)
                st_count += 1

    return hand, deck


def remove_all(hand, used):
    return [card for card in hand if card != used]
