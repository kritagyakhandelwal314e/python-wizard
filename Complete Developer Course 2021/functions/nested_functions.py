def sum(list_in):
    '''
    Info: this function returns the sum of list passed
    param list_in=list
    '''
    def _sum(n1, n2):
        return n1 + n2
    total = 0
    for item in list_in:
        total = _sum(total, item)
    return total


total = sum([1, 2, 3, 4, 5, 6, 7])
print(total)