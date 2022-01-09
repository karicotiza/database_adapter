import pymysql as sql  # Библиотека для работы с MySQL
from config import host, user, port, password, db_name  # Импорт данных для подключения к базе данных


def show(connection, user_choice):
    with connection.cursor() as cursor:
        if 0 < user_choice < 8:
            if user_choice == 1:
                print(
                    "1. Просмотр информации о производственных участках\n" +
                    "2. Добавление информации о производственных участках\n" +
                    "3. Редактирование информации о производственных участках\n" +
                    "4. Удаление информации о производственных участках\n"
                )
                x = int(input("Выберите действие: "))
                if x == 1:
                    action = str(
                        "SELECT * " +
                        "FROM section"
                    )

                    output = True
                elif x == 2:
                    idsection = str(input("Введите id производственного участка: "))
                    title = str(input("Введите название производственного участка: "))
                    equipment = str(input("Введите тип оборудования: "))
                    idequipment = str(input("Введите id оборудования: "))
                    action = str(
                        "insert into section " +
                        "(idsection, title, equipment, idequipment) " +
                        "values ('" + idsection + "', '" + title + "', '" + equipment + "', '" + idequipment + "'); "
                    )

                    print(f"Данные успешно добавлены")
                    output = False
                elif x == 3:
                    idsection = str(input("Введите id производственного участка данные о котором хотите изменить: "))
                    title = str(input("Введите название производственного участка: "))
                    equipment = str(input("Введите тип оборудования: "))
                    idequipment = str(input("Введите id оборудования: "))
                    action = str(
                        "update section " +
                        "set title = '" + title + "', " +
                        "equipment = '" + equipment + "', " +
                        "idequipment = '" + idequipment + "' " +
                        "where idsection = '" + idsection + "'; "
                    )

                    print(f"Значение {idsection} успешно изменено")
                    output = False
                elif x == 4:
                    idsection = str(input("Введите id производственного участка данные о котором хотите удалить: "))
                    action = str(
                        "delete from section " +
                        "where idsection = '" + idsection + "'; "
                    )

                    print(f"Данные {idsection} успешно удалены")
                    output = False
                else:
                    print("Неопределенное действие")
            if user_choice == 2:
                print(
                    "1. Просмотр информации об оборудовании\n" +
                    "2. Добавление информации об оборудовании\n" +
                    "3. Редактирование информации об оборудовании\n" +
                    "4. Удаление информации об оборудовании\n"
                )
                x = int(input("Выберите действие: "))
                if x == 1:
                    action = str(
                        "SELECT * " +
                        "FROM equipment"
                    )

                    output = True
                elif x == 2:
                    idequipment = str(input("Введите id оборудования: "))
                    title = str(input("Введите название оборудования: "))
                    action = str(
                        "insert into equipment " +
                        "(idequipment, title) " +
                        "values ('" + idequipment + "', '" + title + "'); "
                    )

                    print(f"Данные успешно добавлены")
                    output = False
                elif x == 3:
                    idequipment = str(input("Введите id оборудования данные о котором хотите изменить: "))
                    title = str(input("Введите название оборудования: "))
                    action = str(
                        "update equipment " +
                        "set title = '" + title + "' " +
                        "where idequipment = '" + idequipment + "'; "
                    )

                    print(f"Значение {idequipment} успешно изменено")
                    output = False
                elif x == 4:
                    idequipment = str(input("Введите id оборудования данные о котором хотите удалить: "))
                    action = str(
                        "delete from equipment " +
                        "where idequipment = '" + idequipment + "'; "
                    )

                    print(f"Данные {idequipment} успешно удалены")
                    output = False
                else:
                    print("Неопределенное действие")
            if user_choice == 3:
                print(
                    "1. Просмотр информации о техническом осмотре оборудования\n" +
                    "2. Добавление информации о техническом осмотре оборудования\n" +
                    "3. Редактирование информации о техническом осмотре оборудования\n" +
                    "4. Удаление информации о техническом осмотре оборудования\n"
                )
                x = int(input("Выберите действие: "))
                if x == 1:
                    action = str(
                        "SELECT * " +
                        "FROM inspection"
                    )

                    output = True
                elif x == 2:
                    idinspection = str(input("Введите id технического осмотра оборудования: "))
                    date = str(input("Введите дату технического осмотра оборудования: "))
                    result = str(input("Введите результат технического осмотра оборудования: "))
                    reason = str(input("Введите причину результата: "))
                    idequipment = str(input("Введите id оборудования: "))
                    idemployee = str(input("Введите id сотрудника: "))
                    action = str(
                        "insert into inspection " +
                        "(idinspection, date, result, reason, idequipment, idemployee) " +
                        "values ('" + idinspection + "', '" + date + "', '" + result + "', '" + reason +
                        "', '" + idequipment + "', '" + idemployee + "'); "
                    )

                    print(f"Данные успешно добавлены")
                    output = False
                elif x == 3:
                    idinspection = str(input("Введите id технического осмотра оборудования которого хотите изменить: "))
                    date = str(input("Введите дату технического осмотра оборудования: "))
                    result = str(input("Введите результат технического осмотра оборудования: "))
                    reason = str(input("Введите причину результата: "))
                    idequipment = str(input("Введите id оборудования: "))
                    idemployee = str(input("Введите id сотрудника: "))
                    action = str(
                        "update inspection " +
                        "set date = '" + date + "', " +
                        "result = '" + result + "', " +
                        "reason = '" + reason + "', " +
                        "idequipment = '" + idequipment + "', " +
                        "idemployee = '" + idemployee + "' " +
                        "where idinspection = '" + idinspection + "'; "
                    )

                    print(f"Значение {idinspection} успешно изменено")
                    output = False
                elif x == 4:
                    idinspection = str(input(
                        "Введите id технического осмотра оборудования данные о котором хотите удалить: "
                    ))
                    action = str(
                        "delete from inspection " +
                        "where idinspection = '" + idinspection + "'; "
                    )

                    print(f"Данные {idinspection} успешно удалены")
                    output = False
                else:
                    print("Неопределенное действие")
            if user_choice == 4:
                print(
                    "1. Просмотр информации о сотрудниках технического отдела\n" +
                    "2. Добавление информации о сотрудниках технического отдела\n" +
                    "3. Редактирование информации о сотрудниках технического отдела\n" +
                    "4. Удаление информации о сотрудниках технического отдела\n"
                )
                x = int(input("Выберите действие: "))
                if x == 1:
                    action = str(
                        "SELECT * " +
                        "FROM employee"
                    )

                    output = True
                elif x == 2:
                    idemployee = str(input("Введите id сотрудника: "))
                    name = str(input("Введите Фамилию И.О. сотрудника: "))
                    position = str(input("Введите должность сотрудника: "))
                    action = str(
                        "insert into employee " +
                        "(idemployee, name, position) " +
                        "values ('" + idemployee + "', '" + name + "', '" + position + "'); "
                    )

                    print(f"Данные успешно добавлены")
                    output = False
                elif x == 3:
                    idemployee = str(input("Введите id сотрудника которого хотите изменить: "))
                    name = str(input("Введите Фамилию И.О. сотрудника: "))
                    position = str(input("Введите должность сотрудника: "))
                    action = str(
                        "update employee " +
                        "set name = '" + name + "', " +
                        "position = '" + position + "' " +
                        "where idemployee = '" + idemployee + "'; "
                    )

                    print(f"Значение {idemployee} успешно изменено")
                    output = False
                elif x == 4:
                    idemployee = str(input("Введите id сотрудника данные о котором хотите удалить: "))
                    action = str(
                        "delete from employee " +
                        "where idemployee = '" + idemployee + "'; "
                    )

                    print(f"Данные {idemployee} успешно удалены")
                    output = False
                else:
                    print("Неопределенное действие")
            elif user_choice == 5:
                action = str(
                    "select inspection.date, equipment.title, section.equipment, section.title, inspection.result, " +
                    "inspection.reason " +
                    "from inspection " +
                    "join equipment " +
                    "on equipment.idequipment = inspection.idequipment " +
                    "join section " +
                    "on section.idequipment = inspection.idequipment " +
                    "where inspection.result = 'Передать в ремонт' or inspection.result = 'Списать' "
                )

                output = True
            elif user_choice == 6:
                x = str(input("Введите инвентарный номер оборудования (Пример: eq###): "))
                action = str(
                    f"select equipment.idequipment, inspection.date, equipment.title, section.equipment, " +
                    "inspection.result " +
                    "from equipment " +
                    "join inspection " +
                    "on inspection.idequipment = equipment.idequipment " +
                    "join section " +
                    "on section.idequipment = equipment.idequipment " +
                    "where equipment.idequipment = '" + str(x) + "' "
                )

                output = True
            elif user_choice == 7:
                x = str(input("Введите дату (Пример: ГГГГ-ММ-ДД): "))
                action = str(
                    "select distinct inspection.date, employee.name, employee.position " +
                    "from employee " +
                    "join inspection " +
                    "on inspection.idemployee = employee.idemployee " +
                    " where inspection.date = '" + str(x) + "' "
                )

                output = True

            if output:
                cursor.execute(action)
                line = cursor.fetchall()
                if len(line) == 0:
                    print("Таких данных в БД нет")
                else:
                    for text in line:
                        string = ""
                        for key in text:
                            temporary = str(key)
                            while len(temporary) <= 25:
                                temporary = temporary + " "
                            string = string + temporary + " | "
                    print(string)

                    for text in line:
                        string = ""
                        for key in text:
                            temporary = str(text[key])
                            while len(temporary) <= 25:
                                temporary = temporary + " "
                            string = string + temporary + " | "
                        print(string)
            else:
                cursor.execute(action)
                connection.commit()

        elif user_choice == 8:
            print("Работа завершена")
        else:
            print("Неопределенное действие")


def main():
    try:
        connection = sql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=db_name,
            cursorclass=sql.cursors.DictCursor
        )
        print("Соединение установлено.")
        try:
            while True:
                print(
                    "\n1. Просмотр/добавление/редактирование/удаление информации о производственных участках.\n" +
                    "2. Просмотр/добавление/редактирование/удаление информации об оборудовании.\n" +
                    "3. Просмотр/добавление/редактирование/удаление информации о техническом осмотре оборудования.\n" +
                    "4. Просмотр/добавление/редактирование/удаление информации о сотрудниках технического отдела.\n" +
                    "5. Просмотр списка отказавшего оборудования на участках предприятия.\n" +
                    "6. Просмотр истории технических осмотров оборудования с заданным инвентарным номером.\n" +
                    "7. Просмотр фамилии и должности сотрудников технического отдела на заданную дату.\n" +
                    "8. Выйти"
                )
                user_choice = int(input("\nВыберите действие: "))
                show(connection, user_choice)
                if user_choice == 8:
                    break
        finally:
            connection.close()
    except Exception as error:
        print("Нет доступа к БД")
        print(error)


if __name__ == '__main__':  # Если название файла "main.py"
    main()  # Запустить основную функцию
