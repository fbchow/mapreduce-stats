'''Calculate the variance in electricity prices among the states.'''

from mrjob.job import MRJob

class MRElectricityVariance(MRJob):
	def mapper(self, _, line):
		line = line.split(',')
		state = line[0]	
		price = line[1]
		yield 'key', (price, price*price, 1) # add 1 to indicate entity for combiner to count

	def combiner(self, key, some_vals):
		'''
		only takes in some of the values associated with the key -- unlike reducer
		'''
	sum = 0
	count = 0
	sum_square = 0
	for val in some_vals:
		sum += val[0]
		sum_square += val[1]
		count += val[2]
	yield "key", (sum, sum_square, count)	
	

	def reducer(self, key, values):
		values = list(values)	
#		ex_x = sum(values) / len(values)
		
		sum = 0
		count = 0
		sum_square = 0

		for val in values:
			sum += val[0]
			sum_square += val[1]
			count += 1
		yield "var", (sum_square/count) - (sum*sum/(count*count))		


if __name__ == '__main__':
	MRElectricityVariance.run()
