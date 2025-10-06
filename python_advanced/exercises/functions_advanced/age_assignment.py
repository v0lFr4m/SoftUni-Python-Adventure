def age_assignment(*args, **kwargs):
    result = []
    for name in sorted(args):
        age = kwargs[name[0]]
        result.append(f"{name} is {age} years old.")
    return '\n'.join(result)

print(age_assignment("Peter", "George", G=26, P=19))