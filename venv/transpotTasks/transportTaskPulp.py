from pulp import *
import time
start = time.time()
x1 = pulp.LpVariable("x1", lowBound=0)
x2 = pulp.LpVariable("x2", lowBound=0)
x3 = pulp.LpVariable("x3", lowBound=0)
x4 = pulp.LpVariable("x4", lowBound=0)
x5 = pulp.LpVariable("x5", lowBound=0)
x6 = pulp.LpVariable("x6", lowBound=0)
x7 = pulp.LpVariable("x7", lowBound=0)
x8 = pulp.LpVariable("x8", lowBound=0)
x9 = pulp.LpVariable("x9", lowBound=0)
x10 = pulp.LpVariable("x10", lowBound=0)
x11 = pulp.LpVariable("x11", lowBound=0)
x12 = pulp.LpVariable("x12", lowBound=0)
x13 = pulp.LpVariable("x13", lowBound=0)
x14 = pulp.LpVariable("x14", lowBound=0)
x15 = pulp.LpVariable("x15", lowBound=0)
x16 = pulp.LpVariable("x16", lowBound=0)
x17 = pulp.LpVariable("x17", lowBound=0)
x18 = pulp.LpVariable("x18", lowBound=0)
x19 = pulp.LpVariable("x19", lowBound=0)
x20 = pulp.LpVariable("x20", lowBound=0)
x21 = pulp.LpVariable("x21", lowBound=0)
x22 = pulp.LpVariable("x22", lowBound=0)
x23 = pulp.LpVariable("x23", lowBound=0)
x24 = pulp.LpVariable("x24", lowBound=0)
x25 = pulp.LpVariable("x25", lowBound=0)

problem = pulp.LpProblem('0',pulp.LpMaximize)
problem += - 25*x1 - 24*x2 - 23*x3 - 22*x4 - 21*x5 \
           - 20*x6 - 19*x7 - 18*x8 - 17*x9 - 16*x10\
           - 15*x11 - 14*x12 - 13*x13 - 12*x14 - 11*x15\
           - 10*x16 - 9*x17 - 8*x18 - 7*x19 - 6*x20\
           - 5*x21 - 4*x22 - 3*x23 - 2*x24 - 1*x25, "Функция цели"

problem +=x1 + x2 + x3 + x4 + x5 <= 1, "1"
problem +=x6 +x7 + x8 + x9 + x10 <= 2, "2"
problem +=x11 + x12 + x13 + x14 + x15 <= 3, "3"
problem +=x16 + x17 + x18 + x19 + x20 <= 4, "4"
problem +=x21 + x22 + x23 + x24 + x25 <= 5, "5"

problem +=x1 + x6 + x11 + x16 + x21 == 5, "6"
problem +=x2 + x7 + x12 + x17 + x22 == 4, "7"
problem +=x3 + x8 + x13 + x18 + x23 == 3, "8"
problem +=x4 + x9 + x14 + x19 + x24 == 2, "9"
problem +=x5 + x10 + x15 + x20 + x25 == 1, "10"
problem.solve()
print ("Результат:")
for variable in problem.variables():
    print (variable.name, "=", variable.varValue)
print ("Стоимость доставки:")
print (abs(value(problem.objective)))
stop = time.time()
print ("Время :")
print(stop - start)