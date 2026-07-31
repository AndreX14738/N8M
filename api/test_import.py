import sys
sys.path.insert(0, '.')

print("Iniciando import...")

try:
    from app.main import app
    from app.models.predictor import label_encoders

    print("OK - Import exitoso")
    print("\n===== LABEL ENCODERS =====")

    for columna, encoder in label_encoders.items():
        print(f"\n📌 {columna}")
        print(list(encoder.classes_))

except Exception as e:
    import traceback
    print(f"ERROR: {type(e).__name__}: {e}")
    traceback.print_exc()