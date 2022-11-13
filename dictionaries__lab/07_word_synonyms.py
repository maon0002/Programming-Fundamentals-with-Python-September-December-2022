number_of_synonyms = int(input())
synonym_dict = {}

for word in range(number_of_synonyms):
    main_word = input()
    synonym_word = input()
    if main_word not in synonym_dict.keys():
        synonym_dict[main_word] = []
    synonym_dict[main_word].append(synonym_word)

for key, value in synonym_dict.items():
    print(f"{key} - {', '.join(value)}")
