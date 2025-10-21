def classify_books(*args , **kwargs):
    fiction_books = {}
    non_fiction_books = {}
    books = {}
    for genre , name in args:
        books[name] = genre

    for isbn , book_name in kwargs.items():
        if books.get(book_name) == 'fiction':
            fiction_books[isbn] = book_name
        elif books.get(book_name) == 'non_fiction':
            non_fiction_books[isbn] = book_name

    fiction_books_sorted = sorted(fiction_books.items())
    non_fiction_book_sorted = sorted(non_fiction_books.items(), reverse= True)

    output_line = []
    if fiction_books_sorted:
        output_line.append("Fiction Books:")
        for isbn , name in fiction_books_sorted:
            output_line.append(f"~~~{isbn}#{name}")
    if non_fiction_book_sorted:
        output_line.append("Non-Fiction Books:")
        for isbn, name in non_fiction_book_sorted:
            output_line.append(f"***{isbn}#{name}")

    return '\n'.join(output_line)



print(classify_books(
    ("non_fiction", "Sapiens"),
    ("non_fiction", "Homo Deus"),
    ("non_fiction", "The Selfish Gene"),
    NF123ABC="Sapiens",
    NF987XYZ="Homo Deus",
    NF456DEF="The Selfish Gene"
))
