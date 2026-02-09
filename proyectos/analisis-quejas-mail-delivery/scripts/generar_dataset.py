import pandas as pd
import random
from datetime import datetime, timedelta

# ----------------------------
# Configuración general
# ----------------------------
random.seed(42)

START_DATE = datetime(2025, 1, 1)
END_DATE = datetime(2025, 6, 30)

ZONAS = [
    "Vicente López", "San Isidro", "San Fernando", "Tigre",
    "Escobar", "San Martín", "Malvinas Argentinas",
    "San Miguel", "José C. Paz"
]

ASUNTOS_SUCIO = [
    "RECLAMO pedido no llego",
    "Pedido NO entregado!!!",
    "Demora en entrega",
    "Entrega tarde otra vez",
    "Re: Re: falta producto",
    "Pedido incompleto",
    "MAL SERVICIO",
    "Queja repartidor",
    "Problema con el repartidor",
    "Error en la factura",
    "Cobro incorrecto",
    "Reclamo por cobro",
    "No recibí mi pedido",
    "Re: Pedido incompleto",
    "Demora nuevamente",
    "Servicio pésimo"
]

REMITENTES = [
    "cliente@gmail.com",
    "usuario@yahoo.com",
    "reclamos@hotmail.com",
    "cliente123@outlook.com"
]

FORMATOS_FECHA = [
    "%Y-%m-%d %H:%M",
    "%d/%m/%y",
    "%Y/%m/%d",
    "%b %d, %Y"
]

# ----------------------------
# Funciones auxiliares
# ----------------------------
def fecha_random():
    delta = END_DATE - START_DATE
    fecha = START_DATE + timedelta(days=random.randint(0, delta.days))
    formato = random.choice(FORMATOS_FECHA)
    return fecha.strftime(formato)

def texto_mail_fake():
    textos = [
        "Buenas, escribo para reclamar por un problema con mi pedido.",
        "No es la primera vez que pasa esto.",
        "Espero una pronta respuesta.",
        "Muy mal servicio.",
        "Aguardo solución urgente."
    ]
    return " ".join(random.sample(textos, k=random.randint(2, 4)))

# ----------------------------
# Generación del dataset
# ----------------------------
registros = []

EMAIL_ID = 1
THREAD_ID = 1000

for _ in range(1200):  # ~6 meses, varios mails por día
    asunto = random.choice(ASUNTOS_SUCIO)

    # Simular respuestas en hilo
    if asunto.lower().startswith("re:"):
        thread_id = THREAD_ID
    else:
        THREAD_ID += 1
        thread_id = THREAD_ID

    registros.append({
        "email_id": EMAIL_ID,
        "fecha_raw": fecha_random(),
        "asunto_raw": asunto,
        "remitente": random.choice(REMITENTES),
        "zona": random.choice(ZONAS),
        "texto_mail": texto_mail_fake(),
        "thread_id": thread_id
    })

    EMAIL_ID += 1

df = pd.DataFrame(registros)

# ----------------------------
# Guardar CSV
# ----------------------------
output_path = "C:\\Users\\PAPA\\Desktop\\credito alco\\riga-alimentos\\proyectos\\analisis-quejas-mail-delivery\\data/raw/mails_quejas_raw.csv"
df.to_csv(output_path, index=False, encoding="utf-8")

print(f"Dataset generado correctamente en: {output_path}")
print(f"Total de registros: {len(df)}")

