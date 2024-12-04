'''
Names: Elizabeth Boulay, Eliana Leventhal, and Gabrielle Nunez
Course: COMSC.230.02
Prof. Name: Dr. Rivera Morales
Assignment: Final Project: Dataset Analysis
Program Name: wine_correlations.py
Program brief description: Script for reading in dataset and finding correlations between attributes. Prints statistical description as well.
'''

import pandas as pd
import matplotlib.pyplot as plt

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
#print("Correlation Matrix:")
#print(correlation_matrix)

# Save the correlation matrix to a CSV file
correlation_matrix.to_csv("correlation_matrix.csv", index=True)

# Statistical Description
wine_stats = wine_data.describe()
wine_stats.to_csv("wine_stats.csv", index=True)

#print(wine_stats)

# Calculate the average of flavanoids within each class
average_flavanoids = wine_data.groupby('Class')['Flavanoids'].mean()
average_totalphenols = wine_data.groupby('Class')['Total_Phenols'].mean()

# Output the results
#print("Average Flavanoids by Class:")
#print(average_flavanoids)
#print("Average Total Phenols by Class:")
#print(average_totalphenols)

# Plot Flavanoids vs Class
plt.subplot(1, 2, 1)
plt.scatter(wine_data['Class'], wine_data['Flavanoids'], color='blue', alpha=0.7, label='Flavanoids')
plt.xlabel('Class')
plt.xticks([1, 2, 3])
plt.ylabel('Flavanoids')
plt.title('Flavanoids vs Class')
plt.legend()

# Plot Total Phenols vs Class
plt.subplot(1, 2, 2)
plt.scatter(wine_data['Class'], wine_data['Total_Phenols'], color='green', alpha=0.7, label='Total Phenols')
plt.xlabel('Class')
plt.xticks([1, 2, 3])
plt.ylabel('Total Phenols')
plt.title('Total Phenols vs Class')
plt.legend()

# Show the plot
plt.tight_layout()
plt.show()
