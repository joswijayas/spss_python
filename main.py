# import pandas as pd

# # Load your data from the CSV file
# data = pd.read_csv('crop - data.csv')

# subindicator_columns = ['LGN', 'LGP', 'STI', 'STV', 'DGK', 'DGP', 'NTL', 'NTF', 'ITM', 'ITA', 'LIL', 'LIV', 'PPC', 'PPT', 'BDK', 'BDP', 'TCP', 'TCH', 'MSP', 'MSA', 'IPA', 'IPE', 'PCV', 'PCU', 'LDP', 'LDM', 'ETM', 'ETA', 'ASD', 'ASL']

# # Loop through each subindicator column and convert to numeric, handling missing values
# for subindicator in subindicator_columns:
#     data[subindicator] = pd.to_numeric(data[subindicator], errors='coerce')
#     data[subindicator].fillna(0, inplace=True)
# # Define a function to calculate statistics for subindicators
# def calculate_subindicator_stats(subindicator_names):
#     return data[subindicator_names].agg(['mean', 'median', 'std', 'min', 'max'])

# # Create a dictionary to map dimensions to their subindicators
# dimension_to_subindicators = {
#     'LG': ['LGN', 'LGP']
#     # 'ST': ['STI', 'STV'],
#     # 'DG': ['DGK', 'DGP'],
#     # 'NT': ['NTL', 'NTF'],
#     # 'IT': ['ITM', 'ITA'],
#     # 'LI': ['LIL', 'LIV'],
#     # 'PP': ['PPC', 'PPT'],
#     # 'BD': ['BDK', 'BDP'],
#     # 'TC': ['TCP', 'TCH'],
#     # 'MS': ['MSP', 'MSA'],
#     # 'IP': ['IPA', 'IPE'],
#     # 'PC': ['PCV', 'PCU'],
#     # 'LD': ['LDP', 'LDM'],
#     # 'ET': ['ETM', 'ETA'],
#     # 'AS': ['ASD', 'ASL']
# }

# # Create an empty DataFrame to store the descriptive statistics
# dimension_stats = pd.DataFrame()

# # Iterate over dimensions and calculate statistics
# for dimension, subindicators in dimension_to_subindicators.items():
#     subindicator_stats = calculate_subindicator_stats(subindicators)
#     print(subindicator, subindicator_stats)
#     subindicator_stats.columns = [f"{subindicator}_Stats" for subindicator in subindicators]
#     dimension_stats[f"{dimension}_Indicator"] = subindicator_stats.values.flatten()

# # Transpose the DataFrame to have statistics as rows and dimensions as columns
# dimension_stats = dimension_stats.transpose()

# # Print or export the descriptive statistics for each dimension
# print(dimension_stats)


#===============================================================================


# import pandas as pd
# from scipy import stats

# # Load user questionnaire data from a CSV file or another source
# user_data = pd.read_csv('crop - data.csv')

# # Define the desired confidence level (e.g., 95% confidence interval)
# confidence_level = 0.95

# # Calculate statistics for each dimension
# dimensions = ['LG'
#             #   , 'ST', 'DG', 'NT', 'IT', 'LI', 'PP', 'BD', 'TC', 'MS', 'IP', 'PC', 'LD', 'ET', 'AS'
#               ]

# dimension_stats = {}

# for dimension in dimensions:
#     dimension_data = user_data[dimension]
    
#     # Calculate statistics
#     mean = dimension_data.mean()
#     median = dimension_data.median()
#     variance = dimension_data.var()
#     std_deviation = dimension_data.std()
#     min_value = dimension_data.min()
#     max_value = dimension_data.max()
#     data_range = max_value - min_value
#     total_sum = dimension_data.sum()
    
#     # Calculate the confidence interval for the mean
#     n = len(dimension_data)
#     std_error = std_deviation / (n ** 0.5)
#     confidence_interval = stats.t.interval(confidence_level, df=n - 1, loc=mean, scale=std_error)
    
#     # Store the results in a dictionary
#     dimension_stats[dimension] = {
#         'Mean': mean,
#         'Confidence Interval (Lower Bound)': confidence_interval[0],
#         'Confidence Interval (Upper Bound)': confidence_interval[1],
#         'Median': median,
#         'Variance': variance,
#         'Standard Deviation': std_deviation,
#         'Minimum': min_value,
#         'Maximum': max_value,
#         'Range': data_range,
#         'Sum': total_sum
#     }

