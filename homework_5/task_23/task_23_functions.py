def compress_string_rle(user_input: str) -> str:
    list_from_strings: list[str] = list(user_input)

    temp_value: str = ""
    char_counter: int = 0
    compressed_rle_string: str = ""
    for i in range(len(list_from_strings)):
        if (i == 0):
            temp_value = list_from_strings[i]
        if (temp_value == list_from_strings[i]):
            char_counter += 1
        elif (temp_value != list_from_strings[i]):
            compressed_rle_string += f"{char_counter}{temp_value}"
            char_counter = 0
            temp_value = list_from_strings[i]
            char_counter += 1
    compressed_rle_string += f"{char_counter}{temp_value}"

    return compressed_rle_string

def decompress_rle_one_digit_numbers(compressed_rle: str) -> str:
    new_list: list[str] = list(compressed_rle)
    list_of_lists = []
    j: int = 0
    for i in range(len(new_list)):
        if i % 2 == 0:
            list_of_lists.append([int(new_list[i])])
        else:
            list_of_lists[j].append(str(new_list[i]))
            j += 1

    decompressed_rle_numbers: str = ""
    for item in list_of_lists:
        decompressed_rle_numbers += item[0] * item[1]

    print(f"Decompressed RLE single digits -> {decompressed_rle_numbers}")
    return decompressed_rle_numbers

def decompress_rle_letters(compressed_rle: str) -> str:
    decompressed_rle = ""
    number_of_chars = ""
    for char in compressed_rle:
        if char.isalpha():
            decompressed_rle += char * int(number_of_chars)
            number_of_chars = ""
        else:
            number_of_chars += char
    print(f"Decompressed RLE letters -> {decompressed_rle}")
    return decompressed_rle

def decompress_rle_numbers_or_letters(compressed_rle: str, is_decompressing_letters: bool) -> str:
    if is_decompressing_letters:
        return decompress_rle_letters(compressed_rle)
    else:
        return decompress_rle_one_digit_numbers(compressed_rle)