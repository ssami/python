def return_lots(base_num) : 
	power_two = base_num * base_num
	half = base_num / 2
	double = base_num * 2
	return power_two, half, double

num = 100
exp2, div2, time2 = return_lots(num)
print "%s to the power of 2 is %d. Half of %s is %d. And twice of %s is %d" % (num, exp2, num, div2, num, time2)

