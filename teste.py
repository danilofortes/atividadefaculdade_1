av1 = float(input("Digite a nota da AV1: "))
av2 = float(input("Digite a nota da AV2: "))
notas = [av1, av2]
if av1 < 4 and av2 < 4:
    print("O aluno foi reprovado.")
    if av1 >= 6 and av2 >= 6:
        print("o aluno está aprovado.")
else:
    if av1 < 4:
        print("O aluno terá que fazer a Nova Chance na AV1.")
        av1_nova_chance = float(input("Digite a nota da Nova Chance da AV1: "))
        notas.append(av1_nova_chance)
    else:
        av1_nova_chance = av1

    if av2 < 4:
        print("O aluno terá que fazer a Nova Chance na AV2.")
        av2_nova_chance = float(input("Digite a nota da Nova Chance da AV2: "))
        notas.append(av2_nova_chance)
    else:
        av2_nova_chance = av2

    media_avaliacoes = (av1_nova_chance + av2_nova_chance) / 2
    if media_avaliacoes >= 6:
        print("O aluno foi aprovado.")
    else:
        print("O aluno terá que fazer a AV3.")
        av3 = float(input("Digite a nota da AV3: "))
        notas.append(av3)
        notas.sort()
        print(f"{notas}")
        media_final = (notas[1] + notas[2]) / 2
        if media_final >= 6:
            print("O aluno foi aprovado.")
        else:
            print("O aluno está reprovado.")
