prime_numbers = [1, 3, 5, 7, 9, 11]

countries = ["Venezuela", "USA", "Colombia"]


for i in prime_numbers:
    print(i)

print("\n")

for i in enumerate(prime_numbers):
    print(i)

for i in range(len(countries)):
    for country in countries:
        print(i, country)
