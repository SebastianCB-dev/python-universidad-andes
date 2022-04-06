def puede_tener_pase_version1(edad: int)->bool:
    puede = True
    if edad < 16:
        puede = False
    return puede

def puede_tener_pase_version2(edad: int)->bool:
    puede = False
    if edad >= 16:
        puede = True
    return puede

def puede_tener_pase_version3(edad: int)->bool:
    return edad >= 16
