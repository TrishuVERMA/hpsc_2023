"""
A python module for calculating square root using the 
Newton's method implemented in ME522 class
"""

def cuberoot(x,debug=False):
	"""
	The cuberoot function
	Inputs
	x: the number whose cube root is to be calculated
	"""
	s=1.
	kmax=100
	tol=1.0e-14
	for k in range(kmax):
		if debug:
			print("At iteration number %s, s= %20.15f" %(k,s))
		s0=s
		s = (2*s+x/s/s)/3
		delta_s=s-s0
		if(abs(delta_s/x))<tol:
			break
	if debug:
		print("After %s iterations,  s=%20.15f" %(k+1,s))
		
	return s

def test_main():
	from numpy import cbrt
	xvalues=[0., 2., 100, 1.e6]
	for x in xvalues:
		print("Testing with x=%20.15e" %x)
		s=cuberoot(x)
		s_numpy=cbrt(x)
		print("sqrtNT s 	= %20.15e, numpy s = %20.15e" %(s,s_numpy))
		assert abs(s-s_numpy) < 1e-14, "Your sqrt does not agree with numpy sqrt"
