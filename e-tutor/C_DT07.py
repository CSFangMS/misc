# 大老二出牌組合 (Big Two combination)
# Clubs♣ : 1~13 = 0~12
# Diamonds♦ :1~13 = 13~25
# Heart♥ : 1~13 = 26~38
# Spades♠ : 1~13 = 39~51
# hands = ♣3♦4♥4♠3♠4 then input data = "2 16 29 41 42", output = 11
# made by SF
hands = input().split(" ")
total = 0
hands_size = len(hands) 

# create list of dictionary
# suits: Clubs C Diamonds D Heart H Spades S 
# hand = [{'rank':10, 'suit':'Spade'}, {'rank':11, 'suit':'Heart'}]
# useful if you're checking flush and stright flush (but not in this code)
hands_dictionary = []
suits_dict = ['Clubs', 'Diamonds', 'Heart', 'Spades']
for i in range(hands_size):
    if int(hands[i]) // 13 == 3:
        suit = suits_dict[3]
    elif int(hands[i]) // 13 == 2:
        suit = suits_dict[2]
    elif int(hands[i]) // 13 == 1:
        suit = suits_dict[1]
    elif int(hands[i]) // 13 == 0:
        suit = suits_dict[0]
    rank = int(hands[i]) % 13 + 1
    hands_dictionary.append({'rank': rank, 'suit': suit})
ranks = []
for i in range(hands_size):
    ranks.append(hands_dictionary[i]["rank"])
    ranks = sorted(ranks)

# single
total += hands_size

# pair: check duplicate rank
pair = []
for i in range(hands_size): 
    m = i + 1
    for j in range(m, hands_size):
        if hands_dictionary[i]["rank"] == hands_dictionary[j]["rank"]:
           pair.append(hands_dictionary[i]["rank"])
pair_size = len(pair)
total += pair_size

# three of a kind: check 3 duplicate
three = []
for i in range(hands_size): 
    m = i + 1
    for j in range(m, hands_size):
        n = j + 1
        for k in range(n, hands_size):
            if hands_dictionary[i]["rank"] == hands_dictionary[j]["rank"] == hands_dictionary[k]["rank"]:
                three.append(hands_dictionary[i]["rank"])
three_size = len(three)
total += three_size

# Straight 12345
straight_count = 0
for i in range(hands_size):
    n = i + 1
    for j in range(n, hands_size):
        o = j + 1
        for k in range(o, hands_size):
            p = k + 1
            for l in range(p, hands_size):
                q = l + 1
                for m in range(q, hands_size):
                    if int(ranks[i]) + 4 == int(ranks[j]) + 3 == int(ranks[k]) + 2 == int(ranks[l]) + 1 == int(ranks[m]):
                        straight_count += 1
total += straight_count
# still straight, deal with corner case: 10JQKA
corner_ranks = ranks.copy()
# change A10JQK-"1 10 11 12 13" to "10 11 12 13 14"
i = 0
while i < hands_size:
    if corner_ranks[i] == 1:
        corner_ranks.append(14)
        corner_ranks.remove(1)
        #i = 0
    else: i += 1
# delete every ranks is not "10 11 12 13 14"
i = 0
corner_hands_size = hands_size
while i < corner_hands_size:
    if corner_ranks[i] != 10 and corner_ranks[i] != 11 and corner_ranks[i] != 12 and corner_ranks[i] != 13 and corner_ranks[i] != 14:
        del corner_ranks[i]
        corner_hands_size -= 1
    else: i += 1
corner_straight_count = 0
for i in range(corner_hands_size):
    n = i + 1
    for j in range(n, corner_hands_size):
        o = j + 1
        for k in range(o, corner_hands_size):
            p = k + 1
            for l in range(p, corner_hands_size):
                q = l + 1
                for m in range(q, corner_hands_size):
                    if int(corner_ranks[i]) + 4 == int(corner_ranks[j]) + 3 == int(corner_ranks[k]) + 2 == int(corner_ranks[l]) + 1 == int(corner_ranks[m]):
                        corner_straight_count += 1
total += corner_straight_count

# Full House 3 + 2
FH_three = []
# FH_three of a kind
for i in range(hands_size): 
    m = i + 1
    for j in range(m, hands_size):
        n = j + 1
        for k in range(n, hands_size):
            if hands_dictionary[i]["rank"] == hands_dictionary[j]["rank"] == hands_dictionary[k]["rank"]:
                FH_three.append(hands_dictionary[i]["rank"])
FH_three_size = len(FH_three)

FH_size = 0
for i in range(FH_three_size):
    for j in range(hands_size):
        m = j + 1
        for k in range(m, hands_size):
            if hands_dictionary[j]["rank"] == hands_dictionary[k]["rank"] and hands_dictionary[j]["rank"] != FH_three[i]:
                FH_size += 1

total += FH_size

# Four of a kind: 4 duplicated rank with 1 rank (44441)
four = []
for i in range(hands_size): 
    m = i + 1
    for j in range(m, hands_size):
        n = j + 1
        for k in range(n, hands_size):
            o = k + 1
            for l in range(o, hands_size):
                if hands_dictionary[i]["rank"] == hands_dictionary[j]["rank"] == hands_dictionary[k]["rank"] == hands_dictionary[l]["rank"]:
                    four.append(hands_dictionary[i]["rank"])
four_size = len(four)

total_four_size = 0
for i in range(four_size):
    for j in range(hands_size):
        if hands_dictionary[j]["rank"] != four[i]:
            total_four_size += 1
total += total_four_size

# Straight Flush + 1 then Straght - 1, meaningless to count
print(total)