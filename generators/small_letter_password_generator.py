def small_letter_password_generator():
    numbers = '1234567890'
    english_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    special_characters = '#$%^&*'
    one_sp_char = set(special_characters).pop()
    one_numb = set(numbers).pop()
    first_symbol = ''
    for i in set(english_alphabet):
        first_symbol += one_sp_char + one_numb + i
        if len(first_symbol) > 7:  # Итого 8 символов
            break

    return first_symbol