# # Display or print the statistics for each dimension
# for dimension, stats in dimension_stats.items():
#     print(f"Dimension: {dimension}")
#     print(f"Mean: {stats['Mean']:.2f}")
#     print(f"95% Confidence Interval (Lower Bound): {stats['Confidence Interval (Lower Bound)']:.2f}")
#     print(f"95% Confidence Interval (Upper Bound): {stats['Confidence Interval (Upper Bound)']:.2f}")
#     print(f"Median: {stats['Median']:.2f}")
#     print(f"Variance: {stats['Variance']:.2f}")
#     print(f"Standard Deviation: {stats['Standard Deviation']:.2f}")
#     print(f"Minimum: {stats['Minimum']:.2f}")
#     print(f"Maximum: {stats['Maximum']:.2f}")
#     print(f"Range: {stats['Range']:.2f}")
#     print(f"Sum: {stats['Sum']:.2f}")
#     print('\n')

import pandas as pd
from scipy import stats

# Load your user questionnaire data from a CSV file
user_data = pd.read_csv('crop - data.csv')
user_data = user_data.apply(pd.to_numeric, errors='coerce')


# Define the desired number of classes
num_classes = 3

# Create a dictionary to store classification intervals and statistics for each dimension
dimension_stats_intervals = {}

# Iterate through dimensions
dimensions = ['LG'
              , 'ST', 'DG', 'NT', 'IT', 'LI', 'PP', 'BD', 'TC', 'MS', 'IP', 'PC', 'LD', 'ET', 'AS'
              ]

for dimension in dimensions:
    dimension_data = user_data[dimension]

    # Calculate statistics
    mean = dimension_data.mean()
    median = dimension_data.median()
    variance = dimension_data.var()
    std_deviation = dimension_data.std()
    min_value = dimension_data.min()
    max_value = dimension_data.max()
    data_range = max_value - min_value
    total_sum = dimension_data.sum()

    # Calculate the 95% confidence interval for the mean
    n = len(dimension_data)
    std_error = std_deviation / (n ** 0.5)
    confidence_interval = stats.t.interval(0.95, df=n - 1, loc=mean, scale=std_error)

    # Calculate the interval width
    interval_width = data_range / num_classes

    # Check if the interval width results in an "out of control" situation
    if interval_width < (max_value - min_value) / (num_classes + 1):
        # Adjust the interval width to ensure it includes the min and max values
        interval_width = (max_value - min_value) / (num_classes + 1)

    # Create intervals based on the adjusted interval width
    intervals = [min_value + i * interval_width for i in range(num_classes)] + [max_value]

    # Define class labels
    class_labels = ['Feeble', 'Medium', 'Strong']

    # Assign class labels to data based on intervals
    class_column = pd.cut(dimension_data, bins=intervals, labels=class_labels, include_lowest=True)

    # Calculate the class with the highest count
    class_counts = class_column.value_counts()
    most_frequent_class = class_counts.idxmax()

    # Store the statistics and classification intervals for the dimension
    dimension_stats_intervals[dimension] = {
        'Mean': mean,
        'Confidence Interval (Lower Bound)': confidence_interval[0],
        'Confidence Interval (Upper Bound)': confidence_interval[1],
        'Median': median,
        'Variance': variance,
        'Standard Deviation': std_deviation,
        'Minimum': min_value,
        'Maximum': max_value,
        'Range': data_range,
        'Sum': total_sum,
        'Intervals': intervals,
        'Class Labels': class_labels,
        'Classifications': class_column,
        'Most Frequent Class': most_frequent_class
    }

# Display or print the statistics and classification intervals for each dimension
for dimension, info in dimension_stats_intervals.items():
    print(f"Dimension: {dimension}")
    print(f"Mean: {info['Mean']:.2f}")
    print(f"95% Confidence Interval (Lower Bound): {info['Confidence Interval (Lower Bound)']:.2f}")
    print(f"95% Confidence Interval (Upper Bound): {info['Confidence Interval (Upper Bound)']:.2f}")
    print(f"Median: {info['Median']:.2f}")
    print(f"Variance: {info['Variance']:.2f}")
    print(f"Standard Deviation: {info['Standard Deviation']:.2f}")
    print(f"Minimum: {info['Minimum']:.2f}")
    print(f"Maximum: {info['Maximum']:.2f}")
    print(f"Range: {info['Range']:.2f}")
    print(f"Sum: {info['Sum']:.2f}")
    print(f"Intervals: {info['Intervals']}")
    print(f"Class Labels: {info['Class Labels']}")
    print(f"Classifications:\n{info['Classifications'].value_counts()}\n")
    print(f"Classifications:\n{info['Classifications'].value_counts()}\n")
