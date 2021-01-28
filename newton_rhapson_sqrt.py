# estimate x^2 = k --> x = sqrt(k)
def sqrt_newton_rhapson(k):
	# initial guess:
	# let me just reuse k for the initial x0
	x_n = k
	# repeat until the difference x_n^2 and k 
	# with respect to user threshold
	thres = 0.000001
	# to prevent the infinite loop
	# we count the iterations
	# and stop if it reaches the max_iter
	# you can change the max_iter but kind of useless I guess
	# Note that the Newton Rhapson method may not work well in some cases.
	MAX_ITER = 10000
	i = 0
	while i < MAX_ITER:
		# for a slope of f(x_n), we need to differentiate the f(x)
		# but as we know f'(x) = 2x
		# simply f'(x_n) = 2 * x_n
		# f(x_n) = x_n * x_n - k
		x_n = x_n - (x_n * x_n - k) / (2* x_n)
		# check if we've found the root 
		if abs(x_n * x_n - k) < thres:
			return x_n
		i += 1
	# if not converged in a desired number of iterations, report failure
	return False

import math
# compare math.sqrt function and our estimator
print(math.sqrt(20), sqrt_newton_rhapson(20))
print(math.sqrt(834.3453), sqrt_newton_rhapson(834.3453))
print(math.sqrt(2345346340), sqrt_newton_rhapson(2345346340))