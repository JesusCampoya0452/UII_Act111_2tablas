from django.db import models

class Producto(models.Model):
    ID_prd = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, help_text="Nombre del producto")
    unidad_medida = models.CharField(max_length=50)
    fecha_vencimiento = models.DateField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen_producto = models.ImageField(upload_to='img_productos/', blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

class Proveedor(models.Model):
    ID_Prove = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    domicilio = models.CharField(max_length=200, blank=True, null=True)
    ID_prd = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='proveedores', verbose_name="Producto Suministrado")

    def __str__(self):
        return f"{self.nombre} (ID: {self.ID_Prove})"

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"