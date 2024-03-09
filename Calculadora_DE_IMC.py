def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

class IMCClassification:
    def _init_(self, imc):
        self.imc = imc

    def classificacao(self):
        if self.imc < 18.5:
            return "Abaixo do Peso"
        elif self.imc < 25:
            return "Peso Normal"
        elif self.imc < 30:
            return "Sobrepeso"
        elif self.imc < 35:
            return "Obesidade Grau I"
        elif self.imc < 40:
            return "Obesidade Grau II (Severa)"
        else:
            return "Obesidade Grau III (Mórbida)"

peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

imc_calculado = calcular_imc(peso, altura)
classificacao = IMCClassification(imc_calculado)

print(f"Seu IMC é: {imc_calculado:.2f} e você está {classificacao.classificacao()}.")