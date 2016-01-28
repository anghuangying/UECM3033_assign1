import sympy as sy
import numpy as np

def fun_1( your_id ):
    ans = hex(your_id)
    return ans

def my_integral():
    x = sy.Symbol('x')
    ans = sy.integrate( (2*x)*sy.cos(3*x+ sy.pi), (x,sy.pi/3,sy.pi/6))
    return ans

def my_solution():
    A = np.array( [[1,2,3,4,5,6,7,8,9,10], 
                            [2,3,4,5,6,7,8,9,0,11], 
                            [3,4,5,6,7,8,9,10,11,12], 
                            [4,5,6,7,8,9,0,11,12,13], 
                            [5,6,7,8,9,10,11,12,13,14],
                            [6,7,8,9,0,11,12,13,14,15],
                            [7,8,9,10,11,12,13,14,15,16], 
                            [8,9,0,11,12,13,14,15,16,17],
                            [9,10,11,12,13,14,15,16,17,18], 
                            [0,11,12,13,14,15,16,17,18,19]] )
    b = np.array([405,395,545,555,685,665,825,825,965,985])
    x = np.linalg.solve(A,b) # Solve Ax = b
    return x


if __name__ == '__main__':
    your_id = 1307589
    print('Hexadecimal representation of %d is %s'%( your_id, fun_1( your_id) ))
    print('Integral = ', my_integral())
    print('Solution = ', my_solution())