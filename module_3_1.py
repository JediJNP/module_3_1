print('Счётчик вызовов')

calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    string_count = len(string)
    string_upper = string.upper()
    string_lower = string.lower()
    string = string_count, string_upper, string_lower
    print(string)

def is_contains(string , list_to_search):
    count_calls()
    condition = False
    string = string.lower()
    for i in range(len(list_to_search)):
        current = list_to_search[i]
        list_to_search[i] = current.lower()
        if list_to_search[i] == string:
            condition = True
            break

    print(condition)
#######################
string = 'Urban'
list_to_search = ['ban', 'urBAN' , 'BaNaN']
string_info(string)
is_contains(string , list_to_search)

string = 'cycle'
list_to_search = ['REcycling', 'cyCLic']
string_info(string)
is_contains(string , list_to_search)
print('Сколько раз вызваны функции: ' , calls)
