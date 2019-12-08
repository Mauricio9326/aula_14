class funcionario:
 def __init__(self, nome, horas_trabalhadas, salario):
        self.nome = nome
        self.horas_trabalhadas = horas_trabalhadas
        self.salario = salario

 def __str__(self):
    return f"Olá{self.nome}, você está cadastrado com sucesso em nosso sistema."

Pessoa_fisica = funcionario(
    nome= "Mauricio Amyr Ibrahim Silva",
    horas_trabalhadas= "800",
    salario= 10500
)

print(Pessoa_fisica.salario)





