# model_predictivo.py
import os
import json
from dotenv import load_dotenv
import googlemaps

# Carga las variables de entorno desde el archivo .env
load_dotenv()

def obtener_direcciones(api_key, origen, destino):
    gmaps = googlemaps.Client(key=api_key)
    return gmaps.directions(origen, destino, mode="driving", avoid="ferries", alternatives=True)

def calcular_consumo_ajustado(ruta_info):
    eficiencia_vehiculo = 0.2
    factor_ajuste_ascendente = 0.1
    factor_ajuste_descendente = 0.05
    velocidad_media = 60

    distancia_km = ruta_info['legs'][0]['distance']['value'] / 1000
    tiempo_horas = ruta_info['legs'][0]['duration']['value'] / 3600

    ajuste_elevacion = sum(
        max(0, step.get('elevation', 0)) * factor_ajuste_ascendente +
        min(0, step.get('elevation', 0)) * factor_ajuste_descendente
        for step in ruta_info['legs'][0]['steps']
    )

    consumo_base = distancia_km * eficiencia_vehiculo
    consumo_ajustado = consumo_base + ajuste_elevacion * distancia_km

    ajuste_velocidad = distancia_km / tiempo_horas * (velocidad_media / 100)
    consumo_ajustado += ajuste_velocidad

    return consumo_ajustado

def encontrar_ruta_optima(origen, destino, porcentaje_bateria_actual):
    api_key = os.getenv('GOOGLE_MAPS_API_KEY')

    direcciones = obtener_direcciones(api_key, origen, destino)

    if not direcciones:
        return json.dumps({"error": "No se pudieron obtener las direcciones para las rutas."})

    capacidad_bateria_estandar = 60  # Capacidad estándar de la batería en kWh

    resultados = {"rutas": [], "error": None, "mensaje": None, "ruta_optima_index": None}

    for i, ruta_info in enumerate(direcciones):
        consumo_ajustado = calcular_consumo_ajustado(ruta_info)

        porcentaje_bateria_necesario = max(0, (consumo_ajustado / capacidad_bateria_estandar) * 100)

        porcentaje_recargar = max(0, porcentaje_bateria_necesario - porcentaje_bateria_actual)

        mensaje_ruta = "Con el porcentaje de batería actual, puedes llegar al destino." if porcentaje_bateria_necesario <= porcentaje_bateria_actual else f"Necesitas cargar aproximadamente {porcentaje_recargar:.2f}% más de batería para usar esta ruta."

        # Ajusta la información de la ruta para incluir solo lo necesario
        informacion_ruta = {
            "overview_polyline": ruta_info.get("overview_polyline", {}).get("points", ""),
            "bounds": {
                "northeast": {
                    "lat": ruta_info.get("bounds", {}).get("northeast", {}).get("lat", ""),
                    "lng": ruta_info.get("bounds", {}).get("northeast", {}).get("lng", "")
                },
                "southwest": {
                    "lat": ruta_info.get("bounds", {}).get("southwest", {}).get("lat", ""),
                    "lng": ruta_info.get("bounds", {}).get("southwest", {}).get("lng", "")
                }
            }
        }

        ruta_actual = {
            "numero_ruta": i + 1,
            "distancia": ruta_info['legs'][0]['distance']['text'],
            "duracion": ruta_info['legs'][0]['duration']['text'],
            "consumo_ajustado": consumo_ajustado,
            "porcentaje_bateria_necesario": porcentaje_bateria_necesario,
            "porcentaje_recargar": porcentaje_recargar,
            "necesita_recargar": porcentaje_recargar > 0,
            "mensaje": mensaje_ruta,
            "ruta_optima": False,  # Inicialmente establecer como False
            "informacion_ruta": informacion_ruta
        }

        resultados["rutas"].append(ruta_actual)

    # Establece la ruta óptima
    if resultados["rutas"]:
        resultados["ruta_optima_index"] = min(range(len(resultados["rutas"])), key=lambda i: resultados["rutas"][i]["consumo_ajustado"])
        resultados["rutas"][resultados["ruta_optima_index"]]["ruta_optima"] = True

    if not resultados["rutas"]:
        resultados["error"] = "Ninguna ruta te permite llegar al destino con el porcentaje actual de batería."
    else:
        resultados["mensaje"] = "Todas las rutas son alcanzables con el porcentaje de batería actual."

    return json.dumps(resultados, indent=2)
