from fastapi import FastAPI, HTTPException

from app.schemas.vehicle import VehicleData
from app.services.prediction_service import realizar_prediccion

app = FastAPI(
    title="API - Predicción de Fallas Vehiculares",
    description="API para predecir fallas utilizando Machine Learning",
    version="1.0.0"
)


@app.get("/")
def inicio():
    return {
        "mensaje": "API funcionando correctamente"
    }


@app.post("/predict")
def predecir(datos: VehicleData):
    try:
        prediccion, probabilidad = realizar_prediccion(datos)
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error interno en la predicción: {str(e)}"
        )

    if prediccion == 1:
        mensaje = "Alta probabilidad de falla"
    else:
        mensaje = "No se detecta una alta probabilidad de falla"

    respuesta = {
        "prediccion": prediccion,
        "mensaje": mensaje
    }

    if probabilidad is not None:
        respuesta["probabilidad"] = probabilidad

    return respuesta