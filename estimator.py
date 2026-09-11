import re

def parse_and_estimate_co2(user_text: str) -> dict:
    """
    Analiza lenguaje natural y calcula la huella de CO2 estimada en kg.
    """
    text = user_text.lower()
    total_co2 = 0.0
    breakdown = []

    # Reglas de transporte
    bus_match = re.search(r'(\d+)\s*km\s*en\s*bus', text)
    if bus_match:
        km = float(bus_match.group(1))
        co2 = km * 0.103  # ~103g CO2/km por pasajero
        total_co2 += co2
        breakdown.append(f"🚌 Transporte en Bus ({km} km): {co2:.2f} kg CO2")

    car_match = re.search(r'(\d+)\s*km\s*en\s*(carro|auto|coche)', text)
    if car_match:
        km = float(car_match.group(1))
        co2 = km * 0.192  # ~192g CO2/km
        total_co2 += co2
        breakdown.append(f"🚗 Viaje en Carro ({km} km): {co2:.2f} kg CO2")

    # Reglas de alimentación
    if "carne" in text:
        total_co2 += 4.5
        breakdown.append("🥩 Consumo de Carne roja: 4.50 kg CO2")
    if "pollo" in text or "pescado" in text:
        total_co2 += 1.2
        breakdown.append("🍗 Consumo de Carne blanca/pescado: 1.20 kg CO2")
    if "vegetariano" in text or "ensalada" in text:
        total_co2 += 0.5
        breakdown.append("🥗 Comida Vegetariana: 0.50 kg CO2")

    if not breakdown:
        total_co2 = 1.0
        breakdown.append("🌱 Actividad general registrada: 1.00 kg CO2 (Estimado base)")

    return {
        "total_co2": round(total_co2, 2),
        "breakdown": breakdown
    }