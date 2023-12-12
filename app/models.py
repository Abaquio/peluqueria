from django.db import models

# Create your models here.
class Atencion(models.Model):
    ida = models.AutoField(db_column='idA', primary_key=True)  # Field name made lowercase.
    fecha = models.DateField()
    estado = models.CharField(max_length=200, blank=True, null=True)
    reserva = models.BooleanField(blank=False, null=False)
    servicio_ids = models.ForeignKey('Servicio', models.DO_NOTHING, db_column='Servicio_idS')  # Field name made lowercase.
    empleado_rut_e = models.ForeignKey('Empleado', models.DO_NOTHING, db_column='Empleado_rut_e')  # Field name made lowercase.
    cliente_rut_c = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='Cliente_rut_c')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Atencion'


class Cliente(models.Model):
    rut_c = models.AutoField(db_column='rut_c', primary_key=True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    fono = models.CharField(max_length=15, blank=True, null=True)
    correo = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Cliente'


class Empleado(models.Model):
    rut_e = models.CharField(db_column='rut_e',primary_key=True, max_length=10)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    fono = models.CharField(max_length=15)
    correo = models.CharField(max_length=50)
    rol = models.CharField(max_length=45)
    password = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'Empleado'


class Servicio(models.Model):
    ids = models.AutoField(db_column='idS', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=20)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Servicio'