from django.db import models

class Elemento(models.Model):
    atomicnumber = models.IntegerField(primary_key=True)   # Número atómico
    symbol = models.CharField(max_length=5, unique=True)    # Símbolo (ej: H, He, Li)
    name = models.CharField(max_length=100, unique=True)    # Nombre del elemento
    atomicMass = models.CharField(max_length=20, blank=True, null=True)            # Masa atómica
    cpkHexColor = models.CharField(max_length=7, blank=True, null=True)            # Color CPK en formato hexadecimal
    electronicConfiguration = models.CharField(max_length=100, blank=True, null=True)  # Configuración electrónica
    electronegativity = models.FloatField(blank=True, null=True)  # Electronegatividad
    atomicRadius = models.FloatField(blank=True, null=True)       # Radio atómico
    ionRadius = models.CharField(max_length=20, blank=True, null=True)  # Radio iónico
    vanDelWaalsRadius = models.FloatField(blank=True, null=True)  # Radio de Van der Waals
    ionizationEnergy = models.FloatField(blank=True, null=True)   # Energía de ionización
    electronAffinity = models.FloatField(blank=True, null=True)   # Afinidad electrónica
    oxidationStates = models.CharField(max_length=50, blank=True, null=True)  # Estados de oxidación
    standardState = models.CharField(max_length=20, blank=True, null=True)  # Estado estándar
    bondingType = models.CharField(max_length=20, blank=True, null=True)  # Tipo de enlace
    meltingPoint = models.FloatField(blank=True, null=True)  # Punto de fusión
    boilingPoint = models.FloatField(blank=True, null=True)  # Punto de ebullición
    density = models.FloatField(blank=True, null=True)  # Densidad
    groupBlock = models.CharField(max_length=25, blank=True, null=True)  # Bloque de grupo
    yearDiscovered = models.CharField(max_length=20, blank=True, null=True) # Año de descubrimiento


    def __str__(self):
        return f"{self.atomicnumber} - {self.symbol} ({self.name})"

class Short_Element(models.Model):
    atomicnumber = models.IntegerField(primary_key=True)   # Número atómico
    symbol = models.CharField(max_length=5, unique=True)    # Símbolo (ej: H, He, Li)
    name = models.CharField(max_length=100, unique=True)    # Nombre del elemento
    atomicMass = models.CharField(max_length=20, blank=True, null=True)  # Masa atómica
    groupBlock = models.CharField(max_length=25, blank=True, null=True)  # Bloque de grupo

    def __str__(self):
        return f"{self.atomicnumber} - {self.symbol} ({self.name})"
# Create your models here.
