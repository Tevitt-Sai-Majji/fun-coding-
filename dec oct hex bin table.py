def print_formatted(number):
    w=len(bin(number)[2:])
    for i in range(1,number+1):
        print (' ' + (str(i).rjust(w).rjust((len(str(n))), ' ')) + (str(oct(i))[2:].rjust(w+1)) + ((str(hex(i))[2:].upper()).rjust(w+1)) + (str(bin(i))[2:].upper().rjust(w+1)))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
