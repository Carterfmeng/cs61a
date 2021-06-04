def mul_recur(m,n):
    if m == 0 or n == 0:
        return 0
    else:
        return m + mul_recur(m, n - 1)

def count_up(n):
    if n == 1:
        print(n)
    else:
        count_up(n-1)
        print(n)

def sum_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_digits(n // 10)

def count_k(n, k):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        total = 0
        i = 1
        while  i <= k:
            total += count_k(n - i, k)
            i +=1 
        return total



def count_k_recur(n, k):
    def decre_k(m, k):
        if m > k:
            return 0
        else:
            return count_k_recur(n - m, k) + decre_k(m + 1, k)

    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        return decre_k(1, k)

