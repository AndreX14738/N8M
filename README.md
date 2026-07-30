# 🚗 API - Predicción de Fallas Vehiculares

API desarrollada con **FastAPI** que utiliza **Machine Learning** para predecir fallas vehiculares en Bolivia.

---

## 🚀 Cómo ejecutar el proyecto

### 1. Instalar dependencias

```bash
cd api
pip install -r requirements.txt
```

### 2. Iniciar el servidor

```bash
uvicorn app.main:app --reload
```

El servidor se iniciará en: **http://127.0.0.1:8000**

---

## 📡 Endpoints disponibles

### 1️⃣ **GET /** — Verificar que la API funciona

**URL:** [http://127.0.0.1:8000](http://127.0.0.1:8000)

**Respuesta:**
```json
{
  "mensaje": "API funcionando correctamente"
}
```

### 2️⃣ **POST /predict** — Predecir falla vehicular

**Documentación interactiva (Swagger):** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

También puedes consumir el endpoint con `curl`:

```bash
curl -X POST http://127.0.0.1:8000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "region": "La Paz",
    "altitud_msnm": 3640.0,
    "marca": "Toyota",
    "tipo_vehiculo": "Sedan",
    "año_fabricacion": 2018.0,
    "antiguedad_años": 6.0,
    "kilometraje": 85000.0,
    "ultimo_mantenimiento_dias": 45.0,
    "calidad_combustible": "Premium",
    "octanaje_estimado": 95.0,
    "contaminacion_agua_ppm": 12.5,
    "temperatura_motor_c": 90.0,
    "nivel_aceite": "Normal",
    "presion_neumaticos_psi": 32.0,
    "bateria_voltaje": 12.5,
    "estado_frenos": "Bueno",
    "filtro_aire": "Limpio",
    "tipo_via": "Urbana",
    "condicion_via": "Buena",
    "temperatura_ambiente_c": 18.0
  }'
```

**Respuesta esperada:**
```json
{
  "prediccion": 0,
  "mensaje": "No se detecta una alta probabilidad de falla",
  "probabilidad": 0.12
}
```

---

## 📦 Estructura del proyecto

```
api/
├── app/
│   ├── main.py                  # Endpoints de la API
│   ├── models/
│   │   └── predictor.py         # Carga del modelo ML
│   ├── schemas/
│   │   └── vehicle.py           # Esquema de datos del vehículo
│   ├── services/
│   │   └── prediction_service.py# Lógica de predicción
│   └── utils/
│       └── encoder.py           # Codificación de variables
├── modelo/
│   ├── modelo.pkl               # Modelo entrenado
│   └── label_encoders.pkl       # Codificadores de etiquetas
└── requirements.txt             # Dependencias
```

---

## 🛠️ Tecnologías

- **FastAPI** — Framework web
- **Uvicorn** — Servidor ASGI
- **scikit-learn** — Modelo de Machine Learning
- **pandas / numpy** — Procesamiento de datos
- **joblib** — Serialización del modelo