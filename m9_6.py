def all_variants(text):
    num = len(text)
    for i in range(num):
        for j in range(num):
            if j + i == num: break
            yield text[j : j + i + 1]
# ===== test =====
a = all_variants("abcd")
for i in a:
    print(i)