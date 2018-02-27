'''
price = alpha + beta * pop
statename, price, pop

beta = summation(pop - pop_bar)(price - price_bar) / var(pop)*n

run map reduce to compute pop, price, var(pop)
have to run 2 jobs
'''


class MRPriceRegression(MRJob):


	def mapper(self, _, line):






	def reducer(self, key, line):





