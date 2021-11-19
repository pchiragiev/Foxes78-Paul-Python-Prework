import datetime as dt

def hello_name(user_name):
    # print("hello_" + user_name + "!")
    print(f"hello_{user_name}!")


def first_odds():
    for i in range(1, 101):
        if i % 2 == 1:
            print(i)


def max_num_in_list(a_list):
    return max(a_list)


def is_leap_year(a_year):
    result = False
    if a_year % 4 == 0 and (a_year % 100 != 0 or a_year % 400 == 0):
       result = True
    return result


def is_consecutive(a_list):
    result = True
    p = a_list[0]
    for i in a_list[1:]:
        if i - p != 1:
            result = False
            break
        p = i
    return result
        

if __name__ == "__main__":
    hello_name("Paul")
    first_odds()
    print(max_num_in_list([54, 23, 83, 1, 104]))
    print(is_leap_year(1997))
    print(is_consecutive([1, 2, 3, 4, 5, 6, 7, 8, 9]))