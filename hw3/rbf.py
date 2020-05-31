import numpy as np
from numpy import linalg as LA


sig = 1
lr = 1

x1 = np.array([0, 0])
x2 = np.array([0, -1])
x3 = np.array([-1, 0])
x4 = np.array([-1, -1])

t1 = 1
t2 = 0
t3 = 0
t4 = 1

c1 = np.array([0, -0.5])
c2 = np.array([-1, -0.5])

w = np.array([1, 1])
b = 1

def fi(x, c):
	return np.exp(-(LA.norm(x - c)**2)/(2*sig**2))

def out(x, c1, c2, w, b):
	return fi(x, c1) * w[0] + fi(x, c2) * w[1] + b

def sigma(x, c1, c2, w, b):
	return np.exp(out(x, c1, c2, w, b))/(1 + np.exp(out(x, c1, c2, w, b)))

def update_w_b(x, c1, c2, w, b, t):
	new_w = [0, 0]
	new_w[0] = w[0]
	new_w[1] = w[1]

	new_w[0] = w[0] + lr * (t - sigma(x, c1, c2, w, b)) * fi(x, c1)

	new_w[1] = w[1] + lr * (t - sigma(x, c1, c2, w, b)) * fi(x, c2)

	new_b = b + (t - sigma(x, c1, c2, w, b)) * 1

	return new_w, new_b


for i in range(12):
	if(i == 0 or i == 4 or i == 8):
		x = x1
		t = t1
	if(i == 1 or i == 5 or i == 9):
		x = x2
		t = t2
	if(i == 2 or i == 6 or i == 10):
		x = x3
		t = t3 
	if(i == 3 or i == 7 or i == 11):
		x = x4
		t = t4

	print(i)
	print("phi_1 = " + str(fi(x, c1)) + "   phi_2 = " + str(fi(x, c2)))
	print("F(x) = " + str(out(x, c1, c2, w, b)))
	print("sigma = " + str(sigma(x, c1, c2, w, b)))
	w, b = update_w_b(x, c1, c2, w, b, t)
	print("w" + str(i) +" = [" + str(w[0]) + ", " + str(w[1]) + "] | b" + str(i) + " = " + str(b) + "\n")




x5 = np.array([1, 1])

print(fi(x5, c1))
print(fi(x5, c2))
print(out(x5, c1, c2, w, b))
print(sigma(x5, c1, c2, w, b))


