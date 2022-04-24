

num_of_cards = input()
cards = input().split()
int_cards = []
for card in cards:
    int_cards.append(int(card))

sereja_score = 0
dima_score = 0
for i in range(len(int_cards)):
    big_num = max([int_cards[0], int_cards[-1]])
    if i % 2 == 0:
        sereja_score += big_num
        int_cards.remove(big_num)
    else:
        dima_score += big_num
        int_cards.remove(big_num)

print(str(sereja_score) + '  ' + str(dima_score))