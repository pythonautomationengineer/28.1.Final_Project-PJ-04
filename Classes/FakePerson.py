from faker import Faker
import random

fake = Faker('ru_RU')


# Возможно в 1 случае из 100 или 100000 сгенерируется не то, на что я рассчитывал, из-за какого то окончания,
# которое я не учел, но тесты из-за этого не упадут, поэтому это не страшно.

class FakePerson:
    """Генерация необходимых тестовых данных: имени, фамилии, отчества и телефона с помощью рекурсии 💖"""
    max_length_last_name = 10  # задает максимальную длину фамилии
    max_length_first_name = 10  # задает максимальную длину имени
    max_length_patronymic_name = 12  # задает максимальную длину отчества
    length_phone = 11  # задает длину номера телефона

    @staticmethod
    def generate_last_name_of_man(old_last_name):
        """Генерация мужской фамилии"""
        name = fake.name()
        list_name = name.split()
        if old_last_name != list_name[0] and 4 < len(list_name[0]) < FakePerson.max_length_last_name \
                and list_name[0][-2:] in {'ов', 'ев', 'ёв', 'ин'}:
            return list_name[0]
        else:
            return FakePerson.generate_last_name_of_man(old_last_name)

    @staticmethod
    def generate_first_name_of_man(old_first_name):
        """Генерация мужского имени"""
        name = fake.name()
        list_name = name.split()
        if old_first_name != list_name[1] and 4 < len(list_name[1]) < FakePerson.max_length_first_name \
                and list_name[1][-2:] not in {'ов', 'ев', 'ёв', 'ин', 'ич', 'на', 'ва', 'ия', 'са', 'ра', 'та', 'вь',
                                              'да', 'ья', 'га', 'ла', 'оя', 'фа', 'ея', 'ор', 'ка', 'ца', 'ия', 'ль',
                                              'ма', 'ея', 'а', 'вь', 'ь'}:
            return list_name[1]
        else:
            return FakePerson.generate_first_name_of_man(old_first_name)

    @staticmethod
    def generate_patronymic_name_of_man(old_patronymic_name):
        """Генерация мужского имени"""
        name = fake.name()
        list_name = name.split()
        if old_patronymic_name != list_name[2] and 4 < len(list_name[2]) < FakePerson.max_length_patronymic_name and \
                list_name[2][-2:] in {'ич'}:
            return list_name[2]
        else:
            return FakePerson.generate_patronymic_name_of_man(old_patronymic_name)

    @staticmethod
    def generate_fake_phone():
        """Генерация случайного номера, с некоторыми доработками под требования соответствующего поля формы
        на тестируемом сайте"""
        operators = ['790', '791', '792', '795']  # несколько операторов
        phone = fake.phone_number()
        if len(phone) == FakePerson.length_phone and phone[0:1] == '8':
            return operators[random.randint(0, 3)] + f'{phone[3:]}'
        else:
            return FakePerson.generate_fake_phone()


print(FakePerson.generate_fake_phone())
