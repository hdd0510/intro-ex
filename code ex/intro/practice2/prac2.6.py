def dec_to_bin(n):
    if n == 1:
        return 1
    elif n % 2 == 1:
        return str(dec_to_bin(n//2)) + str(1)
    else:
        return str(dec_to_bin(n//2)) + str(0)  
print(dec_to_bin(18))


#C2:
#def DecimalToBinary(num):
#    if num >= 1:
#        DecimalToBinary(num // 2)
#    print(num % 2, end = '')
