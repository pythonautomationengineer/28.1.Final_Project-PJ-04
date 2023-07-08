def not_latin_password_generator():
    numbers = '1234567890'
    russian_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    special_characters = '#$%^&*'
    first_symbol = set(russian_alphabet).pop().upper()
    one_numbers = set(numbers).pop().upper()
    one_special_characters = set(special_characters).pop().upper()
    for i in set(russian_alphabet):
        first_symbol += one_numbers + one_special_characters + i
        if len(first_symbol) > 7:
            break

    return first_symbol