from sets import *

# Verifies if hand can combo successfully

def combo(hand, deck):
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

    # Add barrier statue to the combo list if multiple are being played
    if deck.count("Barrier Statue of the Stormwinds") >= 2:
        normal_summon_non_harpies.append("Barrier Statue of the Stormwinds")

    # Instantly play through Imperm if Red Reboot/Midbreaker opened
    if ("Red Reboot" in hand) | ("Magical Mid-Breaker Field" in hand):
        play_vs_imperm = True

    # Combo with One card
    for i in normal_one_card_combo:
        if i in hand:
            possible_win = True

            # Case if no phalanx in deck, then it is not combo
            if phalanx_brick(hand, deck):
                if i == "Harpie Perfumer":
                    bricked_on_phalanx = True
                    possible_win = False

            if possible_win:
                win = True
                if debug:
                    print("One Card Combo")
                if ("Harpie's Feather Storm" in hand) & (("Harpie Perfumer" in hand) | ("Unexpected Dai" in hand)):
                    feather_stormed = True
                    play_vs_nibiru = True
                if ("Swallow's Nest" in hand) & ("Harpie Perfumer" in hand):
                    play_vs_imperm = True
                if "Quick Launch" in hand:
                    play_vs_imperm = not quick_launch_brick(hand, deck)
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

                for j in harpie_extender + ["Unexpected Dai"]:
                    if (("Gravedigger's Trap Hole" not in chan_hand) &
                            ("Gravedigger's Trap Hole" in deck) & (j in chan_hand)):
                        # Make Traptrix Rafflesia in 5 Summons
                        play_vs_nibiru = True

                    if ("World Chalice Guardragon" in hand):
                        play_vs_imperm = True

                # Case if no phalanx in deck, then it is not combo
                if phalanx_brick(chan_hand, deck):
                    bricked_on_phalanx = True
                    possible_win = False

                if possible_win:
                    win = True
                    if debug:
                        print("Channeler + Discard Combo")
                    if "Harpie's Feather Storm" in chan_hand:
                        feather_stormed = True
                        play_vs_nibiru = True
                    if "Swallow's Nest" in chan_hand:
                        play_vs_imperm = True
                    if "Quick Launch" in chan_hand:
                        play_vs_imperm = not quick_launch_brick(chan_hand, deck)
                    if "Hysteric Sign" in chan_hand:
                        discarded_sign = True
                    break

    # Combo with a harpie + harpie extender
    if (not win) or not play_vs_nibiru:
        for i in normal_summon_harpies + ["Unexpected Dai"]:
            for j in harpie_extender + no_monster_extender :
                if (i in hand) & (j in hand) & (i != j):
                    possible_win = True
                    has_vanilla = False

                    if (j in vanilla_access) | (i in vanilla_access):
                        has_vanilla = True

                    extender_test_hand = hand.copy()
                    extender_test_hand.remove(j)
                    # Board will be 2 winged beasts (1 guaranteed harpie) with possible vanilla access
                    winged_beasts = 2
                    for k in egotist_extender:
                        if k in extender_test_hand:
                            # Could potentially discard hysteric sign here
                            if k == "Hysteric Sign":
                                discarded_sign = True
                            winged_beasts += 1
                            has_vanilla = True
                            extender_test_hand.remove(k)

                    for l in egotist_extender:
                        if l in extender_test_hand:
                            winged_beasts += 1
                            has_vanilla = True
                            extender_test_hand.remove(l)

                    if "Harpie Perfumer" in hand:
                        # Perfumer counts as 2
                        winged_beasts += 1

                    if ("Garuda the Wind Spirit" in extender_test_hand) & has_vanilla:
                        winged_beasts += 1

                    if "Quick Launch" in hand:
                        play_vs_imperm = not quick_launch_brick(hand, deck)
                        if play_vs_imperm:
                            winged_beasts += 1

                    #Discard World Chalice Guardragon to negate Imperm vs Linked Romulus
                    if ((winged_beasts >= 3) & ("World Chalice Guardragon" in hand)):
                        play_vs_imperm = True

                    if ((winged_beasts >= 4) & ("Gravedigger's Trap Hole" not in hand)
                            & ("Gravedigger's Trap Hole" in deck)):
                        play_vs_nibiru = True

                    # Case if no phalanx in deck, then it is not combo
                    if phalanx_brick(hand, deck):
                        bricked_on_phalanx = True
                        possible_win = False

                    if possible_win:
                        win = True
                        if debug:
                            print("Harpie + Harpie Extender Combo. " + str(winged_beasts) + " Bodies")
                        if "Harpie's Feather Storm" in hand:
                            feather_stormed = True
                            play_vs_nibiru = True
                        break

    # Combo with a non-harpie + no monster SS
    if (not win) or not play_vs_nibiru:
        for i in normal_summon_non_harpies:
            for j in no_monster_extender:
                if (i in hand) & (j in hand):
                    possible_win = True

                    # Case if no phalanx in deck, then it is not combo
                    if phalanx_brick(hand, deck):
                        bricked_on_phalanx = True
                        possible_win = False

                    if possible_win:
                        win = True
                        if debug:
                            print("No Monster SS + Dragon Combo")
                        if ("Harpie's Feather Storm" in hand) and (j == "Unexpected Dai"):
                            feather_stormed = True
                            play_vs_nibiru = True
                        if "Quick Launch" in hand:
                            play_vs_imperm = not quick_launch_brick(hand, deck)
                        if "Hysteric Sign" in hand:
                            discarded_sign = True
                        break

    # Combo with Lvl 4 winged beast + extender
    if (not win) or not play_vs_nibiru:
        for i in lvl4_winged_beast:
            for j in lvl4_winged_beast_extender:
                if (i in hand) & (j in hand):
                    possible_win = True

                    # Case if no phalanx in deck, then it is not combo
                    if phalanx_brick(hand, deck):
                        bricked_on_phalanx = True
                        possible_win = False

                    if possible_win:
                        win = True
                        if debug:
                            print("Lvl 4 winged beast + extender combo")
                        if ("Harpie's Feather Storm" in hand) and ((j == "Unexpected Dai") | (j == "Swallow's Nest")):
                            feather_stormed = True
                            play_vs_nibiru = True
                        if "Quick Launch" in hand:
                            play_vs_imperm = not quick_launch_brick(hand, deck)
                        if "Hysteric Sign" in hand:
                            discarded_sign = True
                        break

    # Combo with Vanilla + World Chalice Guardragon
    if (not win) or not play_vs_nibiru:
        for i in vanilla_access:
            if i in hand:
                possible_win = False
                temp_hand = hand.copy()
                if "World Chalice Guardragon" in hand:
                    temp_hand.remove("World Chalice Guardragon")
                    possible_win = True

                if "Tempest, Dragon Ruler of Storms" in hand:
                    for j in wind_attribute:
                        if j in hand:
                            # Tempest + Discard for WCG
                            possible_win = True

                # Case if no phalanx in deck, then it is not combo
                if phalanx_brick(hand, deck):
                    bricked_on_phalanx = True
                    possible_win = False

                if possible_win:
                    win = True
                    if debug:
                        print("Vanilla + WCG Combo")
                    if "Harpie's Feather Storm" in hand:
                        feather_stormed = True
                        play_vs_nibiru = True

                    if "World Chalice Guardragon" in temp_hand:
                        play_vs_imperm = True

                    if "Quick Launch" in hand:
                        play_vs_imperm = not quick_launch_brick(hand, deck)

                    if "Hysteric Sign" in hand:
                        discarded_sign = True
                    break

    # Combo with Double Lyrilusc Turquoise Warbler
    if (not win) or not play_vs_nibiru:
        if "Lyrilusc - Turquoise Warbler" in hand:
            lyrilusc_hand = hand.copy()
            lyrilusc_hand.remove("Lyrilusc - Turquoise Warbler")
            if "Lyrilusc - Turquoise Warbler" in lyrilusc_hand:
                possible_win = True

                # Case if no phalanx in deck, then it is not combo
                if phalanx_brick(hand, deck):
                    bricked_on_phalanx = True
                    possible_win = False

                if possible_win:
                    win = True
                    if debug:
                        print("Double Lyrilusc Turquoise Warbler")

                    if "Quick Launch" in hand:
                        play_vs_imperm = not quick_launch_brick(hand, deck)

                    if "Hysteric Sign" in hand:
                        discarded_sign = True

                    for i in normal_summon_harpies:
                        if ("Harpie's Feather Storm" in lyrilusc_hand) & (i in lyrilusc_hand):
                            feather_stormed = True
                            play_vs_nibiru = True
                            if "World Chalice Guardragon" in hand:
                                play_vs_imperm = True

                    if "Harpie Channeler" in lyrilusc_hand:
                        lyrilusc_hand.remove("Harpie Channeler")
                        for j in harpie_card:
                            if (("Gravedigger's Trap Hole" not in lyrilusc_hand) & ("Gravedigger's Trap Hole" in deck) &
                                    (j in lyrilusc_hand)):
                                # Make Traptrix Rafflesia in 5 Summons
                                play_vs_nibiru = True

                            if ("Swallow's Nest" in hand) | ("World Chalice Guardragon" in hand):
                                play_vs_imperm = True

                    if "Harpie Perfumer" in lyrilusc_hand:
                        if ("Gravedigger's Trap Hole" not in lyrilusc_hand) & ("Gravedigger's Trap Hole" in deck):
                            # Make Traptrix Rafflesia in 5 Summons
                            play_vs_nibiru = True

                        if ("Swallow's Nest" in hand) | ("World Chalice Guardragon" in hand):
                            play_vs_imperm = True

                    for i in normal_summon_harpies:
                        for j in harpie_extender:
                            if (i in hand) & (j in hand):
                                # Make Traptrix Rafflesia in 5 Summons
                                play_vs_nibiru = True

                            if (i in hand) & ("World Chalice Guardragon" in hand):
                                play_vs_imperm = True

    # Combo with Vanilla + Garuda the Wind Spirit
    if (not win) or not play_vs_nibiru:
        for i in vanilla_access:
            if (i in hand) & ("Garuda the Wind Spirit" in hand):
                possible_win = True

                # Case if no phalanx in deck, then it is not combo
                if phalanx_brick(hand, deck):
                    bricked_on_phalanx = True
                    possible_win = False

                if possible_win:
                    win = True
                    if debug:
                        print("Vanilla + Garuda Combo")
                    if "Harpie's Feather Storm" in hand:
                        feather_stormed = True
                        play_vs_nibiru = True
                    if "Quick Launch" in hand:
                        play_vs_imperm = not quick_launch_brick(hand, deck)
                    if "Hysteric Sign" in hand:
                        discarded_sign = True
                    break

    #Quick Launch combos
    if (not win) or not play_vs_nibiru:
        for i in lvl4_winged_beast + no_monster_extender + normal_summon_non_harpies:
            if (i in hand) & ("Quick Launch" in hand):
                possible_win = True

                # Case if no quick launch targets in deck
                if quick_launch_brick(hand, deck):
                    possible_win = False

                # Case if no phalanx in deck, then it is not combo
                if phalanx_brick(hand, deck):
                    bricked_on_phalanx = True
                    possible_win = False

                if possible_win:
                    win = True
                    if debug:
                        print("Quick Launch Combo")
                    if "Harpie's Feather Storm" in hand:
                        for j in normal_summon_harpies + ["Unexpected Dai"]:
                            if j in hand:
                                feather_stormed = True
                                play_vs_nibiru = True
                    if "Hysteric Sign" in hand:
                        discarded_sign = True
                    break

    # Combo with  Phalanx + Divine Lance
    if (not win) or (not play_vs_nibiru) or (not partial_combo):
        if ("Dragunity Phalanx" in hand) & ("Dragunity Divine Lance" in hand):
            if phalanx_brick(hand, deck):
                bricked_on_phalanx = True
            else:
                win = True
                if "Hysteric Sign" in hand:
                    discarded_sign = True
                if debug:
                    print("Phalanx + Divine Lance combo")

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
