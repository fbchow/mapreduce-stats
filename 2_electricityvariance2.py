
from mrjob.job import MRJob

class MRElectricityVariance(MRJob):

	def mapper (self,_,line):
		line = line.split(',')
		state = line[0]
		price = float(line[1])
		yield 'key', (price, price*price, 1)

	def combiner (self, key, somevals):
		sum = 0
		count = 0
		sum_square = 0
		for val in somevals:
			sum += val[0]
			sum_square += val[1]
			count += val[2]
		yield 'key', (sum, sum_square, count)


	def reducer (self, key, values):
		sum = 0
		count = 0
		sum_square = 0
		for val in values:
			sum += val[0]
			sum_square += val[1]
			count += val[2]
		yield 'var', sum_square/count - sum*sum/(count*count)

if __name__ == '__main__':
	MRElectricityVariance.run()

