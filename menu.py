# Класс створення меню
class Menu:
    __exit_item = 0
    __menu_list = []
    __title = ''
    # def __init__(self, menu_title, menu_list: list):
    #     self.__menu_title = menu_title
    #     self.__menu_list = menu_list
    #     self.exit_item = len(menu_list) + 1

    @staticmethod
    def display_menu(title: str, menu_list):
        Menu.__menu_list = menu_list
        Menu.__title = title
        # функція виводу Меню
        # Виводить загловок меню
        print()
        border = "*" * 40
        print(border.rjust(80, " "))

        print('*'.rjust(41, ' '), end="")
        print(title.center(37, ' '), '*')

        print(border.rjust(80, " "))
        print()
        Menu.__display_menu_items()
        # cls.display_menu_items(cls.__menu_list)

    @classmethod
    def __display_menu_items(cls):
        # Виводить пункти меню
        for index, menu in enumerate(cls.__menu_list):
            print(" " * 47, index + 1, menu)
        print(" " * 47, len(cls.__menu_list) + 1, 'EXIT')

    @staticmethod
    def display_list(title, new_list):
        # Виводить список
        print()
        # border = "*" * 40
        # print(border.rjust(80, " "))

        print('***'.rjust(41, ' '), end="")
        print(title.center(27, ' '), '***')

        # print(border.rjust(80, " "))
        print()
        for index, menu in enumerate(new_list):
            print(f'{" " * 39}{index + 1}. {menu}')

    @staticmethod
    def get_user_choice(count_items):
        # Повертає номер пункту, який обрав користувач
        while True:
            try:
                # Чекаємо ввод користувача
                choice = input(f'\n{" " * 40}Select menu item:\t')
                choice = int(choice)
                # Перевіряємо, що число знаходиться в допустимому діапазоні
                if 1 <= choice <= count_items:
                    return choice
                else:
                    print(f"Please enter a number between 1 and {count_items}.")

            except ValueError:
                print("Invalid input. Please enter a number.")

    # @property
    # def menu_list():
    #     return cls.__menu_list
    #
    # @property
    # def menu_title(:
    #     return self.__menu_title


class SubMenu(Menu):
    # def __init__(self, menu_title, menu_list: list):
    #     super().__init__(menu_title, menu_list)

    def __display_menu_items(Menu):
        for index, menu in enumerate(Menu.__menu_list):
            print(" " * 47, index + 1, menu)
        print(" " * 47, len(menu_list) + 1, 'EXIT')
