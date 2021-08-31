# s = 'My Name is Julia'

# if 'Name' in s:
#     print('Substring found')

# index = s.find('Name')
# if index != -1:
#     print(f'Substring found at index {index}')


# def test_substring(full_string, substring):
#     # ваша реализация, напишите assert и сообщение об ошибке
#     assert full_string.find(substring) != -1, \
#         "expected {!r} to be substring of {!r}".format(substring, full_string)

numerator = 10
divisor = 0
try:
    result = numerator / divisor
except ZeroDivisionError as e:
    result = None