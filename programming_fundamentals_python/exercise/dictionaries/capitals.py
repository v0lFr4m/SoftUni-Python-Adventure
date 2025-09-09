country_names = input().split(", ")
capitals_city = input().split(", ")

my_dict = {name : city for (name, city) in zip(country_names , capitals_city)}

for i in my_dict:
    print(f"{i} -> {my_dict[i]}")