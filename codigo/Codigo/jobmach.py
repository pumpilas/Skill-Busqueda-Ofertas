# jobmatch.py
# Prototipo JobMatchAgent con Outlook y Microsoft Graph API

import msal
import requests

# Configuración de la aplicación registrada en Azure
CLIENT_ID = "TU_CLIENT_ID"
TENANT_ID = "TU_TENANT_ID"
CLIENT_SECRET = "TU_CLIENT_SECRET"

AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
SCOPE = ["https://graph.microsoft.com/.default"]

# Inicializar cliente MSAL
app = msal.ConfidentialClientApplication(
    CLIENT_ID, authority=AUTHORITY, client_credential=CLIENT_SECRET
)

# Obtener token de acceso
result = app.acquire_token_for_client(scopes=SCOPE)
if "access_token" not in result:
    raise Exception("Error al obtener token de acceso")

token = result["access_token"]

# Función para leer correos de la bandeja de entrada
def leer_correos():
    url = "https://graph.microsoft.com/v1.0/me/messages"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()["value"]
    else:
        raise Exception("Error al leer correos: " + response.text)

# Filtrar ofertas laborales según perfil
def filtrar_ofertas(correos, perfil):
    relevantes = []
    for correo in correos:
        asunto = correo.get("subject", "")
        cuerpo = correo.get("bodyPreview", "")
        if any(p.lower() in cuerpo.lower() or p.lower() in asunto.lower() for p in perfil):
            relevantes.append(correo)
    return relevantes

# Generar correo de postulación
def generar_postulacion(oferta):
    cuerpo = f"""
Estimado equipo de {oferta.get('from', {}).get('emailAddress', {}).get('name', 'Reclutador')},

Me permito postularme a la vacante: {oferta.get('subject', 'Oferta laboral')}.
Mi perfil profesional incluye experiencia en Cisco, AWS y Telecomunicaciones,
lo cual considero se ajusta a los requisitos solicitados.

Adjunto mi hoja de vida para su consideración.
Quedo atento a la posibilidad de entrevista.

Atentamente,
Javier
hjavier_17@outlook.es
"""
    return cuerpo

# Enviar correo de postulación
def enviar_postulacion(destinatario, asunto, cuerpo):
    url = "https://graph.microsoft.com/v1.0/me/sendMail"
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    data = {
        "message": {
            "subject": asunto,
            "body": {"contentType": "Text", "content": cuerpo},
            "toRecipients": [{"emailAddress": {"address": destinatario}}],
        },
        "saveToSentItems": "true",
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 202:
        print("Postulación enviada correctamente.")
    else:
        print("Error al enviar postulación:", response.text)

# Ejecución del prototipo
perfil = ["Cisco", "AWS", "Telecomunicaciones"]
correos = leer_correos()
ofertas = filtrar_ofertas(correos, perfil)

print("Ofertas relevantes encontradas:")
for oferta in ofertas:
    print("-", oferta["subject"])
    cuerpo = generar_postulacion(oferta)
    # Aquí podrías enviar la postulación automáticamente:
    # enviar_postulacion(oferta["from"]["emailAddress"]["address"], oferta["subject"], cuerpo)
    print("Correo generado:\n", cuerpo)



