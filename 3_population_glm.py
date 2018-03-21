'''
find <alpha> and <beta> that minimize the squared residuals when the state data is represented using this model
Use linear regression to fit the following simple model

Population = Area * <beta> + <alpha>

formula for OLS:
    
beta = sum(xi-xbar)(yi-ybar))/ n*var_x 

alpha = y_hat - beta

'''

from mrjob.job import MRJob

# outuputs computed from previous problems
pop_mean = 4876487.7058823528
area_var = 9006334405.7747020721 
area_mean = 74261.098 

class MRRegression(MRJob):

    def mapper(self, _, line):
        line = line.split(',')
        area = float(line[3])
        pop = float(line[4])
        xy = (area - area_mean)*(pop - pop_mean)
        yield 'key', (xy, 1) 
    
    def combiner(self, key, some_vals):
        count = 0
        s_xy = 0 

        for val in some_vals:
            count += val[1]
            s_xy += val[0]
        yield 'key', (s_xy, count)

    def reducer(self, _, values):
        count = 0
        s_xy = 0
        
        for val in values:
            s_xy = val[0]
            count = val[1]

        beta = s_xy/(count*area_var)
        alpha = pop_mean - (beta*area_mean) 
            
        yield 'slope', beta
        yield 'intercept', alpha

if __name__ == '__main__':
	MRRegression.run()
