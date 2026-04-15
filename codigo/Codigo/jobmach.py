# jobmatch.py
# Prototipo inicial del agente JobMatchAgent

def filtrar_ofertas(correos, perfil):
    relevantes = []
    for correo in correos:
        if any(palabra in correo.lower() for palabra in perfil):
            relevantes.append(correo)
    return relevantes

# Ejemplo de prueba
correos = [
    "Vacante Ingeniero de redes e infraestructura",
    "tecnologo telecomunicaciones",
    "analista junior"
]

perfil = ["Cisco", "proyect manager", "Telecomunicaciones"]

print("Ofertas relevantes encontradas:")
for oferta in filtrar_ofertas(correos, perfil):
    print("-", oferta)

]

perfil = ["Cisco", "AWS", "Telecomunicaciones"]

print("Ofertas relevantes encontradas:")
for oferta in filtrar_ofertas(correos, perfil):
    print("-", oferta)
