from PIL import Image, ImageDraw
import io, json
img = Image.new("RGB", (520, 460), "white")
d = ImageDraw.Draw(img)
lines = [
 "EXAMEN DE MATEMATICAS      Alumno: Juan Perez",
 "",
 "1. (facil) Cuanto es 2 + 2 ?",
 "   Respuesta: 5",
 "",
 "2. (facil) Capital de Colombia ?",
 "   Respuesta: Medellin",
 "",
 "3. (dificil) Derivada de x^2 ?",
 "   Respuesta: 2x",
 "",
 "4. (dificil) Integral de 1/x dx ?",
 "   Respuesta: ln(x) + C",
]
y = 20
for ln in lines:
    d.text((20, y), ln, fill="black"); y += 30
buf = io.BytesIO(); img.save(buf, format="PNG")

from app.products.registry import get_product
from app.services import engine
r = engine.run(get_product("exam"), buf.getvalue(), "image/png")
print(json.dumps(r.model_dump(), indent=2, ensure_ascii=False))
