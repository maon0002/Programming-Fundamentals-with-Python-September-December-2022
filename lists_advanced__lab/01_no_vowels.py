text = input()
vowels = ['a', 'o', 'u', 'e', 'i']
output = [v for v in text if v.lower() not in vowels]
print("".join(output))
