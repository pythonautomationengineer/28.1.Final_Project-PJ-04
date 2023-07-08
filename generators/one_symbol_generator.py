def one_symbol_generator():
    main_str = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    first_symbol = set(main_str).pop().upper()
    return first_symbol
