import sys
sys.path.insert(0, '.')
sys.stdout.write("Iniciando import...\n")
sys.stdout.flush()
try:
    from app.main import app
    sys.stdout.write("OK - Import exitoso\n")
    sys.stdout.flush()
except Exception as e:
    import traceback
    sys.stdout.write(f"ERROR: {type(e).__name__}: {e}\n")
    sys.stdout.flush()
    traceback.print_exc()