def input_error(func):
    def wrapper(*args):
        try:
            if not args[1].isalpha():
                raise KeyError
            if func.__name__ != "phone":
                if not args[2].isdecimal():
                    raise ValueError
            return func(*args)
        except KeyError:
            return "Enter user name correctly"
        except ValueError:
            return "Enter phone number correctly"
        except IndexError:
            return "Give me name (and phone is needed) please"
    return wrapper


@input_error
def add(*args):
    result = ""
    for key in phone_book.keys():
        if key.casefold() == args[1].casefold():
            result = "The contact is exist"
            break
    if not result:
        phone_book[args[1].title()] = args[2]
        result = "Add success"
    return result


@input_error
def change(*args):
    result = ""
    for key in phone_book.keys():
        if key.casefold() == args[1].casefold():
            phone_book[args[1].title()] = args[2]
            result = "Change success"
            break
    if not result:
        result = "The contact is not found"
    return result


def exit():
    return "Good bye!"


def hello():
    return "Can I help you?"


def no_command():
    return "Unknown command"


@input_error
def phone(*args):
    result = ""
    for key, value in phone_book.items():
        if key.casefold() == args[1].casefold():
            result = f"The contact:\n{key}: {value}\n"
            break
    if not result:
        result = "The contact is not found"
    return result


def show_all():
    if not phone_book:
        result = "The phone book is empty"
    else:
        result = "All contacts:\n"
        for key, value in phone_book.items():
            result += f"{key}: {value}\n"
    return result


def parser(text: str) -> tuple[callable, tuple[str]|None]:
    if text.casefold().startswith("add"):
        return add, text.strip().split()
    elif text.casefold().startswith("change"):
        return change, text.strip().split()
    elif text.casefold() == "good bye" or text.casefold() == "bye" or text.casefold() == "close" or text.casefold() == "exit":
        return exit, None
    elif text.casefold() == "hello":
        return hello, None
    elif text.casefold().startswith("phone"):
        return phone, text.strip().split()
    elif text.casefold() == "show all":
        return show_all, None
    return no_command, None


def main():
    while True:
        user_input = input(">>> ")
        command, data = parser(user_input)
        if data:
            result = command(*data)
        else:
            result = command()
        print(result)
        if result == "Good bye!":
            break


if __name__ == "__main__":
    phone_book = {}
    main()