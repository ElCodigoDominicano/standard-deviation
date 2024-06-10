def standard_deviation(data: list[int | float]) -> int | float:
    """Find the standard deviation from a list of integers.
    
    got inspired to just "Not search for a function." but
    "To search for its formula and build a function based
    on instructions." 

    instructions obtained from watching 2 very informative 
    youtubers on YouTube @SirBernieReyes and @TheOrganicChemistryTutor 
    their breakdown and explaination on Variance and Standard Deviation.
    
    Author: AERivas
    Date: 06/10/2024
    """
    sum_data = sum(data)
    len_data = len(data)
    mean_data = sum_data / len_data
    difference = [num - mean_data for num in data]
    squared_difference = [diff ** 2 for diff in difference]
    sum_of_squared_differences = sum(squared_difference)
    result = sum_of_squared_differences / (len_data - 1)
    return math.sqrt(result)
