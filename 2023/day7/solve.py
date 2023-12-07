from dataclasses import dataclass
from typing import List
from collections import Counter
from enum import Enum
from functools import cmp_to_key
from copy import copy

class Type(Enum):
    HighCard = 1
    OnePair = 2
    TwoPair = 3
    ThreeKind = 4
    FullHouse = 5
    FourKind = 6
    FiveKind = 7

@dataclass
class Hand:
    cards: []
    value: int
    type: Type = None
    
data: List[Hand]  = []

for line in open("./input.txt").readlines():
    line = line.strip("\n")
    cards = line.split(" ")[0]
    value = int(line.split(" ")[1])
    data.append(Hand(cards, value))

handStrength = {"J": 0, "2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7, "9": 8, "T": 9, "Q": 11, "K": 12, "A": 13}

def sortCards(c1, c2):
    if handStrength[c1] > handStrength[c2]:
        return -1
    return 1

def parseType(hand: Hand, accountForJoker: bool = False):
    if hand.cards == "JJJJJ":
        hand.type = Type.FiveKind
        return
    count = Counter([x for x in hand.cards if x != "J"])
    numberOfJs = Counter(hand.cards)["J"] if "J" in hand.cards else 0
    if not accountForJoker: 
        count = Counter(hand.cards)
        numberOfJs = 0
    countValues = list([x[1] for x in count.most_common(2)])
    ## In natural 5s
    if countValues[0] == 5:
        hand.type = Type.FiveKind #Nat 5
    ## In fours
    elif countValues[0] == 4:
        if numberOfJs == 1: hand.type = Type.FiveKind
        else: hand.type = Type.FourKind #Nat 4
    ## In three we can have nat 3, promote to 4kind, 5kind or a full house
    elif countValues[0] == 3:
        if numberOfJs == 2: hand.type = Type.FiveKind
        elif numberOfJs == 1: hand.type = Type.FourKind
        elif countValues[1] == 2: hand.type = Type.FullHouse
        else: hand.type = Type.ThreeKind
    ## In Two we can promote to 5kind, 4kind, 3kind/fullhouse or 2 pair
    elif countValues[0] == 2:
        if numberOfJs == 3: hand.type = Type.FiveKind
        elif numberOfJs == 2: hand.type = Type.FourKind
        elif numberOfJs == 1: 
            if countValues[1] == 2: hand.type = Type.FullHouse
            else: hand.type = Type.ThreeKind
        elif countValues[1] == 2: hand.type = Type.TwoPair
        else: hand.type = Type.OnePair
    else:
        if numberOfJs == 4: hand.type = Type.FiveKind
        elif numberOfJs == 3: hand.type = Type.FourKind
        elif numberOfJs == 2: hand.type = Type.ThreeKind
        elif numberOfJs == 1: hand.type = Type.OnePair
        else: hand.type = Type.HighCard



def handSort(hand1: Hand, hand2: Hand) -> int:
    print("Sort", hand1, hand2)
    # diffranks
    if hand1.type.value > hand2.type.value:
        return 1
    if hand2.type.value > hand1.type.value:
        return -1
    # sameranks
    for c1, c2 in zip(hand1.cards, hand2.cards):
        if handStrength[c1] > handStrength[c2]:
            return 1
        if handStrength[c2] > handStrength[c1]:
            return -1
    print("ISSUE WITH COMPARE")
    return 0

#### part 1 
        
hands1: List[Hand] = []
for hand in data:
    parseType(hand)
    hands1.append(hand)

hands1 = sorted(hands1, key=cmp_to_key(handSort))
p1sum = 0
for idx, hand in enumerate(hands1):
    p1sum += ((idx+1) * hand.value) 

## part 2
hands2: List[Hand] = []

for hand in data:
    parseType(hand, True)
    hands2.append(hand)

p2sum = 0
for idx, hand in enumerate(hands2):
    p2sum += ((idx+1) * hand.value)
print(p1sum, p2sum)

