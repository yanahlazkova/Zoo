# Класс створення меню
class Menu:
    exit_item = 0
    def __init__(self, menu_title, menu_list: list):
        self.__menu_title = menu_title
        self.__menu_list = menu_list
        self.exit_item = len(menu_list) + 1

    # функція виводу Меню
    def display_menu(self):
        # Виводить загловок меню
        print()
        border = "*" * 40
        print(border.rjust(80, " "))

        print('*'.rjust(41, ' '), end="")
        print(self.__menu_title.center(37, ' '), '*')

        print(border.rjust(80, " "))
        print()
        self.display_menu_items()

    def display_menu_items(self):
        # Виводить пункти меню
        for index, menu in enumerate(self.__menu_list):
            print(" " * 47, index + 1, menu['menu_title'])
        print(" " * 47, len(self.__menu_list) + 1, 'EXIT')

    def get_user_choice(self):
        # Повертає номер пункту, який обрав користувач
        while True:
            try:
                # Чекаємо ввод користувача
                choice = input(f'\n{" " * 40}Select menu item:\t')
                choice = int(choice)
                # Перевіряємо, що число знаходиться в допустимому діапазоні
                if 1 <= choice <= len(self.__menu_list) + 1:
                    return choice
                else:
                    print(f"Please enter a number between 1 and {len(self.__menu_list) + 1}.")

            except ValueError:
                print("Invalid input. Please enter a number.")

    @property
    def menu_list(self):
        return self.__menu_list

    @property
    def menu_title(self):
        return self.__menu_title


class SubMenu(Menu):
    def __init__(self, menu_title, menu_list: list):
        super().__init__(menu_title, menu_list)
        # self.__menu_title = menu_title

    def display_menu_items(self):
        for index, menu in enumerate(self.menu_list):
            print(" " * 47, index + 1, menu)
        print(" " * 47, len(self.__menu_list) + 1, 'EXIT')
