def list_roman_emperors(*args , **kwargs):
    roman_emperors = {}

    for name, status in args:
        years = kwargs[name]
        if status:
            roman_emperors.setdefault("Successful", []).append((name, years))
        else:
            roman_emperors.setdefault("Unsuccessful", []).append((name, years))


    output_line = [f"Total number of emperors: {len(args)}"]
    if "Successful" in roman_emperors:
        roman_emperors["Successful"].sort(key=lambda x: (-x[1], x[0]))
        output_line.append("Successful emperors:")
        for name , years in roman_emperors['Successful']:
            output_line.append(f"****{name}: {years}")

    if "Unsuccessful" in roman_emperors:
        roman_emperors["Unsuccessful"].sort(key=lambda x: (x[1], x[0]))
        output_line.append("Unsuccessful emperors:")
        for name, years in roman_emperors["Unsuccessful"]:
            output_line.append(f"****{name}: {years}")

    return '\n'.join(output_line)


print(list_roman_emperors(("Augustus", True), ("Trajan", True), ("Nero", False), ("Caligula", False), ("Pertinax", False), ("Vespasian", True), Augustus=40, Trajan=19, Nero=14, Caligula=4, Pertinax=4, Vespasian=19,))