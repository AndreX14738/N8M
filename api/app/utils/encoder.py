from app.models.predictor import label_encoders


def codificar_datos(datos):
    """Convierte variables categóricas usando los LabelEncoder guardados.

    Lanza una excepción si una categoría no existe durante el entrenamiento,
    con un mensaje claro indicando qué columna y valor son problemáticos.
    """
    for columna, encoder in label_encoders.items():
        if columna in datos:
            valor = datos[columna]
            # Intentar coincidencia exacta primero
            if valor in encoder.classes_:
                datos[columna] = encoder.transform([valor])[0]
            else:
                # Buscar coincidencia ignorando mayúsculas/minúsculas y espacios
                valor_normalizado = valor.strip().lower()
                encontrado = None
                for clase in encoder.classes_:
                    if clase.strip().lower() == valor_normalizado:
                        encontrado = clase
                        break

                if encontrado is not None:
                    datos[columna] = encoder.transform([encontrado])[0]
                else:
                    raise ValueError(
                        f"El valor '{valor}' en la columna '{columna}' no fue visto durante el entrenamiento. "
                        f"Valores válidos: {list(encoder.classes_)}"
                    )
    return datos
