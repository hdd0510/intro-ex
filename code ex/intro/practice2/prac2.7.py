def sum_of_digit(n):
    a = str(n)[len(str(n))-1]
    if len(str(n)) == 1:
        return n
    return sum_of_digit(int(n/10)) + int(a)

#Cách 2
# def sum_of_digit( n ):
#    if n == 0:
#        return 0
#    return (n % 10 + sum_of_digit(int(n / 10)))
