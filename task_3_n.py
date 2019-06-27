def adv_print(*args, **kwargs):
    string = ''
    mn = ''
    for arg in args:
        string += str(f' {arg}')
        # string = string.lstrip()
    if 'start' in kwargs.keys():
        start = kwargs['start']
    else:
        start = '\n'
    if 'max_line' in kwargs.keys():
        max_line = kwargs['max_line']
        if len(string) > max_line:
            mn = '\n'
    finish_string = mn + start + string
    if 'in_file' in args:
        print(finish_string.replace('in_file', ''))
        with open('text.txt', 'w', encoding='utf-8') as f:
            f.write(finish_string.replace('in_file', ''))
    else:
        print(finish_string)


adv_print('привет', 'пока', 'in_file', start='с чего начинается вывод', max_line=65)
adv_print('goo', 6669, 111)
