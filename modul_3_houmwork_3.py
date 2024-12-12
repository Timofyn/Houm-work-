def print_params(a=9, b='Trun', c=None):
    print(a, b, c)


print_params(b=25)
print_params(c=[1, 2, 3])
values_list = ['#&%', 745.678, 897]
values_dict = {'a': True, 'b': 890, 'c': 'i_will_be_back'}
print_params(**values_dict)
print_params(*values_list)
values_list_2 = [458, 7940.656]
print_params( *values_list_2, 42)
