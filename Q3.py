import pulp

#min Custo=190*x+200*y
#     1.8<=2*x+2.5*y<=2.5 (silicon)
#     0.9<= x+1.5*y<=1.2 (níquel)
#     3.2<=3*x+4*y<=3.5 (carbono)
#     x= quantidade de tonelada da liga 1, x2= quantidade de tonelada da liga 2


# Definindo o problema como de maximização
prob = pulp.LpProblem('Problema da Liga de Aço', pulp.LpMinimize)

# Definindo as variáveis de decisão
x = pulp.LpVariable('Liga_1', lowBound=0, upBound = 1, cat='Continuous')
y = pulp.LpVariable('Liga_2', lowBound=0, upBound = 1, cat='Continuous')

#Definindo a função Objetivo
Custo= 190*x+200*y

#Add a função-objetivo
prob += Custo

#Restrição
Silicon=2*x+2.5*y

#Add restrição 
prob += (Silicon<=2.5)
prob += (1.8<=Silicon)


#Restrição
Niquel=x+1.5*y

#Add restrição 
prob += (Niquel<=1.2)
prob += (0.9<=Niquel)

#Restrição
Carbono=3*x+4*y

#Add restrição 
prob += (Carbono<=3.5)
prob += (3.2<=Carbono)

#Restrição
Porcentagem=x+y

#Add restrição 
prob += (Porcentagem==1)

#escrevendo o problema de otimização linear
print (prob)

# Resolvendo o problema 
optimization_result = prob.solve()

# Verificando se a solução ótima foi encontrada
assert optimization_result == pulp.LpStatusOptimal

#mostrando o resultado
for var in (x, y):
    print('A produção ótima deve ser {}: {:1.2f}'.format(var.name, var.value()))