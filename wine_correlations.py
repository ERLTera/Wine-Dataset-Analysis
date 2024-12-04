import pandas as pd

# Define column names
columns = [
    'Class', 'Alcohol', 'Malicacid', 'Ash', 'Alcalinity_of_Ash', 'Magnesium',
    'Total_Phenols', 'Flavanoids', 'Nonflavanoid_Phenols', 'Proanthacyanins',
    'Color_Intensity', 'Hue', '0D280/0D315_of_Diluted_Wine', 'Proline'
]

# Load the dataset
wine_data = pd.read_csv("wine.data", names=columns)

# Calculate correlations for every combination of columns
correlation_matrix = wine_data.corr()

# Output the correlation matrix
print("Correlation Matrix:")
print(correlation_matrix)

# Save the correlation matrix to a CSV file
correlation_matrix.to_csv("correlation_matrix.csv", index=True)

wine_stats = wine_data.describe()
wine_stats.to_csv("wine_stats.csv", index=True)

print(wine_stats)

