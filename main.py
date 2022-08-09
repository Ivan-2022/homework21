from request import Request, store, shop


def main():
    print('Привет\n')
    print("Формат ввода команды:")
    print("Доставить 5 печеньки из склад в магазин")
    print("Доставить 1 печеньки из магазин на склад")
    print("Доставить 10 печеньки из ниоткуда на склад")
    print("Доставить 2 печеньки из магазин в никуда\n")
    while True:
        print(f"В склад хранится:\n{store}")
        print(f"В магазин хранится:\n{shop}\n")
        user_input = input("Введите команду:\n"
                           "Если хотите закончить, введите команду 'стоп'\n").lower()
        if user_input == 'стоп':
            break
        else:
            request = Request(user_input)
            request.move()


if __name__ == '__main__':
    main()
