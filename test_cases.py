from combinations import combo


# One card combos
def one_card():
    assert combo(["Harpie Perfumer"], ["Dragunity Phalanx", "Mecha Phantom Beast Coltwing"], False)[0]
    # These hands should not combo
    assert not combo(["Dragunity Phalanx"], ["Dragunity Phalanx", "Mecha Phantom Beast Coltwing"], False)[0]
    assert not combo(["Unexpected Dai"], ["Dragunity Phalanx", "Mecha Phantom Beast Coltwing"], False)[0]
    assert not combo(["World Chalice Guardragon"], ["Dragunity Phalanx", "Mecha Phantom Beast Coltwing"], False)[0]
    return True


# Hands that combo with two cards
def two_card():
    assert combo(["Harpie Channeler", "Harpie Harpist"], ["Dragunity Phalanx", "Mecha Phantom Beast Coltwing"], False)[0]
    assert combo(["Harpie Lady", "Elegant Egotist"], ["Dragunity Phalanx", "Mecha Phantom Beast Coltwing"], False)[0]
    assert combo(["Unexpected Dai", "Swallow's Nest"], ["Dragunity Phalanx", "Mecha Phantom Beast Coltwing"], False)[0]
    assert combo(["Lyrilusc - Turquoise Warbler", "Lyrilusc - Turquoise Warbler"], ["Dragunity Phalanx", "Mecha Phantom Beast Coltwing"], False)[0]
    assert combo(["Small World", "Tenyi Spirit - Adhara"], ["Dragunity Phalanx", "Mecha Phantom Beast Coltwing"], False)[0]
    assert combo(["Preparation of Rites", "Emergency Teleport"],["Dragunity Phalanx", "Mecha Phantom Beast Coltwing"], False)[0]
    assert combo(["Tenyi Spirit - Adhara", "Emergency Teleport"], ["Mecha Phantom Beast Coltwing"], False)[0]
    # These hands should not combo
    assert not combo(["World Chalice Guardragon", "Elegant Egotist"], ["Dragunity Phalanx", "Mecha Phantom Beast Coltwing"], False)[0]
    return True


# Hands that combo with three cards
def three_card():

    # These hands should not combo

    return True


# Hands that can partial combo
def partial_combos():
    assert combo(["Harpie Channeler", "Harpie Harpist", "Mecha Phantom Beast Coltwing"], ["Dragunity Phalanx", "Mecha Phantom Beast Coltwing"], False)[6]
    assert combo(["Tenyi Spirit - Adhara", "Mecha Phantom Beast Coltwing"], ["Mecha Phantom Beast Coltwing"], False)[6]

    assert not combo(["Ghost Ogre & Snow Rabbit", "Ghost Ogre & Snow Rabbit", "Harpie Lady", "Mecha Phantom Beast Coltwing", "Ghost Belle & Haunted Mansion"], ["Dragunity Phalanx", "Mecha Phantom Beast Coltwing"], False)[6]
    return True


# combos we have recognised give a wrong result (we need to fix)
def incorrect_combos():
    return True


# combos that we haven't recognised vs nibiru (we need to fix)
def incorrect_nibiru_combos():
    return True


# Hands that can correctly combo/not combo through nibiru
def vs_nibiru():
    assert combo(["Harpie Perfumer", "Harpie's Feather Storm"], ["Dragunity Phalanx", "Mecha Phantom Beast Coltwing"], False)[2]

    assert combo(["Harpie Channeler", "Harpie Channeler", "Harpie's Feather Storm"],
                 ["Dragunity Phalanx", "Mecha Phantom Beast Coltwing"], False)[2]

    assert not combo(["Harpie Channeler", "Harpie's Feather Storm"],
                     ["Dragunity Phalanx", "Mecha Phantom Beast Coltwing"], False)[2]

    return True

def vs_imperm():

    return True

def sign_discard():
    assert combo(["Harpie Channeler", "Harpie Lady", "Hysteric Sign"], ["Dragunity Phalanx", "Mecha Phantom Beast Coltwing"], False)[7]
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
    assert sign_discard()

    print("All tests pass")


test_combo()
