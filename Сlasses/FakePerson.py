import random
from faker import Faker

fake = Faker('ru_RU')


# Возможно в 1 случае из 100 или 1000000 сгенерируется не то, на что я рассчитывал, из-за какого то окончания,
# которое я не учел, но тесты из-за этого не упадут, поэтому это не страшно.

class FakePerson:
    """Генерация необходимых тестовых данных: имени, фамилии, отчества и телефона"""
    min_length_last_name = 4  # задает минимальную длину фамилии
    max_length_last_name = 10  # задает максимальную длину фамилии
    max_length_first_name = 10  # задает максимальную длину имени
    min_length_first_name = 4  # задает минимальную длину имени
    max_length_patronymic_name = 12  # задает максимальную длину отчества
    min_length_patronymic_name = 12  # задает минимальную длину отчества
    length_phone = 11  # задает длину номера телефона
    first_name_word_endings = {'ов', 'ев', 'ёв', 'ин', 'ич', 'на', 'ва', 'ия', 'са', 'ра', 'та', 'вь', 'да', 'ья', 'га',
                               'ла',
                               'оя', 'фа', 'ея', 'ор', 'ка', 'ца', 'ия', 'ль', 'ма', 'ея', 'а', 'вь', 'ь'}
    patronymic_name_word_ending = {'ич'}
    last_name_word_endings = {'ов', 'ев', 'ёв', 'ин'}
    operators = ['790', '791', '792', '795']  # несколько валидных операторов

    @staticmethod
    def generate_last_name_of_man(old_last_name: str) -> str:
        """Генерация мужской фамилии"""
        name = fake.name()
        last_name = name.split()[0]
        if (old_last_name != last_name) and (FakePerson.min_length_last_name < len(last_name)
                                             < FakePerson.max_length_last_name) \
                and last_name[-2:] in FakePerson.last_name_word_endings and len(last_name) != len(old_last_name):
            return last_name
        else:
            return FakePerson.generate_last_name_of_man(old_last_name)

    @staticmethod
    def generate_first_name_of_man(old_first_name: str) -> str:
        """Генерация мужского имени"""
        name = fake.name()
        first_name = name.split()[1]

        if (old_first_name != first_name) and (FakePerson.min_length_first_name < len(first_name)
                                               < FakePerson.max_length_first_name) \
                and first_name[-2:] not in FakePerson.first_name_word_endings \
                and len(first_name) != len(old_first_name):
            return first_name
        else:
            return FakePerson.generate_first_name_of_man(old_first_name)

    @staticmethod
    def generate_patronymic_name_of_man(old_patronymic_name: str) -> str:
        """Генерация мужского имени"""
        name = fake.name()
        patronymic_name = name.split()[2]
        if (old_patronymic_name != patronymic_name) and (
                FakePerson.min_length_patronymic_name < len(patronymic_name)
                < FakePerson.max_length_patronymic_name) \
                and patronymic_name[-2:] in FakePerson.patronymic_name_word_ending \
                and len(patronymic_name) != len(old_patronymic_name):
            return patronymic_name
        else:
            return FakePerson.generate_patronymic_name_of_man(old_patronymic_name)

    @staticmethod
    def generate_fake_phone() -> str:
        """Генерация случайного номера, с некоторыми доработками под требования соответствующего поля формы
        на тестируемом сайте"""
        phone = fake.phone_number()
        if len(phone) == FakePerson.length_phone and phone[0:1] == '8':
            # вернуть случайного оператора со сгенерированными оставшимися символами
            return FakePerson.operators[random.randint(0, 3)] + f'{phone[3:]}'
        else:
            return FakePerson.generate_fake_phone()
