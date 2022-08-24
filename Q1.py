import pulp

# Criação do problema
prob = pulp.LpProblem('Q1-Custo_da_ração', pulp.LpMinimize)

# Variáveis de decisão
x1 = pulp.LpVariable('Milho', lowBound=0, cat='Continuous')
x2 = pulp.LpVariable('Farelo_de_soja', lowBound=0, cat='Continuous')

# Definindo função objetivo
custo = 0.26*x1 + 0.32*x2

# Add a função-objetivo
prob += custo

# Restrições
protein = 0.07*x1 + 0.21*x2
carb = 0.82*x1 + 0.79*x2

# Add restrições
prob += (protein >= 0.34)
prob += (carb >= 2.64)

# escrevendo o problema de otimização linear
print(prob)

# Resolvendo o problema
optimization_result = prob.solve()

# Verificando se a solução ótima foi encontrada
assert optimization_result == pulp.LpStatusOptimal

# mostrando o resultado
for var in (x1, x2):
    print('A produção ótima deve ser {}: {:.5f}'.format(var.name, var.value()))
