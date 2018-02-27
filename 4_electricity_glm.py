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
	outputs state, price

mapper2
	takes file2
	outputs state, pop

'''

from mrjob.job import MRJob

class MRPriceRegression(MRJob):


	def mapper(self, _, line):
		line = line.split(',')
		price = float(line[1])
		pop = float(line[2])		
		yield 'key', ((pop - popmean)*(price-price_mean), 1) 


	#def reducer(self, key, line):


if __name__ == '__main__':
	MRPriceRegression.run() 


