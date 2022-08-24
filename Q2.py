# imports
import pulp
from math import log10 as log

#
prob = pulp.LpProblem('Q2', pulp.LpMaximize)

# Variáveis de decisão
x1 = pulp.LpVariable('1ano', lowBound=0, cat='Integer')
x2 = pulp.LpVariable('2ano', lowBound=0, cat='Integer')
x3 = pulp.LpVariable('3ano', lowBound=0, cat='Integer')

# Definindo função objetivo
logD = log(22000) + log(1.08)*x1 + log(1.17)*x2 + log(1.27)*x3

# Add a função-objetivo
prob += logD

# Restrições
anos = x1 + 2*x2 + 3*x3

# Add restrições
prob += (anos == 5)

# escrevendo o problema de otimização linear
print(prob)

# Resolvendo o problema
optimization_result = prob.solve()

# Verificando se a solução ótima foi encontrada
assert optimization_result == pulp.LpStatusOptimal

# mostrando o resultado
for var in (x1, x2, x3):
    print('A produção ótima deve ser {}: {:.5f}'.format(var.name, var.value()))
