def hacer_la_vaca(salon: list, vaca: str) -> list:
    result = []
    mayor_i = 0
    mayor_j = 0
    tot = 0
    for i in range(0, len(salon)):
        for j in range(0, len(salon[i])):
            if salon[i][j] > salon[mayor_i][mayor_j]:
                mayor_i = i
                mayor_j = j
            tot += salon[i][j]

    if (vaca == 'botella' and tot >= 120000) or (vaca == 'pastel' and tot >= 35000):
        result.append("Hay Vaca")
    else:
        result.append("No Alcanza")
    result.append([mayor_i, mayor_j])

    return result

salon = [ [1,12121,1212,345,678,4], [2, 3, 101,121212,-1,1212], [12000, 100000]]
print(hacer_la_vaca(salon,"pastel"))