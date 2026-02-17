hindu_books = [
    "Bhagavad Gita",
    "Ramayana",
    "Mahabharata",
    "Upanishads",
    "Rigveda",
    "Atharvaveda",
    "Vishnu Purana",
    "Shiva Purana"]
writers = [
    "Sage Vyasa",
    "Sage Valmiki",
    "Sage Vyasa",
    "Various authors",
    ]

hindu_books_writers_dict = zip(hindu_books, writers)
print(dict(hindu_books_writers_dict))

inverse=dict()
for key in hindu_books_writers_dict:
	val = hindu_books_writers_dict[key]
	if val not in inverse:
		inverse[val] = key
print (inverse)