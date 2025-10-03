def censo_salario(personas: list[tuple[int, float]]) -> list[tuple[str, int]]:
    SMVM = int(input("Ingrese el salario mínimo, vital y móvil: "))
    
    menos_1 = 0
    entre_1_2 = 0
    entre_2_4 = 0
    mas_4 = 0

    for persona in personas:
        if persona[1] < SMVM:
            menos_1 += 1
        elif SMVM <= persona[1] < 2 * SMVM:
            entre_1_2 += 1
        elif 2 * SMVM <= persona[1] < 4 * SMVM:
            entre_2_4 += 1
        else:
            mas_4 += 1
    
    a = "Menor que el salario mínimo, vital y móvil (SMVM)"
    b = "Entre un SMVM y dos SMVM"
    c = "Entre dos SMVM y 4 SMVM"
    d = "Mayor a 4 SMVM"

    censo = [
        (a, menos_1), 
        (b, entre_1_2),
        (c, entre_2_4),
        (d, mas_4)
    ]

    return censo