def add_piece(piece_name: str, composer: str, key: str, pieces_dict: dict) -> str:
    """
    Adds a piece to the dictionary if it doesn't already exist.
    """
    if piece_name in pieces_dict:
        return f"{piece_name} is already in the collection!"

    pieces_dict[piece_name] = {"composer": composer, "key": key}
    return f"{piece_name} by {composer} in {key} added to the collection!"


def remove_piece(piece_name: str, pieces_dict: dict) -> str:
    """
    Removes a piece from the dictionary if it exists.
    """
    if piece_name in pieces_dict:
        del pieces_dict[piece_name]
        return f"Successfully removed {piece_name}!"
    return f"Invalid operation! {piece_name} does not exist in the collection."


def change_key(piece_name: str, new_key: str, pieces_dict: dict) -> str:
    """
    Changes the key of an existing piece.
    """
    if piece_name in pieces_dict:
        pieces_dict[piece_name]["key"] = new_key
        return f"Changed the key of {piece_name} to {new_key}!"
    return f"Invalid operation! {piece_name} does not exist in the collection."


# Initialize dictionary to store the pieces
pieces = {}

# Read number of initial pieces
number_of_pieces = int(input())

# Read each piece and add it to the dictionary
for _ in range(number_of_pieces):
    piece_name, composer, key = input().split('|')
    pieces[piece_name] = {"composer": composer, "key": key}

# Process commands until "Stop"
while (command := input()) != "Stop":
    parts = command.split("|")
    action = parts[0]

    if action == "Add":
        piece_name = parts[1]
        composer = parts[2]
        key = parts[3]
        print(add_piece(piece_name, composer, key, pieces))

    elif action == "Remove":
        piece_name = parts[1]
        print(remove_piece(piece_name, pieces))

    elif action == "ChangeKey":
        piece_name = parts[1]
        new_key = parts[2]
        print(change_key(piece_name, new_key, pieces))

# Print the final collection
for piece_name, info in pieces.items():
    print(f"{piece_name} -> Composer: {info['composer']}, Key: {info['key']}")