from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver


# Create your models here.

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField("Nome", max_length=100,blank=True)
    email = models.EmailField("Email",blank=True)
    cpf = models.CharField("CPF", max_length=15,blank=True)
    data_nascimento = models.DateField("Data de nascimento", null=True,blank=True)
    
    def __str__(self):
            return "{}".format(self.nome)
    
    class Meta:
        verbose_name_plural = "Clientes"
    


class Carro(models.Model):

    placa = models.CharField("Placa", max_length=10)
    marca = models.CharField("Marca", max_length=50)
    modelo = models.CharField("Modelo", max_length=20)
    comprar = models.DateField("Data de compra")
    ano = models.CharField('Ano', max_length=10)

    def __str__(self):
        return "{} - {}".format(self.marca, self.modelo)

    class Meta:
        verbose_name = "carro"
        verbose_name_plural = "carros"

class Aluguel(models.Model):

    codigo = models.CharField("Codigo", max_length=100)
    data_aluguel = models.DateField("Data de aluguel")
    data_devolucao = models.DateField("Data de devolução")
    valor = models.DecimalField("Valor", max_digits=15, decimal_places=2)
    devolucao = models.BooleanField("Devolvido")
    cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING, related_name='cliente_alugueis', verbose_name="Cliente")
    carro = models.ForeignKey(Carro, on_delete=models.DO_NOTHING, related_name='carro_alugueis', verbose_name="carros") 

    def __str__(self):
        return "{} - {} - {}".format(self.codigo, self.cliente.nome, self.carro.modelo)

    class Meta:
        verbose_name = "Aluguel"
        verbose_name_plural = "Alugueis"
