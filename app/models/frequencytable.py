from tortoise import fields
from tortoise.models import Model

class FrequencyTable(Model):
    #Usando variable id por error de recursion ocasionado por usar la variable de nombre pk con tortoise
    id = fields.IntField(pk=True)
    freqlang = fields.CharField(max_length=23)
    created = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return self.freqlang