def validar_notas(notas):    
    # isInstance -> Pode verificar se um objeto pertence a um de vários tipos, passando uma tupla: isinstance(x, (int, float))
    if not isinstance(notas, list):
        return False

    if len(notas) == 0:
        return False

    for nota in notas:
        if not isinstance(nota, (int, float)):
            return False

    return True

def calcular_media(notas):
    return sum(notas) / len(notas)
