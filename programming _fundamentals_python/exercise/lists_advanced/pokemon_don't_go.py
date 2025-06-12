distance_of_the_pokemon = list(map(int, input().split()))


while len(distance_of_the_pokemon) > 0:
    index_input = int(input())
    for i in range(len(distance_of_the_pokemon)):
        current = distance_of_the_pokemon[i]
        if index_input == i:
            distance_of_the_pokemon.pop(index_input)
            if i <= current:
                increase = [i + current for i in range(len(distance_of_the_pokemon))]
            else:
                distance_of_the_pokemon += current

            distance_of_the_pokemon[index_input] -= current




