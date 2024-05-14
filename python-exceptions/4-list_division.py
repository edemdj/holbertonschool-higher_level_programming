#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = [0 for _ in range(list_length)]
    for i in range(list_length):

        try:
            result = (my_list_1[i] / my_list_2[i])
        except TypeError:
            print("wrong type")
            continue
        except ZeroDivisionError:
            print("division by 0")
            continue
        except IndexError:
            print("out of range")
            continue
        finally:
            new_list[i] = result
    return new_list
