def standard_deviation(data: list[int | float], sample_deviation=False) -> int | float:
    """Find the standard deviation (population, by default when 
    sample_deviation set to False) from a list of numbers.
    
    got inspired to just "Not search for a function." but
    "To search for its formula and build a function based
    on instructions." 

    instructions obtained from watching 2 very informative 
    youtubers on YouTube @SirBernieReyes and @TheOrganicChemistryTutor 
    their breakdown and explaination on Variance and Standard Deviation.

    Parameter: data, a list containing numbers datatype int or float.
    Parameter: sample_deviation, a boolean datatype False or True to calculate
    sample_deviation and not population standard deviation.

    Author: AERivas
    Date: 06/10/2024 Update: 06/11/2024
    """
    import math

    sum_data = sum(data)
    len_data = len(data)
    mean_data = sum_data / len_data
    difference = [num - mean_data for num in data]
    squared_difference = [diff ** 2 for diff in difference]
    sum_of_squared_differences = sum(squared_difference)
    population_standard_deviation = sum_of_squared_differences / (len_data - 1)
    sample_standard_deviation = sum_of_squared_differences / len_data
    result = population_standard_deviation if not sample_deviation else sample_standard_deviation  
    return math.sqrt(result)