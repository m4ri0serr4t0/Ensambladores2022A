binario = '1010111B'


def validaBinario(string):
    # set function convert string
    # into set of characters .
    p = set(string)

    # declare set of '0', '1' .
    s = {'0', '1'}

    # check set p is same as set s
    # or set p contains only '0'
    # or set p contains only '1'
    # or not, if any one condition
    # is true then string is accepted
    # otherwise not .
    if s == p or p == {'0'} or p == {'1'}:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    print(validaBinario(binario))
