# imports
import pulp

# Criação do problema
prob = pulp.LpProblem('Q6-PPL', pulp.LpMaximize)

# Variáveis de decisão
x1 = pulp.LpVariable('x1', lowBound=0, cat='Continuous')
x2 = pulp.LpVariable('x2', lowBound=0, cat='Continuous')

# Definindo função objetivo
z = 3*x1 + x2

# Add a função-objetivo
prob += z

# Restrições
cond1 = 2*x1 + x2
cond2 = x1 + 3*x2

# Add restrições
prob += (cond1 <= 6)
prob += (cond2 <= 9)

# escrevendo o problema de otimização linear
print(prob)

# Resolvendo o problema
optimization_result = prob.solve()

# Verificando se a solução ótima foi encontrada
assert optimization_result == pulp.LpStatusOptimal

# mostrando o resultado
for var in (x1, x2):
    print('A produção ótima deve ser {}: {:.5f}'.format(var.name, var.value()))
