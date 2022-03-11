from sets import *

# Verifies if hand can combo successfully

def combo(hand, deck, souls_drawn):
    debug = False
    win = False
    play_vs_nibiru = False
    play_vs_imperm = False
    bricked_on_phalanx = False
    partial_combo = False
    discarded_sign = False
    feather_stormed = False

    # Checks if drawn handtraps
    open_ht, open_two_hts = two_hts(hand)

    # Instantly play through Imperm if Red Reboot/Midbreaker opened
    if ("Red Reboot" in hand) | ("Magical Mid-Breaker Field" in hand):
        play_vs_imperm = True

    # Combo with One card
    for i in normal_one_card_combo:
        if i in hand:
            possible_win = True

            # Case if no phalanx in deck, then it is not combo
            if phalanx_brick(hand, deck):
                if ("Illusion of Chaos" not in hand) & ("Preparation of Rites" not in hand):
                    if i == "Harpie Perfumer":
                        bricked_on_phalanx = True
                        possible_win = False
            elif coltwing_brick(hand, deck):
                if ("Illusion of Chaos" not in hand) & ("Preparation of Rites" not in hand):
                    bricked_on_phalanx = True
                    possible_win = False
                    partial_combo = True


            if possible_win:
                win = True
                if debug:
                    print("One Card Combo")
                if ("Harpie's Feather Storm" in hand) & (("Harpie Perfumer" in hand) | ("Unexpected Dai" in hand)):
                    feather_stormed = True
                    play_vs_nibiru = True
                if ("Swallow's Nest" in hand) & ("Harpie Perfumer" in hand):
                    play_vs_imperm = True
                if "Hysteric Sign" in hand:
                    discarded_sign = True
                break

    # Combo with Channeler + Discard
    if ((not win) or not play_vs_nibiru) & ("Harpie Channeler" in hand):
        chan_hand = hand.copy()
        chan_hand.remove("Harpie Channeler")
        for i in harpie_card:
            if i in chan_hand:
                possible_win = True
                chan_hand.remove(i)

                # Case if no phalanx in deck, then it is not combo
                if phalanx_brick(chan_hand, deck) | coltwing_brick(hand, deck):
                    if ("Illusion of Chaos" not in hand) & ("Preparation of Rites" not in hand):
                        bricked_on_phalanx = True
                        possible_win = False
                        partial_combo = True
                    if debug:
                        print("Channeler Partial Combo")

                if possible_win:
                    win = True
                    if debug:
                        print("Channeler + Discard Combo")
                    if "Harpie's Feather Storm" in chan_hand:
                        feather_stormed = True
                        play_vs_nibiru = True
                    if "Swallow's Nest" in chan_hand:
                        play_vs_imperm = True
                    if "Hysteric Sign" in chan_hand:
                        discarded_sign = True
                    break

    # Combo with a normal summon tuner + extender
    if (not win) or not play_vs_nibiru:
        for i in normal_summon_tuners:
            for j in non_tuner_extender + tuner_extender:
                if (i in hand) & (j in hand) & (i != j):
                    possible_win = True

                    extender_test_hand = hand.copy()
                    extender_test_hand.remove(j)
                    # Board will be 2 winged beasts (1 guaranteed harpie) with possible vanilla access

                    # Case if no coltwing in deck, then it is not combo
                    if coltwing_brick(hand, deck):
                        if ("Illusion of Chaos" not in hand) & ("Preparation of Rites" not in hand):
                            possible_win = False
                            bricked_on_phalanx = True
                            partial_combo = True

                    if i == "Creation Resonator":
                        possible_win = False
                        partial_combo = True

                    if possible_win:
                        win = True
                        if debug:
                            print("Normal Summon Tuner + Extender Combo.")
                        if ("Harpie's Feather Storm" in hand) and (j == "Unexpected_Dai"):
                            feather_stormed = True
                        if "Hysteric Sign" in hand:
                            discarded_sign = True
                        break

    # Combo with a normal summon harpie + extender
    if (not win) or not play_vs_nibiru:
        for i in normal_summon_harpies + ["Unexpected Dai"]:
            for j in harpie_extender + tuner_extender:
                if (i in hand) & (j in hand):
                    possible_win = True

                    # Case if no phalanx in deck, then it is not combo
                    if phalanx_brick(hand, deck):
                        if j in harpie_extender:
                            if ("Illusion of Chaos" not in hand) & ("Preparation of Rites" not in hand):
                                bricked_on_phalanx = True
                                possible_win = False
                                partial_combo = True

                    if coltwing_brick(hand, deck):
                        if ("Illusion of Chaos" not in hand) & ("Preparation of Rites" not in hand):
                            possible_win = False
                            bricked_on_phalanx = True
                            partial_combo = True

                    if possible_win:
                        win = True
                        if debug:
                            print("Normal Summon Harpie + Extender Combo.")
                        if "Harpie's Feather Storm" in hand:
                            feather_stormed = True
                            play_vs_nibiru = True
                        if ("Hysteric Sign" in hand) and (j != "Hysteric Sign"):
                            discarded_sign = True
                        break

    # Combo with Small World into Perfumer
    if ((not win) or not play_vs_nibiru) & ("Small World" in hand):
        sw_hand = hand.copy()
        sw_hand.remove("Small World")
        for i in small_world_perfumer_targets:
            if i in sw_hand:
                possible_win = True
                sw_hand.remove(i)

                # Case if no phalanx in deck, then it is not combo
                if phalanx_brick(hand, deck) | coltwing_brick(hand, deck):
                    if ("Illusion of Chaos" not in hand) & ("Preparation of Rites" not in hand):
                        bricked_on_phalanx = True
                        possible_win = False
                        partial_combo = True

                if possible_win:
                    win = True
                    if debug:
                        print("Small World into Perfumer Combo")
                    if "Harpie's Feather Storm" in sw_hand:
                        feather_stormed = True
                        play_vs_nibiru = True
                    if "Swallow's Nest" in sw_hand:
                        play_vs_imperm = True
                    if "Hysteric Sign" in sw_hand:
                        discarded_sign = True
                    break

    # Combo with a tuner extender + extender
    if (not win) or not play_vs_nibiru:
        for i in tuner_extender:
            for j in non_tuner_extender + tuner_extender:
                if (i in hand) & (j in hand) & (i != j):
                    possible_win = True

                    if coltwing_brick(hand, deck):
                        if ("Illusion of Chaos" not in hand) & ("Preparation of Rites" not in hand):
                            possible_win = False
                            bricked_on_phalanx = True
                            partial_combo = True

                    if possible_win:
                        win = True
                        if debug:
                            print("Tuner Extender + Extender Combo")
                        if "Hysteric Sign" in hand:
                            discarded_sign = True
                        break

    # Combo with Double Lyrilusc Turquoise Warbler
    if not win:
        if "Lyrilusc - Turquoise Warbler" in hand:
            lyrilusc_hand = hand.copy()
            lyrilusc_hand.remove("Lyrilusc - Turquoise Warbler")
            if "Lyrilusc - Turquoise Warbler" in lyrilusc_hand:
                possible_win = True
                # Case if no phalanx in deck, then it is not combo
                if phalanx_brick(hand, deck) | coltwing_brick(hand, deck):
                    if ("Illusion of Chaos" not in hand) & ("Preparation of Rites" not in hand):
                        bricked_on_phalanx = True
                        possible_win = False
                        partial_combo = True

                if possible_win:
                    win = True
                    if debug:
                        print("Double Warbler Combo")
                    if "Hysteric Sign" in hand:
                        discarded_sign = True

    # Combo with Vanilla + World Chalice Guardragon
    if not win:
        for i in vanilla_access:
            if (i in hand) & ("World Chalice Guardragon" in hand):
                possible_win = True
                # Case if no phalanx in deck, then it is not combo
                if phalanx_brick(hand, deck) | coltwing_brick(hand, deck):
                    if ("Illusion of Chaos" not in hand) & ("Preparation of Rites" not in hand):
                        bricked_on_phalanx = True
                        possible_win = False
                        partial_combo = True

                if possible_win:
                    win = True
                    if debug:
                        print("Vanilla + WCG Combo")
                    if "Hysteric Sign" in hand:
                        discarded_sign = True
                    if "Harpie's Feather Storm" in hand:
                        feather_stormed = True
                        play_vs_nibiru = True
                    break

    # If unable to combo, attempt to draw with souls
    if not win:
        for i in magicians_souls:
            if (i in hand) & (souls_drawn == False):
                temp_hand = hand.copy()
                temp_hand, deck = souls_draw(temp_hand, deck)
                if "Hysteric Sign" in hand:
                    discarded_sign = True

                result = combo(temp_hand, deck, True)
                if debug:
                    print("Attempting Souls Hand:" + ', '.join(map(str, temp_hand)))
                win = result[0]
                partial_combo = result[6]
                break

    #Check for Coltwing partial combo
    if (not win) & ("Mecha Phantom Beast Coltwing" in hand):
        for i in tuner_extender + non_tuner_extender:
            if i in hand:
                partial_combo = True
                if "Hysteric Sign" in hand:
                    discarded_sign = True
                if debug:
                    print("Partial Combo - Coltwing + Extender")
                break

    #Check for other partial combos
    if (not win) & ("Fusion Destiny" in deck):
        if "Fusion Destiny" in hand:
            partial_combo = True
            if debug:
                print("Partial Combo - Hard open Fusion Destiny")
            if "Hysteric Sign" in hand:
                discarded_sign = True
        else:
            for i in non_tuner_extender:
                for j in normal_summon_non_tuners:
                    if (i in hand) & (j in hand):
                        partial_combo = True
                        if debug:
                            print("Partial Combo - 2 Non tuners")
                        if "Hysteric Sign" in hand:
                            discarded_sign = True
                        break

            if not partial_combo:
                for i in magicians_souls:
                    if i in hand:
                        temp_hand = hand.copy()
                        temp_hand.remove(i)
                        if "Magicians' Souls" in temp_hand:
                            partial_combo = True
                            if debug:
                                print("Partial Combo - Double Souls")
                            if "Hysteric Sign" in hand:
                                discarded_sign = True
                            break

    win_nibiru = (win | partial_combo) & play_vs_nibiru
    win_imperm = win & play_vs_imperm
    open_ht = (win | partial_combo) & open_ht
    open_two_hts = (win | partial_combo) & open_two_hts
    if win:
        partial_combo = False
        bricked_on_phalanx = False
    return [win, open_two_hts, win_nibiru, open_ht, win_imperm, bricked_on_phalanx, partial_combo, discarded_sign,
            feather_stormed]


# Checks if we have a handtrap in hand
def hts(hand):
    return any(i in handtraps for i in hand)


# Checks if we have 2 playable handtraps in hand
def two_hts(hand):
    open_one_ht = False
    open_two_hts = False
    for i in hand:
        if i in handtraps:
            open_one_ht = True
            if i in opt_handtraps:
                open_two_hts = hts(remove_all(hand.copy(), i))
            else:
                temp_hand = hand.copy()
                temp_hand.remove(i)
                open_two_hts = hts(temp_hand)
    return open_one_ht, open_two_hts
