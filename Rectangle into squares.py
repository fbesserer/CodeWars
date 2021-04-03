def sqInRect(lngth, wdth):
    sqr_list = []
    while (lngth and wdth) != 0:
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
    return sqr_list

# recursive solution
def sqInRect1(lng, wdth, recur = 0):
    if lng == wdth:
        return (None, [lng])[recur]            # wenn original function call wird None ausgegeben (None, lng)[0]
                                               # wenn recursive call wird lng ausgegeben (None, lng)[1]
    lesser = min(lng, wdth)
    return [lesser] + sqInRect1(lesser, abs(lng - wdth), recur = 1)

print(sqInRect1(3, 13))

