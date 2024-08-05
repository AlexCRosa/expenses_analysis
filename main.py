import pandas as pd
from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv('path_to_your_csv_file.csv')

# Load the Llama 3 model and tokenizer
model_name = "meta-llama/Meta-Llama-3-8B"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Create a text classification pipeline
classifier = pipeline('text-classification', model=model, tokenizer=tokenizer)

# Example function to categorize expenses
def categorize_expense(description):
    result = classifier(description)
    return result[0]['label']

# Apply the function to the 'description' column
df['category'] = df['description'].apply(categorize_expense)

# Group by category and sum the amounts
category_sums = df.groupby('category')['amount'].sum()

# Plot a pie chart
plt.figure(figsize=(10, 6))
category_sums.plot(kind='pie', autopct='%1.1f%%', startangle=140)
plt.title('Expenses by Category')
plt.ylabel('')  # Hide the y-label
plt.show()
