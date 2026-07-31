from app.models.predictor import label_encoders

# Valores alternativos para que la API sea más flexible
MAPEO_VALORES = {
    "calidad_combustible": {
        "alta": "NORMAL",
        "media": "NORMAL",
        "baja": "DEGRADADA",
    },
    "nivel_aceite": {
        "bueno": "NORMAL",
        "regular": "NORMAL",
        "malo": "DEGRADADA",
    },
    "estado_frenos": {
        "bueno": "NORMAL",
        "regular": "NORMAL",
        "malo": "DEGRADADA",
    },
    "filtro_aire": {
        "limpio": "NORMAL",
        "sucio": "CONTAMINADA",
    },
    "condicion_via": {
        "buena": "NORMAL",
        "regular": "NORMAL",
        "mala": "DEGRADADA",
    }
}


def codificar_datos(datos):
    for columna, encoder in label_encoders.items():
        if columna not in datos:
            continue

        valor = str(datos[columna]).strip()

        # Buscar si existe un mapeo para ese campo
        if columna in MAPEO_VALORES:
            valor = MAPEO_VALORES[columna].get(valor.lower(), valor)

        # Buscar ignorando mayúsculas/minúsculas
        encontrado = None
        for clase in encoder.classes_:
            if clase.strip().lower() == valor.strip().lower():
                encontrado = clase
                break

        if encontrado is None:
            raise ValueError(
                f"El valor '{valor}' en la columna '{columna}' no es válido. "
                f"Valores permitidos: {list(encoder.classes_)}"
            )

        datos[columna] = encoder.transform([encontrado])[0]

    return datos