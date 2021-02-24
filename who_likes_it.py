def likes(names):
    s = ''
    if len(names) == 0:
        s += 'no one likes this'
    if len(names) == 1:
        s += names[0]
        s += ' likes this'
    if len(names) >= 2:
        if len(names) == 2:
            s += names[0]
            s += ' and '
            s += names[1]
        if len(names) >= 3:
            s += names[0] + ', ' + names[1]
            if len(names) == 3:
                s += ' and ' + names[2]
            else:
                s += ' and ' + str(len(names) - 2) + ' others'
        s += ' like this'
    return s
