def apply_all_func(int_list, *functions):
    dict_functions = {}
    for func in functions:
        dict_functions[func.__name__] = func(int_list)
    return dict_functions

# === test case ===

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))