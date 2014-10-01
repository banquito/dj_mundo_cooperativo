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
    fax = models.CharField(max_length=200, null=True, blank=True)
    correo_electronico = models.CharField(max_length=200, null=True, blank=True) 
    director = models.CharField(max_length=200)
    director2 = models.CharField(max_length=200, null=True)

    def __unicode__(self):
        return self.provincia

class Cooperative(models.Model):
    provincia = models.ForeignKey(Organization)
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200, null=True, blank=True)
    objeto = models.CharField(max_length=200, null=True, blank=True)
    direccion = models.CharField(max_length=200, null=True, blank=True)
    localidad = models.CharField(max_length=200, null=True, blank=True)
    codigo_postal = models.CharField(max_length=200, null=True, blank=True)
    pub_date = models.DateTimeField('date published')
    capital_fecha = models.DateTimeField('date', null=True, blank=True)
    capital_monto = models.CharField(max_length=200, null=True, blank=True)
    capital_numero = models.CharField(max_length=200, null=True, blank=True)
    capital_banco = models.CharField(max_length=200, null=True, blank=True)
    capital_direccion = models.CharField(max_length=200, null=True, blank=True)
    presentacion = models.DateTimeField('date', null=True, blank=True)
    expediente = models.CharField(max_length=200, null=True, blank=True)
    matricula = models.CharField(max_length=200, null=True, blank=True)
    cuit = models.CharField(max_length=200, null=True, blank=True)

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

class Course(models.Model):
    partner = models.ForeignKey(Partner)
    fecha_de_asistencia = models.DateTimeField('date')
    sede = models.CharField(max_length=200)
    confirmacion = models.NullBooleanField()
    pub_date = models.DateTimeField('date published')

class Assembly(models.Model):
    cooperative = models.ForeignKey(Cooperative)
    fecha_de_convocatoria = models.DateTimeField('date')
    notificacion = models.BooleanField(True)
    direccion = models.CharField(max_length=200)
    localidad = models.CharField(max_length=200)
    codigo_postal = models.CharField(max_length=200)
    fecha_inicio_asamblea = models.DateTimeField('date')
    fecha_fin_asamblea = models.DateTimeField('date')
    precide_asamblea = models.OneToOneField(Partner, related_name='precide')
    miembros_consejo_1 = models.OneToOneField(Partner, related_name='consejo_1')
    miembros_consejo_2 = models.OneToOneField(Partner, related_name='consejo_2')
    miembros_consejo_3 = models.OneToOneField(Partner, related_name='consejo_3')
    sindico_titular = models.OneToOneField(Partner, related_name='sindico')
    sindico_suplente = models.OneToOneField(Partner, related_name='suplente')
    fecha_inicio_consejo = models.DateTimeField('date')
    fecha_fin_consejo = models.DateTimeField('date')
    miembros_consejo_presidente = models.OneToOneField(Partner, related_name='consejo_presidente')
    miembros_consejo_secretario = models.OneToOneField(Partner, related_name='consejo_secretario')
    miembros_consejo_tesorero = models.OneToOneField(Partner, related_name='consejo_tesorero')