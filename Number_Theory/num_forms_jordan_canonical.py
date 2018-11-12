def get_num_forms_jordan_canonical(n):
    total = 0
    for i in range(1, n+1):
        val = i + get_num_forms_jordan_canonical(n-i)
        print(val)
        if val == 0:
            break
        if val == n:
            total += 1
    return total


n = 2
print(get_num_forms_jordan_canonical(n))
