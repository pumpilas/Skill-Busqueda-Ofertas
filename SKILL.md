# Skill: JobMatchAgent

## Descripción
Skill diseñada para buscar ofertas laborales en el correo electrónico del usuario, filtrarlas según su perfil profesional y enviar postulaciones automáticas a las vacantes relevantes.

## Instrucciones
- Entrada:
  - Palabras clave del perfil (ej. "Cisco", "AWS", "Telecomunicaciones").
  - Fuente de datos: bandeja de entrada del correo electrónico.
- Proceso:
  1. Escanea correos con ofertas laborales.
  2. Analiza requisitos de cada oferta.
  3. Compara con el perfil del usuario.
  4. Filtra solo las ofertas relevantes.
  5. Genera y envía un correo de postulación con CV adjunto.
- Salida:
  - Lista de ofertas relevantes.
  - Confirmación de postulaciones enviadas.

## Ejemplo de uso
**Usuario:** "Busca ofertas laborales en mi correo que incluyan 'Cisco' y 'AWS' y postúlate automáticamente."  
**Skill Output:**  
