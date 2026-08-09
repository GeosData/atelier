# Generador de código QR
> Crea el QR de WhatsApp, WiFi, teléfono o cualquier link de un negocio y lo descarga en PNG.

**Para quién:** negocios que necesitan un QR para mostrador, volante o vitrina sin depender de un servicio externo.
**ROI:** ⏱️ evita usar generadores QR de terceros con marca de agua o registro.
**Motor:** Cálculo en navegador (sin IA)
**Demo en vivo:** https://atelier.geosdata.com/soluciones/generador-de-qr/

## Qué hace
Genera un código QR estático a partir de uno de cuatro tipos: URL/texto libre, WhatsApp (número + mensaje precargado), WiFi (SSID + contraseña + seguridad) o teléfono. Lo dibuja en un canvas y permite descargarlo como PNG en alta calidad.

## Entrada → Salida
Entrada: tipo de QR y sus campos (URL/texto; número + mensaje de WhatsApp; SSID + contraseña + tipo de seguridad de WiFi; número de teléfono).

Calcula: arma el payload correspondiente al tipo (link `wa.me`, string `WIFI:...`, `tel:+...` o texto/URL directo) y lo codifica como QR en el navegador.

## Cómo está hecho
Client-side, cero backend: usa la librería `qrcode` en el navegador; ni el número ni la clave de WiFi salen del dispositivo.
