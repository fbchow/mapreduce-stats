'''
price = alpha + beta * pop
statename, price, pop

beta = summation(pop - pop_bar)(price - price_bar) / var(pop)*n

run map reduce to compute pop, price, var(pop)
have to run 2 jobs

you can copy and paste the results of the previous job & use it in the next map-reduce
popmean = 4334234
priceman =343432
pop var = 324234

pipe output to a text file
	python nfd.py > output.txt
write output to a text file
command line argument to copy small text file to every machine

=================

Map Reduce Jobs that take in 2 files as input
	aka a join

	set up a separate mapper for each file

mapper1
	takes file1
	outputs state, price, 'price'

mapper2
	takes file2
	outputs state, pop, 'pop'
========

one mapper version
	tables to join:
		state, price       state, pop, area

'''

from mrjob.job import MRJob



class MRRegression(MRJob):
    mean_area = 74261.0980392157
    mean_pop = 4876487.7058823528
#	def mapper(self, _, line):
#		line = line.split(',')
#		price = float(line[1])
#		pop = float(line[2])		
#		yield 'key', ((pop - popmean)*(price-price_mean), 1) 
#

	def mapper(self, _, line):
	'''
	one mapper
	python djflsdj.py file1 file2
	'''
		line = line.split(',')
		if len(line) == 2:
			price  = line[1]
			yield state, (price)

		if len(line) == 3:
			pop = line[2]
			yield state, (pop)



	def reducer(self, key, values): # values = 2 values for each state (price, pop)
		# problem: how do i know the price is associated with this key, and pop for that key?
		# sol: put in some flag for the output of mapper1 and mapper2 for price & pop

		for val in values:
			if val[0] = "price":
				price = val[1]
			else:
				pop = val[1]

		yield state, price, pop 	
		

if __name__ == '__main__':
	MrRegression.run() 


