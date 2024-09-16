Задача: Система управління зоопарком
Опис:
Створіть систему управління зоопарком, яка дозволить додавати тварин, персонал, відслідковувати їх розміщення у вольєрах і управління графіками годування. Система має використовувати об'єктно-орієнтоване програмування для моделювання відносин між різними об'єктами.

Вимоги:
Класи:

Animal: Тварина з атрибутами name, species, age.
Enclosure: Вольєр з атрибутами enclosure_id, size, animals (список тварин, які знаходяться у вольєрі).
Zookeeper: Персонал, який опікується тваринами, з атрибутами name, employee_id, assigned_enclosures (список вольєрів, за якими він відповідає).
Наслідування:

Можна створити базовий клас Person для атрибутів, які спільні між Zookeeper та можливими іншими персоналами (наприклад, гіди).
Методи:

Enclosure.add_animal(animal): Додає тварину до вольєра.
Enclosure.remove_animal(animal): Видаляє тварину з вольєра.
Zoo.add_enclosure(enclosure): Додає вольєр до зоопарку.
Zoo.assign_zookeeper(zookeeper, enclosure_id): Призначає зоопарку відповідати за вольєр.# Zoo