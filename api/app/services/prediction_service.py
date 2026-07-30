import pandas as pd

from app.models.predictor import modelo
from app.utils.encoder import codificar_datos


def realizar_prediccion(datos):
    """
    Convierte los datos recibidos, los codifica y ejecuta la predicción.

    Retorna una tupla (prediccion, probabilidad) donde:
    - prediccion: int (0 o 1)
    - probabilidad: float (confianza de la predicción) o None si no está disponible.
    """
    datos = datos.model_dump()

    datos = codificar_datos(datos)

    df = pd.DataFrame([datos])

    prediccion = modelo.predict(df)[0]

    # Intentar obtener probabilidad si el modelo lo soporta
    probabilidad = None
    if hasattr(modelo, "predict_proba"):
        probas = modelo.predict_proba(df)[0]
        # Para clasificación binaria, tomar la probabilidad de la clase 1
        if len(probas) == 2:
            probabilidad = round(float(probas[1]), 4)
        else:
            probabilidad = round(float(probas[prediccion]), 4)

    return int(prediccion), probabilidad