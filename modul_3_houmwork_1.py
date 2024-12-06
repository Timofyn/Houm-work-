calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()

def is_contains(string, list_to_search):
    count_calls()
    for i in list_to_search:
        if i == string:
            return True
        else:
            return False

print(string_info('popygai'))
print(string_info('Foto'))
print(is_contains('tot', ['iok', 'uot', 'ToT']))
print(calls)
