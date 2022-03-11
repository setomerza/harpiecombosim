import random

from combinations import *

# Shuffles deck
def shuffle(deck):
    random.shuffle(deck)


# Draws 5 cards
def draw(deck, n):
    hand = []
    test_deck = deck.copy()
    shuffle(test_deck)
    for i in range(n):
        hand.append(test_deck.pop(0))
    return hand


# Keeps track of numbers times we can successfully combo
def combo_sim(deck, n):
    debug = False
    success_no_hts = 0
    success_2hts = 0
    success_vs_nibiru = 0
    success_vs_imperm = 0
    num_phalanx_bricks = 0
    opened_ht = 0
    success_partial_combo = 0
    discarded_sign = 0
    num_feather_storm = 0
    for i in range(0, n):
        test_hand = draw(deck, 5)
        if debug:
            print("Hand: " + ', '.join(map(str, test_hand)))
        shuffle(deck)
        results = combo(test_hand, deck, False)
        if results[0]:
            success_no_hts += 1
        if results[1]:
            success_2hts += 1

        if results[2]:
            success_vs_nibiru += 1

        if results[3]:
            opened_ht += 1

        if results[4]:
            success_vs_imperm += 1

        if results[5]:
            num_phalanx_bricks += 1

        if results[6]:
            success_partial_combo += 1

        if results[7]:
            discarded_sign += 1

        if results[8]:
            num_feather_storm += 1

    # Prints the results
    no_hts_ratio = round(success_no_hts / n * 100, 2)
    two_hts_ratio = round(success_2hts / n * 100, 2)
    nibiru_ratio = round(success_vs_nibiru / n * 100, 2)
    imperm_ratio = round(success_vs_imperm / n * 100, 2)
    open_ht_ratio = round(opened_ht / n * 100, 2)
    phalanx_brick_ratio = round(num_phalanx_bricks / n * 100, 2)
    feather_storm_ratio = round(num_feather_storm / n * 100, 2)
    partial_ratio = round(success_partial_combo / n * 100, 2)
    full_partial_ratio = round((success_partial_combo + success_no_hts) / n * 100, 2)
    hysteric_ratio = round(discarded_sign / n * 100, 2)

    dataFile = open("Previous_Run.txt", "r+")
    prev_results = dataFile.readline().split(" ")

    dataFile.close()
    print("Full Combo Success Rate through no Handtraps: " + str(no_hts_ratio) +
          "% (Prev: " + prev_results[0] + "%)")
    if "Fusion Destiny" in deck:
        print("Partial Combo/DPE Success Rate through no Handtraps: " + str(full_partial_ratio) +
          "% (Prev: " + prev_results[7] + "%)")
    #print("Combo Success Rate through Nibiru: " + str(nibiru_ratio) + "% (Prev: " + prev_results[1] + "%)")
    #print("Combo Success Rate through Imperm: " + str(imperm_ratio) + "% (Prev: " + prev_results[4] + "%)")
    print("Combo with drawing at least 1 Handtrap/Defensive Card: " + str(open_ht_ratio) +
          "% (Prev: " + prev_results[2] + "%)")
    print("Combo with drawing at least 2 Handtrap/Defensive Cards: " + str(two_hts_ratio) +
          "% (Prev: " + prev_results[6] + "%)")
    if "Hysteric Sign" in deck:
        print("Discarding Hysteric Sign: " + str(hysteric_ratio) + "% (Prev: " + prev_results[3] + "%)")
    print("Feather Storm Rate: " + str(feather_storm_ratio) + "% (Prev: " + prev_results[5] + "%)")
    print("Coltwing/Phalanx Brick Rate: " + str(phalanx_brick_ratio) + "% (Prev: " + prev_results[8] + "%)")


    dataFile = open("Previous_Run.txt", "w+")
    dataFile.write(str(no_hts_ratio) + " " + str(nibiru_ratio) + " " + str(open_ht_ratio) + " " + str(hysteric_ratio) +
                   " " + str(imperm_ratio) + " " + str(feather_storm_ratio) + " " + str(two_hts_ratio) +
                   " " + str(full_partial_ratio) + " " + str(phalanx_brick_ratio))
    dataFile.close()