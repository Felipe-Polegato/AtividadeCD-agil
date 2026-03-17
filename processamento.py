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


def analisar_alunos(lista_alunos):
    resultados = []
    recuperacao = []

    top_student = None
    maior_media = 0

    for nome, notas in lista_alunos:

        if not validar_notas(notas):
            print(f"Os dados são inválidos para aluno(a) {nome}")
            continue

        media = calcular_media(notas)

        aluno = {
            "nome": nome,
            "media": round(media, 2) #Round arredonda um número float
        }

        resultados.append(aluno)

        if media < 7:
            recuperacao.append(nome)

        if media > maior_media:
            maior_media = media
            top_student = nome

    return resultados, recuperacao, top_student