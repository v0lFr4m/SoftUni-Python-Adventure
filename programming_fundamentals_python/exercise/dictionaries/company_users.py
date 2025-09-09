companies = {}

while (line := input()) != 'End':
    company_name , id_ = line.split(" -> ")

    if company_name not in companies:
        companies[company_name] = [id_]
    else:
        if id_ not in companies[company_name]:
            companies[company_name] += [id_]

for company_name, id_ in companies.items():
    print(f"{company_name}")
    for employee in id_:
        print(f"-- {employee}")
