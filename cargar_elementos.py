import os
import django
import json

# Configurar Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Table_Chemistry.settings")
django.setup()

from elementos.models import Elemento

# Leer el JSON
ruta = os.path.join(os.getcwd(), "data.json")
with open(ruta, "r", encoding="utf-8") as f:
    elementos = json.load(f)

for elem in elementos:
    # Manejo de campos vacíos
    atomicnumber = elem.get("atomicNumber") or 0
    symbol = elem.get("symbol") or None
    name = elem.get("name") or None
    atomicMass = elem.get("atomicMass") or None
    cpkHexColor = elem.get("cpkHexColor") or None
    electronicConfiguration = elem.get("electronicConfiguration") or None
    electronegativity = elem.get("electronegativity") or None
    atomicRadius = elem.get("atomicRadius") or None
    ionRadius = elem.get("ionRadius") or None
    vanDelWaalsRadius = elem.get("vanDelWaalsRadius") or None
    ionizationEnergy = elem.get("ionizationEnergy") or None
    electronAffinity = elem.get("electronAffinity") or None
    oxidationStates = elem.get("oxidationStates") or None
    standardState = elem.get("standardState") or None
    bondingType = elem.get("bondingType") or None
    meltingPoint = elem.get("meltingPoint") or None
    boilingPoint = elem.get("boilingPoint") or None
    density = elem.get("density") or None
    groupBlock = elem.get("groupBlock") or None
    yearDiscovered = elem.get("yearDiscovered") or None

    Elemento.objects.get_or_create(
        atomicnumber=atomicnumber,
        defaults={
            "symbol": symbol,
            "name": name,
            "atomicMass": atomicMass,
            "cpkHexColor": cpkHexColor,
            "electronicConfiguration": electronicConfiguration,
            "electronegativity": electronegativity,
            "atomicRadius": atomicRadius,
            "ionRadius": ionRadius,
            "vanDelWaalsRadius": vanDelWaalsRadius,
            "ionizationEnergy": ionizationEnergy,
            "electronAffinity": electronAffinity,
            "oxidationStates": oxidationStates,
            "standardState": standardState,
            "bondingType": bondingType,
            "meltingPoint": meltingPoint,
            "boilingPoint": boilingPoint,
            "density": density,
            "groupBlock": groupBlock,
            "yearDiscovered": yearDiscovered
        }
    )

print("¡Elementos cargados correctamente!")