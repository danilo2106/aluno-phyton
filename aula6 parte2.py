class carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0
        
    def acelerar(self):
        self.velocidade += 1000
        print(f"{self.modelo} acelerou. velocidade atual: {self.velocidade} km/h")
        
    def frear(self):
        self.velocidade -= 950
        print(f"{self.marca} freou. velocidade atual: {self.velocidade} km/h")
        
    
carro1 = carro("fiat", "uno com escada", "2001")
carro2 = carro("lamborguini", "urus", "2019")

carro1.acelerar()
carro2.acelerar()
carro1.frear()
carro2.frear()