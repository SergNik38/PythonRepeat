keys = ['key1', 'key2', 'key3', 'key4']
values = ['val1', 'val2', 'val3']

result = {}
for el in keys:
    try:
        result[el] = values[keys.index(el)]
    except IndexError:
        result[el] = None

print(result)
