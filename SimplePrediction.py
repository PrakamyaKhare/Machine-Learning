
def pow(n,r):
	if r == 1:
		return n
	elif r == 0:
		return 1
	elif r < 0:
		res = 0
		n1 = n
		i = -1
		while i > r:
			res = n*n1
			n1 = res
			i -= 1
		return (1/res)
	else:
		res  = 0
		n1 = n
		for i  in range(r):
			res = n*n1
			n1 = res
		return res

def sigmoid(w_sum):
	e = 2.71828183
	output = 1/(1+(pow(e,-w_sum)))
	return output

def predict(x,w,b):
	y = 0
	weighted_sum = 0
	for i in range(len(x)):
		weighted_sum += x[i]*w[i]
	weighted_sum += b
	print("Weighte sum = ",weighted_sum)
	y = sigmoid(weighted_sum)
	print("Output of the neuron = ", y)
	
x = [1,-1,2]
w = [1,5,2]
b = 2
print(predict(x,w,b))
