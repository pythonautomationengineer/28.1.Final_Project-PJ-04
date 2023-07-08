def very_long_last_name_generation():
    main_str = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    first_symbol = set(main_str).pop().upper()
    for i in set(main_str):
        first_symbol += i
        if len(first_symbol) > 30:
            break

    return first_symbol