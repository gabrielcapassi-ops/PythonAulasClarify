#classe base (superclasse) que representa o animal
class Animal:
    def fazerSom(self):
          #método generico que sera sobreesrito pelas subclasses
            #O uso do pass indica que nao há implementacoes aqui
        pass
#classe que herda de animal e representa cachorro      
class Cachorro(Animal):
    def fazerSom(self):
        #implementação especifica para cachorro
        return 'Au au'

class Gato(Animal):
    def fazerSom(self):
        return 'Miau'

class Vaca(Animal):
    def fazerSom(self):
        return 'Múú'

#funcao que recebe qualquer objetodo tipo animal (ou subclasses)
#e chamao metodo fazerSom()- uso efetivo do polimorfismo
def fazerAnimalFalar(animal: Animal):
   nome_animal = animal.__class__.__name__ #criando classe e nome dos animais
   som = animal.fazerSom()  #criando classe e som dos animais
   print(f'O {nome_animal} faz {som}')
   

#criando os objetos
cachorro = Cachorro()
gato = Gato()
vaca = Vaca()

#chama o método de cada animal de formapoliformica
fazerAnimalFalar(cachorro)
fazerAnimalFalar(gato)
fazerAnimalFalar(vaca)

animais = [ Cachorro(), Gato(), Vaca()]

for animal in animais:
    fazerAnimalFalar(animal)
