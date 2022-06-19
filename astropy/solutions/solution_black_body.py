from scipy.optimize import minimize

# Copy over the definition from the tutorial notebook 
@u.quantity_input(frequency=u.hertz, temperature=u.K)
def blackbody(frequency, temperature): 
        pre_factor = 2 * (const.h * frequency ** 3) / const.c ** 2
        exponential_factor = 1. / (np.exp((const.h * frequency) / (const.k_B * temperature)) - 1)
        return pre_factor * exponential_factor


# Define the objective function that shall be minimized
# We introduce x = np.log(frequency) => frequency = np.exp(x)
# And convert the radiance to well defined units and take the negative logarithm
def objective_funtion(x):
        frequency = u.Quantity(np.exp(x) , unit="Hz", copy=False)
        radiance = blackbody(frequency=frequency, temperature=5000 * u.K)
        value = -np.log(radiance.to_value('Hz3 J s3 / m2'))
        return value
                             
result = minimize(objective_funtion, x0=np.log(1E14), method='Nelder-Mead') 
#We minimize over log(frequency)
frequency_max = np.exp(result['x']) * u.Hz

# Equation taken from https://en.wikipedia.org/wiki/Wien%27s_displacement_law#Alternate_Maxima
@u.quantity_input(temperature=u.K)
def wiens_displacement_law(temperature):
    return 0.058789e12 * u.Unit("Hz /K") * temperature

frequency_max_wien = wiens_displacement_law(temperature=5000*u.K)

print("The numerical optimization gives: {[0]:.3e}".format(frequency_max))
print("Wien's displacement law gives   : {:.3e}".format(frequency_max_wien))
