sintomas = [
    "Congestión leve", "Congestión moderada", "Congestión severa",
    "Fatiga ligera", "Fatiga moderada", "Fatiga severa",
    "Dolor leve de cabeza", "Dolor moderado de cabeza", "Dolor intenso de cabeza",
    "Fiebre baja", "Fiebre moderada", "Fiebre alta",
    "Tos leve", "Tos moderada", "Tos intensa",
    "Dificultad respiratoria leve", "Dificultad respiratoria moderada", "Dificultad respiratoria severa",
    "Náuseas leves", "Náuseas severas"
]

def mapear_sintomas(s1, s2, s3):
    return [
        (s1, sintomas[s1 - 1]),
        (s2, sintomas[s2 - 1]),
        (s3, sintomas[s3 - 1])
    ]

def clasificar_enfermedad(s1, s2, s3):
    sintomas_combinados = mapear_sintomas(s1, s2, s3)
    descripciones = [desc for _, desc in sintomas_combinados]

    if any(x in descripciones for x in ["Congestión leve", "Fatiga ligera", "Dolor leve de cabeza"]):
        resultado = "NO ENFERMO"
    elif any(x in descripciones for x in ["Fiebre baja", "Tos leve", "Dolor moderado de cabeza"]):
        resultado = "ENFERMEDAD LEVE"
    elif any(x in descripciones for x in ["Fiebre alta", "Tos intensa", "Dificultad respiratoria moderada"]):
        resultado = "ENFERMEDAD AGUDA"
    else:
        resultado = "ENFERMEDAD CRÓNICA"

    return resultado, sintomas_combinados

def predecir_enfermedad(s1, s2, s3):
    return clasificar_enfermedad(s1, s2, s3)
