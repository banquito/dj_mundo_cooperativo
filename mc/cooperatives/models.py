from django.db import models

class Organization(models.Model):
    nombre = models.CharField(max_length=200)
    siglas = models.CharField(max_length=200)
    domicilio = models.CharField(max_length=200)
    codigo_postal = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=200)
    provincia = models.CharField(max_length=200)
    prefijo = models.IntegerField()
    telefonos = models.CharField(max_length=200)
    fax = models.CharField(max_length=200, null=True)
    correo_electronico = models.CharField(max_length=200, null=True) 
    director = models.CharField(max_length=200)
    director2 = models.CharField(max_length=200, null=True)

    def __unicode__(self):
        return self.provincia

class Cooperative(models.Model):
    provincia = models.ForeignKey(Organization)
    nombre = models.CharField(max_length=200)
    objeto = models.CharField(max_length=200, null=True)
    direccion = models.CharField(max_length=200, null=True)
    localidad = models.CharField(max_length=200, null=True)
    codigo_postal = models.CharField(max_length=200, null=True)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.nombre

class Partner(models.Model):
    cooperative = models.ForeignKey(Cooperative)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    correo_electronico = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    localidad = models.CharField(max_length=200)
    dni = models.IntegerField(default=0)
    fecha_de_nacimiento = models.DateTimeField('date')
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.nombre