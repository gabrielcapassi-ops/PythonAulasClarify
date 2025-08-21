import unittest
from operacoes import somar, subtrair, multiplicar, dividir

#define uma classe de teste que herda de unittest.testcase
class TesteOperacoes(unittest.TestCase):
    def testar_somar(self): #self pq vai testar dentro dele verificar se o def esta dentro da identacao do class
        self.assertEqual(somar(2,3),5) #vc da um exemplo e o resultado esperado
        self.assertEqual(somar(-1,1),0)
        self.assertEqual(somar(-2,-3),-5)

    def testar_subtrair(self):
        self.assertEqual(subtrair(5,3),2) 
        self.assertEqual(subtrair(-1,1),-2)
        self.assertEqual(subtrair(0,0),0)

    def testar_multiplicar(self):
        self.assertEqual(multiplicar(2,3),6)
        self.assertEqual(multiplicar(-1,1),-1)
        self.assertEqual(multiplicar(0,0),0)

    def testar_dividir(self):
        self.assertEqual(dividir(6,2),3)
        self.assertEqual(dividir(-6,2),-3)
        with self.assertRaises(ValueError):
            dividir(1,0)

if __name__ == "__main__":
    unittest.main()
