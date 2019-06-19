def adv_print(*args, **kwargs):
    def func_start():
        if kwargs == {}:
            start = '\n'
        else:
            start = kwargs
        return start
    def func_max_line(max_line):
        # if len(args) > max_line:
        print(max_line)
        print(args)
        print(kwargs)

    for i in args:
        print(f'{func_start()}{i}')
        func_max_line(args)


adv_print(6, 'hello world', 9, 0)