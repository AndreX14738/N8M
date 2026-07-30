import requests
import json

BASE_URL = "http://127.0.0.1:8000"

# Test 1: GET /
print("=" * 60)
print("TEST 1: GET /")
print("=" * 60)
try:
    r = requests.get(f"{BASE_URL}/")
    print(f"Status: {r.status_code}")
    print(f"Response: {r.json()}")
    print()
except Exception as e:
    print(f"ERROR: {e}")
    print()

# Test 2: POST /predict sin falla
print("=" * 60)
print("TEST 2: POST /predict (sin falla - prediccion 0)")
print("=" * 60)

datos = {
    "region": "Cochabamba",
    "altitud_msnm": 2500,
    "marca": "Toyota",
    "tipo_vehiculo": "Sedan",
    "año_fabricacion": 2020,
    "antiguedad_años": 6,
    "kilometraje": 50000,
    "ultimo_mantenimiento_dias": 120,
    "calidad_combustible": "Normal",
    "octanaje_estimado": 95,
    "contaminacion_agua_ppm": 5,
    "temperatura_motor_c": 90,
    "nivel_aceite": "Optimo",
    "presion_neumaticos_psi": 32,
    "bateria_voltaje": 12.5,
    "estado_frenos": "Bueno",
    "filtro_aire": "Limpio",
    "tipo_via": "Urbana",
    "condicion_via": "Buena",
    "temperatura_ambiente_c": 25
}

try:
    r = requests.post(f"{BASE_URL}/predict", json=datos)
    print(f"Status: {r.status_code}")
    print(f"Response: {json.dumps(r.json(), indent=4)}")
    print()
except Exception as e:
    print(f"ERROR: {e}")
    print()

# Test 3: POST /predict con alta probabilidad de falla
print("=" * 60)
print("TEST 3: POST /predict (alta probabilidad de falla)")
print("=" * 60)

datos_falla = {
    "region": "La Paz",
    "altitud_msnm": 4000,
    "marca": "Nissan",
    "tipo_vehiculo": "Camion",
    "año_fabricacion": 2010,
    "antiguedad_años": 16,
    "kilometraje": 200000,
    "ultimo_mantenimiento_dias": 500,
    "calidad_combustible": "Contaminado",
    "octanaje_estimado": 85,
    "contaminacion_agua_ppm": 50,
    "temperatura_motor_c": 120,
    "nivel_aceite": "Bajo",
    "presion_neumaticos_psi": 20,
    "bateria_voltaje": 10.0,
    "estado_frenos": "Critico",
    "filtro_aire": "Obstruido",
    "tipo_via": "Camino de Tierra",
    "condicion_via": "Mala",
    "temperatura_ambiente_c": 35
}

try:
    r = requests.post(f"{BASE_URL}/predict", json=datos_falla)
    print(f"Status: {r.status_code}")
    print(f"Response: {json.dumps(r.json(), indent=4)}")
    print()
except Exception as e:
    print(f"ERROR: {e}")
    print()

# Test 4: Categoria desconocida (debe dar 400)
print("=" * 60)
print("TEST 4: POST /predict con categoria desconocida")
print("=" * 60)

datos_invalidos = dict(datos)
datos_invalidos["marca"] = "MarcaInventadaXYZ"

try:
    r = requests.post(f"{BASE_URL}/predict", json=datos_invalidos)
    print(f"Status: {r.status_code}")
    print(f"Response: {json.dumps(r.json(), indent=4)}")
    print()
except Exception as e:
    print(f"ERROR: {e}")
    print()

# Test 5: Case-insensitive (debe funcionar)
print("=" * 60)
print("TEST 5: POST /predict con mayus/minus")
print("=" * 60)

datos_case = dict(datos)
datos_case["region"] = "cochabamba"
datos_case["calidad_combustible"] = "normal"

try:
    r = requests.post(f"{BASE_URL}/predict", json=datos_case)
    print(f"Status: {r.status_code}")
    print(f"Response: {json.dumps(r.json(), indent=4)}")
    print()
except Exception as e:
    print(f"ERROR: {e}")
    print()

# Test 6: Swagger
print("=" * 60)
print("TEST 6: Swagger Docs /docs")
print("=" * 60)
try:
    r = requests.get(f"{BASE_URL}/docs")
    print(f"Status: {r.status_code}")
    print("Swagger disponible" if r.status_code == 200 else "Swagger NO disponible")
except Exception as e:
    print(f"ERROR: {e}")

print("=" * 60)
print("FIN DE PRUEBAS - TODOS LOS TESTS COMPLETADOS")
print("=" * 60)