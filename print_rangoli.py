def print_rangoli(size):
    # your code goes here
    for i in range(2*(size-1)+1):
        s = ''
        for j in range(4*(size-1)+1):
            c = calc_c(i,j,size)
            s += c
        print(s)


def calc_c(i,j,size):
    if j%2==1:
        return '-'
    j = j//2
    d = abs(i-size+1)+abs(j-size+1)
    c = chr(ord('a')+d) if d<size else '-'
    return c

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

