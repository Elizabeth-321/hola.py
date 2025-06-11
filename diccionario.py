dic={"nombre": "eli",
    "numero": 4657888,
    "casada": False

}
print(dic)

for key,value in dic.items():
    print(key, value)

 #key: es la clave  "nombre"
 #value: es el valor "eli"
 #dic

print(dic["numero"])  #si se pone nombre se mostraria "eli"

#///////////////////////////
# lista de diccionarios

personas=[{"nombre": "eli",
          "numero": 4657888,
          "casada": False
        },
        {"nombre": "ana",
        "numero": 464557888,
        "casada": True
        }]
# print(personas[2]["nombre"])

text=input("ingrese un texto")
pala=input("ingrese la palabra que quiere buscar")
productos={"nombre": "eli",
            "pera": 1500,
            # "melon": 1000
}
