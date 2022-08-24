# imports
import pulp

#
prob = pulp.LpProblem('Q1-Custo_da_ração', pulp.LpMinimize)

# Variáveis de decisão
x1 = pulp.LpVariable('AltosFornos_Med1', lowBound=0, cat='Continuous')
x2 = pulp.LpVariable('AltosFornos_Med2', lowBound=0, cat='Continuous')
x3 = pulp.LpVariable('AltosFornos_Med3', lowBound=0, cat='Continuous')
x4 = pulp.LpVariable('FornosAbertos_Med1', lowBound=0, cat='Continuous')
x5 = pulp.LpVariable('FornosAbertos_Med2', lowBound=0, cat='Continuous')
x6 = pulp.LpVariable('FornosAbertos_Med3', lowBound=0, cat='Continuous')

# Definindo função objetivo
custo = 8*x1 + 10*x2 + 7*x3 + 6*x4 + 11*x5 + 9*x6

# Add a função-objetivo
prob += custo

# Restrições
particulas = 12*x1 + 9*x2 + 25*x3 + 20*x4 + 17*x5 + 43*x6
oxido = 35*x1 + 42*x2 + 18*x3 + 31*x4 + 56*x5 + 49*x6
hidrocarbonetos = 37*x1 + 53*x2 + 28*x3 + 34*x4 + 29*x5 + 20*x6

# Add restrições
prob += (particulas >= 60)
prob += (oxido >= 150)
prob += (hidrocarbonetos >= 125)

# escrevendo o problema de otimização linear
print(prob)

# Resolvendo o problema
optimization_result = prob.solve()

# Verificando se a solução ótima foi encontrada
assert optimization_result == pulp.LpStatusOptimal

# mostrando o resultado
for var in (x1, x2, x3, x4, x5, x6):
    print('A produção ótima deve ser {}: {:.5f}'.format(var.name, var.value()))
