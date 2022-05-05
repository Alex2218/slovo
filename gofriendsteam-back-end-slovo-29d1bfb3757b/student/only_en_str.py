list_ = [
    'some string',
    'asdasdasd5',
    'asdasdasd3',
    'пропустить',
    'asdasdasdфы4',
    'asdasdыфыфвфывasdasd',
    'asdasdasd12',
]
new_list = []

for s in list_:
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError as e:
        new_list.append(s)
        print(e, type(e), s)

print(new_list)