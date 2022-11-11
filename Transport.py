import numpy
from cvxopt.modeling import variable, op
def count(mass1, mass2, mass3, mass4, mass5, mass6, z):
         x_non_negative = (x >= 0) #загальна умова для всіх х
         problem = op (z, [mass1, mass2, mass3, mass4, mass5, mass6, x_non_negative])
         problem.solve(solver='glpk')
         problem.status
         print("Мінімальна вартість закупівлі -",problem.objective.value()[0])
         print("Матриця закупівель:")
         for i in [1,4,7]:
                  print("|",x.value[i-1],"|", x.value[i],"|", x.value[i+1],"|")
x = variable(9, 'x')
z=(7*x[0] + 3*x[1] +6* x[2] +4*x[3] + 8*x[4] +2* x[5]+x[6] + 5*x[7] +9* x[8])# цільова функція
mass1 = (x[0] + x[1] +x[2] <= 74)# умова для першого рядка матриці закупівель
mass2 = (x[3] + x[4] +x[5] <= 40)#умова для другого рядка матриці закупівель
mass3 = (x[6] + x[7] + x[8] <= 36)# #умова для третього рядка матриці закупівель
mass4 = (x[0] + x[3] + x[6] == 20)# умови для стовпця
mass5 = (x[1] +x[4] + x[7] == 45)#умови для стовпця
mass6 = (x[2] + x[5] + x[8] == 30)#умови для стовпця
count (mass1, mass2, mass3, mass4, mass5, mass6,z)