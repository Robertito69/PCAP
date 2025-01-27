class Reptil:
    def __init__(self, nombre):
        self.nombre = nombre
        pass
   
class Serpiente(Reptil):
    pass
 
class Culebra(Serpiente):
    pass
 
print("--------------")
print(f"{Reptil.__name__}\t{Serpiente.__name__} {Culebra.__name__}")
 
for cls1 in [Reptil, Serpiente, Culebra]:
    for cls2 in [Reptil, Serpiente, Culebra]:
        print(issubclass(cls1, cls2), end="\t")
    print()
   
print("--------------")
   
repril1 = Reptil("largarto")
reptil2 = Serpiente("Mamba_Negra")
reptil3 = Culebra("Culebra_Ibe")
 
print(Reptil.__name__)
print(type(reptil2).__name__)
 
print("--------------")
print(f"\t\t{Reptil.__name__}\t{Serpiente.__name__} {Culebra.__name__}")
for cls1 in [repril1, reptil2, reptil3]:
    print(cls1.nombre, end=" \t")
    for cls2 in [Reptil, Serpiente, Culebra]:
        #el primer argumento sera el objeto y el segundo la clase
        print(isinstance(cls1, cls2), end="\t")
    print()
 
print("--------------")
 
reptil4 = Reptil("Rana")
reptil5 = Reptil("vibora")
reptil6 = Reptil("cocodrilo")
 
reptil4 = reptil5
##reptil5 = reptil6
 
print(reptil4 == reptil5, reptil4 is reptil5)
print(reptil5 == reptil6, reptil5 is reptil6)
reptil4=reptil6
print(reptil4== reptil6,reptil4 is reptil6)