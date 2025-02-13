from collections import deque

def drunkard_game(boris_cards, nursik_cards):
    boris = deque(boris_cards)
    nursik = deque(nursik_cards)
    moves = 0

    while boris and nursik:
        if moves > 10**6:
            return "Draw"
        moves += 1

        b_card = boris.popleft()
        n_card = nursik.popleft()

        if (b_card == 0 and n_card == 9) or (b_card > n_card and not (b_card == 9 and n_card == 0)):
            boris.extend([b_card, n_card])  # Boris wins this round
        else:
            nursik.extend([b_card, n_card])  # Nursik wins this round

    # Determine  winner
    winner = "Boris" if boris else "Nursik"
    return f"{winner} {moves}"


boris_cards = list(map(int, input().split()))
nursik_cards = list(map(int, input().split()))

print(drunkard_game(boris_cards, nursik_cards))
