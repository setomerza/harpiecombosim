from combinations import combo


# One card combos
def one_card():
    assert combo(["Harpie Perfumer"], ["Dragunity Phalanx"])[0]
    # These hands should not combo
    assert not combo(["Dragunity Phalanx"], ["Dragunity Phalanx"])[0]
    assert not combo(["Unexpected Dai"], ["Dragunity Phalanx"])[0]
    assert not combo(["World Chalice Guardragon"], ["Dragunity Phalanx"])[0]
    return True


# Hands that combo with two cards
def two_card():
    assert combo(["Harpie Channeler", "Harpie Harpist"], ["Dragunity Phalanx"])[0]
    assert combo(["Harpie Lady", "Elegant Egotist"], ["Dragunity Phalanx"])[0]
    assert combo(["Unexpected Dai", "Swallow's Nest"], ["Dragunity Phalanx"])[0]
    assert combo(["Unexpected Dai", "Golden Castle of Stromberg"], ["Dragunity Phalanx"])[0]
    assert combo(["Lyrilusc - Turquoise Warbler", "Lyrilusc - Turquoise Warbler"], ["Dragunity Phalanx"])[0]
    assert combo(["Dragunity Phalanx", "Dragunity Divine Lance"], ["Dragunity Phalanx", "Dragunity Phalanx"])[0]
    assert combo(["Quick Launch", "Harpie Lady"], ["Dragunity Phalanx", "Rokket Tracer"])[0]
    # These hands should not combo
    assert not combo(["World Chalice Guardragon", "Elegant Egotist"], ["Dragunity Phalanx"])[0]
    assert not combo(["Quick Launch", "Harpie Lady"], ["Dragunity Phalanx"])[0]
    return True


# Hands that combo with three cards
def three_card():
    assert combo(["Quick Launch", "Rokket Tracer", "Harpie Lady"], ["Dragunity Phalanx", "Rokket Tracer",
                                                                    "Rokket Tracer"])[0]
    # These hands should not combo
    assert not combo(["Quick Launch", "Rokket Tracer", "Harpie Lady"], ["Dragunity Phalanx", "Rokket Tracer"])[0]
    return True


# Hands that can partial combo
def partial_combos():
    return True


# combos we have recognised give a wrong result (we need to fix)
def incorrect_combos():
    return True


# combos that we haven't recognised vs nibiru (we need to fix)
def incorrect_nibiru_combos():
    return True


# Hands that can correctly combo/not combo through nibiru
def vs_nibiru():
    assert combo(["Harpie Perfumer", "Harpie's Feather Storm"], ["Dragunity Phalanx"])[2]
    assert combo(["Harpie Channeler", "Harpie's Feather Storm", "Harpies' Hunting Ground"], ["Dragunity Phalanx"])[2]
    assert combo(["Lyrilusc - Turquoise Warbler", "Lyrilusc - Turquoise Warbler", "Harpie Perfumer"],
                 ["Gravedigger's Trap Hole", "Dragunity Phalanx"])[2]
    assert combo(["Lyrilusc - Turquoise Warbler", "Lyrilusc - Turquoise Warbler", "Harpie Channeler",
                  "Harpies' Hunting Ground"], ["Gravedigger's Trap Hole", "Dragunity Phalanx"])[2]

    assert combo(["Lyrilusc - Turquoise Warbler", "Lyrilusc - Turquoise Warbler", "Harpie Lady",
                  "Elegant Egotist"], ["Gravedigger's Trap Hole", "Dragunity Phalanx"])[2]

    assert combo(["Harpie Channeler", "Harpie Channeler", "Elegant Egotist"],
                 ["Gravedigger's Trap Hole", "Dragunity Phalanx"])[2]

    assert combo(["Harpie Channeler", "Harpie Channeler", "Harpie's Feather Storm"],
                 ["Dragunity Phalanx"])[2]

    assert not combo(["Harpie Channeler", "Harpie's Feather Storm"],
                     ["Dragunity Phalanx"])[2]

    return True

def vs_imperm():
    assert combo(["Harpie Perfumer", "Quick Launch"],
                     ["Dragunity Phalanx", "Rokket Tracer"])[4]

    return True


def test_combo():
    # Tests all
    assert one_card()
    assert two_card()
    assert vs_nibiru()
    assert vs_imperm()
    assert incorrect_combos()
    assert three_card()
    assert incorrect_nibiru_combos()
    assert partial_combos()

    print("All tests pass")


test_combo()
