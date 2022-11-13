countries = input().split(", ")
capitals = input().split(", ")
pairs_dictionary = dict(zip(countries, capitals))
for country, capital in pairs_dictionary.items():
    print(f"{country} -> {capital}")
