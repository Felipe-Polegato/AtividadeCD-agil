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

def gerar_relatorio(resultados, recuperacao, top_student):
    # with = Garante que o arquivo será fechado no final, mesmo que ocorra algum erro
    # open = abre algum arquivo
    # 'w' = significa que algum arquivo vai ser criado e/ou aberto
    # encoding="utf-8" = codificação de caracteres (permite escrever acentos)
    with open("resultado.txt", "w", encoding="UTF-8") as arquivo:

        # arquivo.write grava texto ou algum dado em um arquivo aberto antes / é como se fosse um print que ainda não foi escrito
        arquivo.write("RELATÓRIO DE DESEMPENHO - ALUNOS SENAI 1.34\n")
        arquivo.write("=" * 30)

        arquivo.write("\nMÉDIAS DOS ALUNOS\n\n")

        for aluno in resultados:
            arquivo.write(f"- {aluno['nome']} com Média: {aluno['media']}\n")

        arquivo.write("\n")
        arquivo.write("=" * 30)
        arquivo.write("\n")
        
        arquivo.write("ALUNOS EM RECUPERAÇÃO\n")

        if recuperacao:
            for nome in recuperacao:
                arquivo.write(f"- {nome}\n")
        else:
            arquivo.write("Nenhum aluno em recuperação\n")

        arquivo.write("=" * 30)
        arquivo.write("\n")

        arquivo.write(f"TOP STUDENT: {top_student}.\nParabéns por toda sua dedicação nas aulas!\n")
        arquivo.write("=" * 30)