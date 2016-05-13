from django.db import models


class Fact(models.Model):
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.description

    def arguments(self):
        return FactArgument.objects.filter(fact=self)

    def arguments_json(self):
        labels = []
        data = []
        json = {'labels': labels, 'data': data}
        for argument in self.arguments():
            labels.append(argument.label)
            data.append(argument.value)
        return json


class ArgumentType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class FactArgument(models.Model):
    label = models.CharField(max_length=200)
    value = models.IntegerField()
    type = models.ForeignKey(ArgumentType)
    fact = models.ForeignKey(Fact)

    def __str__(self):
        return 'Argument of ' + self.fact.__str__() + ' label: ' + self.label + ' value: ' + str(self.value) \
               + ' type: ' + self.type.__str__()
