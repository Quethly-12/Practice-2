def count_character_frequency(input_string):
    char_frequency = {}

    for char in input_string:
        char_frequency[char] = char_frequency.get(char, 0) + 1

    print("Character frequency:")
    for char, freq in char_frequency.items():
        print(f"{char}: {freq}")

a = input("Enter a string: ").replace(" ", "")
count_character_frequency(a)
