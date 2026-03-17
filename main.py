from processamento import analisar_alunos, gerar_relatorio


alunos = [
    ("Duda", [8.0, 6.4, 9.0]),
    ("Gustavo", [6.4, 7.2]),
    ("Polegato", [9.4, 10.0, 8.8]),
    ("Dayana", [7.7, 9.1, 7.5]),
    ("Gabi", [5.2])
]
resultados, recuperacao, top_student = analisar_alunos(alunos)

print("\nMEDIAS DOS ALUNOS 1.34\n")
print("=" * 30)

for aluno in resultados:
    print(f"{aluno['nome']} teve media: {aluno['media']}")

print("=" * 30)
print("\nALUNOS EM RECUPERACAO\n")

for nome in recuperacao:
    print(nome)

print("=" * 30)
print(f"\nTOP STUDENT: {top_student}\n")

gerar_relatorio(resultados, recuperacao, top_student)

print("=" * 30)
print("O Relatório foi gerado com sucesso: resultado.txt")
print("=" * 30)

print("Arquivo criado")