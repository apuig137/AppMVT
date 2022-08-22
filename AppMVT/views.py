from re import M
from django.shortcuts import render
from AppMVT.models import familiar
from datetime import date

def familia(request):
    padre=familiar(nombre="Roberto",edad=58,parentesco="padre",nacimiento=date(1964,7,29))
    madre=familiar(nombre="Liliana",edad=42,parentesco="madre",nacimiento=date(1979,9,12))
    hermano_menor=familiar(nombre="Juan Ignacio",edad=13,parentesco="hermano menor",nacimiento=date(2008,12,29))
    hermano_mayor=familiar(nombre="Agustin",edad=20,parentesco="hermano mayor",nacimiento=date(2002,2,6))

    padre.save()
    madre.save()
    hermano_menor.save()
    hermano_mayor.save()
    CONTEXTO={
        "roberto":padre,"liliana":madre,"juani":hermano_menor,"yo":hermano_mayor
    }
    return render(request,"template1.html",CONTEXTO)
