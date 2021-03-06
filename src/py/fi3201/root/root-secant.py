#	
#	root-secant.py
#	Finding root using secant method
#	
#	Sparisoma Viridi | https://butiran.github.io/
#	
#	Execute: py root-secant.js
#	
#	20210103
#	1042 Start this program from root-newton-raphton.py.
# 1351 Remove unecessary semicolons.
#	20210210
#	0527 Typo node --> py.
#	

# Import necessary libraries
import numpy as np


# Define a test function
def test_function(x):
	y3 = 0.01 * x * x * x
	y2 = -0.2192 * x * x
	y1 = 0.3056 * x
	y0 = 1.568
	y = y3 + y2 + y1 + y0
	return y


# Define input
f = test_function
xinit1 = 2
xinit2 = 3
eps = 1E-10
n = 0
maxstep = 40

# Define default message and parameter
xroot = "not found"
SHOW_PROGRESS = False

# Do iteration
Nstep = 0
x = []
x.append(xinit1)
x.append(xinit2)
froot = np.abs(f(x[n+1]))

while froot > eps and n < maxstep - 1:
	x.append(x[n+1] - f(x[n+1]) * (x[n+1] - x[n])  / (f(x[n+1]) - f(x[n])))
	
	froot = np.abs(f(x[n+2]))
	if froot < eps:
		xroot = x[n+2]
	
	if SHOW_PROGRESS:
		if n == 0:
			fn = f(x[n])
			print("n\tx\tf(x)")
			print(n, x[n], f(x[n]), sep="\t")
			print(n+1, x[n+1], f(x[n+1]), sep="\t")
		print(n+2, x[n+2], f(x[n+2]), sep="\t")
	
	n += 1

Nstep = n+2

if SHOW_PROGRESS:
	print()

# Display result
print("f(x)  0.01x^3 - 0.2192x^2 + 0.3056x + 1.568");
print("x1    ", xinit1, sep="")
print("x2    ", xinit2, sep="")
print("ε     ", eps, sep="")
print("Nstep ", Nstep, sep="")
print("xroot ", xroot, sep="")
