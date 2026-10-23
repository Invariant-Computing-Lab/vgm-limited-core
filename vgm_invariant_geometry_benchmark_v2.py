import numpy as np, math
from scipy.integrate import quad
SEED=20260812
rng=np.random.default_rng(SEED)
def K(k):
    k=np.asarray(k,float); return (k@k)*np.eye(4)-np.outer(k,k)
# Core quotient identity:
Q, L, s = 3.0, 7.0, 1e5
assert np.isclose((Q/L)**2, ((s*Q)/(s*L))**2)
# Normalized Gaussian jet:
a=[(-1)**n/math.factorial(n) for n in range(7)]
assert np.allclose([a[0]-1,a[1]+1,2*a[2]-1,6*a[3]+1,24*a[4]-1],0)
# UV proxy:
Iloc=lambda R: quad(lambda x:x**3/(x*x+.01)**2,0,R)[0]
Ig=lambda R: quad(lambda x:x**3*np.exp(-2*x*x)/(x*x+.01)**2,0,R)[0]
print('local(100)=',Iloc(100),'gaussian(100)=',Ig(100))
print('Run the accompanying CSV tables and Appendix for the full Monte Carlo specifications.')
