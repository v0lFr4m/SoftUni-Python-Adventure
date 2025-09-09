def check_ticket(ticket: str) -> str:
    if len(ticket) != 20:
        return "invalid ticket"
    winning_symbols = ('@', '#', '$', '^')
    left_part = ticket[:10]
    right_part = ticket[10:]
    for match_symbol in winning_symbols:
        for uninterrupted_match_length in range(10, 5, -1):
            winning_symbol_repetition = match_symbol * uninterrupted_match_length
            # Case where we have a winning ticket
            if winning_symbol_repetition in left_part and winning_symbol_repetition in right_part:
                # Jackpot ticket
                if uninterrupted_match_length == 10:
                    return f'ticket "{ticket}" - {uninterrupted_match_length}{match_symbol} Jackpot!'
                # Winning ticket (NO Jackpot)
                return f'ticket "{ticket}" - {uninterrupted_match_length}{match_symbol}'
    return f'ticket "{ticket}" - no match'


tickets = [ticket.strip() for ticket in input().split(", ")]
for current_ticket in tickets:
    print(check_ticket(current_ticket))