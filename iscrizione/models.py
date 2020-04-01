from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Eventi(models.Model):
    evento = models.CharField(max_length=100)
    nota = models.CharField(max_length=250,blank=True)
    parte_da = models.CharField(max_length=50,blank=True)
    data_evento = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return  str(self.evento)

    class Meta:
        verbose_name = 'evento'
        verbose_name_plural = 'eventi'

    def get_number_of_iscrizioni(self):
        return Iscrizioni.objects.filter(id_evento=self).count()

    def get_number_of_iscrizioni_for_utente(self):
        return Iscrizioni.objects.filter(id_evento=self,id_user=1).count()


class TabellaFermate(models.Model):
    fermata = models.CharField(max_length=100)

    def __str__(self):
        return self.fermata

    class Meta:
        verbose_name = 'fermata'
        verbose_name_plural = 'fermate'
#

class Iscrizioni(models.Model):
    id_evento = models.ForeignKey(Eventi,on_delete=models.CASCADE,related_name='eventi')
    id_user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='iscrizioni')
    nome = models.CharField(max_length=50)
    cognome = models.CharField(max_length=50)
    telefono = models.CharField(max_length=40,blank=True)
    id_fermata = models.ForeignKey(TabellaFermate,on_delete=models.CASCADE,related_name='fermate',default=1)

    def __str__(self):
        return str(self.id) + 'Id_user: ' +  str(self.id_user_id) + '- Nominativo= ' + self.nome + ' ' + self.cognome + ' ' + str(self.id_evento)

    class Meta:
        verbose_name = 'iscrizione'
        verbose_name_plural = 'iscrizioni'

    def get_id_user(self):
        return self.id_user


    def get_number_of_iscrizioni_for_utente1(self):
        return Iscrizioni.objects.filter(id_evento=1,id_user=1).count()



#    def get_absolute_url(self):
        #return reverse('user_iscrizioni_list')


##data_creazione = models.DateTimeField(auto_now_add=True)
