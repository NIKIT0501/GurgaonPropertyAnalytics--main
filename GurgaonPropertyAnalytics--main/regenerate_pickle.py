import pandas as pd
import pickle

# Read the cleaned data
try:
    print("Reading cleaned data file...")
    df = pd.read_csv('gurgaon_properties_cleaned_v2.csv')
    
    # Save as pickle
    print("Saving as pickle...")
    with open('df.pkl', 'wb') as f:
        pickle.dump(df, f)
    
    print("Successfully regenerated df.pkl")
    print("\nDataFrame columns:", df.columns.tolist())
    print("\nFirst 2 rows:")
    print(df.head(2).to_string())
    
except Exception as e:
    print("Error:", str(e))
