def rect_into_rects(lngth, wdth):
    sqr_list = []
    if lngth == 0 or wdth == 0:
        return None
    elif lngth == wdth:
        return None
    while lngth != 0 and wdth != 0:
        if lngth > wdth:
            a = lngth // wdth
            lngth = lngth % wdth
            [sqr_list.append(wdth) for _ in range(a)]
        elif wdth > lngth:
            a = wdth // lngth
            wdth = wdth % lngth
            [sqr_list.append(lngth) for _ in range(a)]
        else:
            return None
    return squares_to_rect(sqr_list)

def squares_to_rect(list):
    # wandelt Quadrate in alle möglichen Rechtecke um nach folgendem Prinzip:
    # quadrate aller kombinationen mindestens zweier zahlen aus der lsite miteinander addieren und durch den größten wert der seite der addierten
    # quadrate teilen. das ergebnis X und die längste Seite Y sollen dann in folgender Form in der Liste squares ausgegeben werden:
    # "(Y * X)"
    squares = sorted(list, reverse=True)
    rectangles = []
    #print(list)
    i = 0
    for _ in range(len(squares)):
        j = len(squares)
        while i != j:
            area = 0
            for cur_sqr in range(i, j):
                area += squares[cur_sqr] ** 2
            if area % squares[i] == 0:
                long_side = area // squares[i]
                if check(long_side, squares, i) == True:
                    rectangles.append("({}*{})".format(long_side, squares[i]))
            j -= 1
        i += 1
    return rectangles

def check(longside, squares, i):
    # checks if long side of rectangle can be made by adding up the sides of one or more of the subsequent squares and therefore if the
    # rectangle is one that can be built by this arrangement of squares
    if longside == squares[i]:
        return False
    sum = 0
    for _ in range(i, len(squares)):
        sum += squares[_]
        if sum == longside:
            return True
    return False



# liste = [5,5,3,2,1,1]
# print(squares_to_rect(liste))

print(rect_into_rects(13, 5))
print(rect_into_rects(0, 0))
print(rect_into_rects(2, 0))
print(rect_into_rects(2, 2))