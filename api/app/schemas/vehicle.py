from pydantic import BaseModel

class VehicleData(BaseModel):

    region: str
    altitud_msnm: float
    marca: str
    tipo_vehiculo: str
    año_fabricacion: float
    antiguedad_años: float
    kilometraje: float
    ultimo_mantenimiento_dias: float
    calidad_combustible: str
    octanaje_estimado: float
    contaminacion_agua_ppm: float
    temperatura_motor_c: float
    nivel_aceite: str
    presion_neumaticos_psi: float
    bateria_voltaje: float
    estado_frenos: str
    filtro_aire: str
    tipo_via: str
    condicion_via: str
    temperatura_ambiente_c: float