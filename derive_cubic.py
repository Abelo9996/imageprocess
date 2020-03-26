import matplotlib.pyplot as plt
import numpy as np
import sympy

a, b, c, d, x, alpha, beta = sympy.symbols('a b c d x alpha beta')

f = a*x**3 + b*x**2 + c*x + d

fp = f.diff(x)

f0 = f.subs(x, 0)
f1 = f.subs(x, 1)
fp0 = fp.subs(x, 0)
fp1 = fp.subs(x, 1)


S = sympy.solve([f0, f1, fp0-alpha, fp1-beta], [a, b, c, d])

coeffs = []

num_alpha = 0.3
num_beta = 0.03

for key in [a, b, c, d]:
    print key, '=', S[key]
    coeffs.append(S[key].subs(dict(alpha=num_alpha,
                                   beta=num_beta)))

xvals = np.linspace(0, 1, 101)
yvals = np.polyval(coeffs, xvals)

plt.plot(xvals, yvals)
plt.show()

