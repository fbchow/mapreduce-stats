'''
find <alpha> and <beta> that minimize the squared residuals when the state data is represented using this model
Use linear regression to fit the following simple model

Population = Area * <alpha> + <beta>
'''

from mrjob.job import mrjob

class MRRegression():


    def mapper(self, _, line):
        line = line.split()


    def reduce(self, _, line):


        yield   



