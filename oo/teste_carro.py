from unittest import TestCase

from oo.carro import Motor, Direcao, Carro


class CarroTestCase(TestCase):
    def teste_velocidade_inicial(self):
        motor = Motor()
        self.assertEqual(0, motor.velocidade)

    def teste_acelerar(self):
        motor = Motor()
        motor.acelerar()
        self.assertEqual(1, motor.velocidade)

    def teste_frear(self):
        motor = Motor()
        motor.acelerar()
        motor.acelerar()
        motor.frear()
        self.assertEqual(0, motor.velocidade)
        motor.acelerar()
        motor.acelerar()
        motor.acelerar()
        motor.frear()
        self.assertEqual(1, motor.velocidade)

    def teste_direcao_inicial(self):
        direcao = Direcao()
        self.assertEqual('Norte', direcao.valor)

    def teste_girar_a_direita(self):
        direcao = Direcao()
        direcao.girar_a_direita()
        self.assertEqual('Leste', direcao.valor)

    def teste_girar_a_esquerda(self):
        direcao = Direcao()
        direcao.girar_a_esquerda()
        self.assertEqual('Oeste', direcao.valor)

    def teste_velocidade_inicial_carro(self):
        direcao = Direcao()
        motor = Motor()
        carro = Carro(direcao, motor)
        self.assertEqual(0, carro.calcular_velocidade())

    def teste_acelerar_carro(self):
        direcao = Direcao()
        motor = Motor()
        carro = Carro(direcao, motor)
        carro.acelerar()
        self.assertEqual(1, carro.calcular_velocidade())

    def teste_frear_carro(self):
        direcao = Direcao()
        motor = Motor()
        carro = Carro(direcao, motor)
        carro.acelerar()
        carro.acelerar()
        carro.frear()
        self.assertEqual(0, carro.calcular_velocidade())
        carro.acelerar()
        carro.acelerar()
        carro.acelerar()
        carro.frear()
        self.assertEqual(1, carro.calcular_velocidade())

    def teste_direcao_inicial_carro(self):
        direcao = Direcao()
        motor = Motor()
        carro = Carro(direcao, motor)
        self.assertEqual('Norte', carro.calcular_direcao())

    def teste_girar_a_direita_carro(self):
        direcao = Direcao()
        motor = Motor()
        carro = Carro(direcao, motor)
        direcao.girar_a_direita()
        self.assertEqual('Leste', carro.calcular_direcao())

    def teste_girar_a_esquerda_carro(self):
        direcao = Direcao()
        motor = Motor()
        carro = Carro(direcao, motor)
        direcao.girar_a_esquerda()
        self.assertEqual('Oeste', carro.calcular_direcao())
