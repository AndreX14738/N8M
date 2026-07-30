import joblib
from pathlib import Path

# Ruta hacia la carpeta modelo
BASE_DIR = Path(__file__).resolve().parent.parent.parent
MODELO_DIR = BASE_DIR / "modelo"

# Validar que los archivos existan antes de cargar
MODELO_PATH = MODELO_DIR / "modelo.pkl"
ENCODERS_PATH = MODELO_DIR / "label_encoders.pkl"

if not MODELO_PATH.exists():
    raise FileNotFoundError(
        f"No se encontró el archivo del modelo en: {MODELO_PATH}. "
        "Asegúrate de haber ejecutado el notebook de entrenamiento."
    )

if not ENCODERS_PATH.exists():
    raise FileNotFoundError(
        f"No se encontró el archivo de label_encoders en: {ENCODERS_PATH}. "
        "Asegúrate de haber ejecutado el notebook de entrenamiento."
    )

# Cargar modelo entrenado
modelo = joblib.load(MODELO_PATH)

# Cargar Label Encoders
label_encoders = joblib.load(ENCODERS_PATH)