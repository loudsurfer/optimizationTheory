from cvxopt.modeling import variable, op
import time
start = time.time()
x = variable(25, 'x')

z =          25*x[0]    + 24*x[1]   + 23*x[2]   + 22*x[3]   + 21*x[4]   \
           + 20*x[5]    + 19*x[6]   + 18*x[7]   + 17*x[8]   + 16*x[9]   \
           + 15*x[10]   + 14*x[11]  + 13*x[12]  + 12*x[13]  + 11*x[14]  \
           + 10*x[15]   + 9*x[16]   + 8*x[17]   + 7*x[18]   + 6*x[19]   \
           + 5*x[20]    + 4*x[21]   + 3*x[22]   + 2*x[23]   + 1*x[24]

mass1 = (x[0] + x[1] + x[2] + x[3] + x[4] <= 1)
mass2 = (x[5] + x[6] + x[7] + x[8] + x[9] <= 2)
mass3 = (x[10] + x[11] + x[12] + x[13] + x[14] <= 3)
mass4 = (x[15] + x[16] + x[17] + x[18] + x[19] <= 4)
mass5 = (x[20] + x[21] + x[22] + x[23] + x[24] <= 5)

mass6 = (x[0] + x[5] + x[10] + x[15] + x[20] == 5)
mass7 = (x[1] + x[6] + x[11] + x[16] + x[21] == 4)
mass8 = (x[2] + x[7] + x[12] + x[17] + x[22] == 3)
mass9 = (x[3] + x[8] + x[13] + x[18] + x[23] == 2)
mass10 = (x[4] + x[9] + x[14] + x[19] + x[24] == 1)

x_non_negative = (x >= 0)
problem =op(z,[mass1,mass2,mass3,mass4 ,mass5,mass6,mass7,mass8,mass9,mass10, x_non_negative])
problem.solve(solver='glpk')
problem.status
print("Результат:")
print(x.value)
print("Стоимость доставки:")
print(problem.objective.value()[0])
stop = time.time()
print ("Время :")
print(stop - start)