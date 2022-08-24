import pulp

#max Receita=4*x+2*y
#     4*x+y<=30 (ovos)
#     x+2*y<=100 (tempo de forno)
#     x= quantidade de torta de chocolate, x2= quantidade de torta de morango


# Definindo o problema como de maximização
prob = pulp.LpProblem('Problema da Torta', pulp.LpMaximize)

# Definindo as variáveis de decisão
x = pulp.LpVariable('torta_chocolate', lowBound=0, cat='Integer')
y = pulp.LpVariable('torta_morango', lowBound=0, cat='Integer')

#Definindo a função Objetivo
Receita= 4*x+2*y

#Add a função-objetivo
prob += Receita

#Restrição
Ovos=4*x+y

#Add restrição 
prob += (Ovos<=30)


#Restrição
Forno= x+2*y

#Add restrição 
prob += (Forno<=24)


#escrevendo o problema de otimização linear
print (prob)

# Resolvendo o problema 
optimization_result = prob.solve()

# Verificando se a solução ótima foi encontrada
assert optimization_result == pulp.LpStatusOptimal

#mostrando o resultado
for var in (x, y):
    print('A produção ótima deve ser {}: {:1.0f}'.format(var.name, var.value()))