# Real Estate Price Prediction - Gurgaon Properties

## Project Overview

This project analyzes real estate data from Gurgaon and builds machine learning models to predict property prices. It covers the full pipeline — data cleaning, exploratory analysis, feature engineering, model training, and a recommendation system — using flats and independent houses data scraped/collected from the Gurgaon property market.

## Dataset Description

- **flats.csv** - Raw flats data
- **houses.csv** - Raw independent houses data
- **appartments.csv** - Apartment listings
- **gurgaon_properties.csv** - Merged dataset combining flats and houses
- **latlong.csv** - Latitude/longitude mapping for locations, used for map-based features

## Project Structure

### 1. Data Cleaning
- `flats_cleaning.ipynb` — Cleaning and preprocessing raw flats data
- `house_cleaning.ipynb` — Cleaning and preprocessing raw houses data
- `merging_flats_and_houses.ipynb` — Combining flats and houses into a single dataset

### 2. Exploratory Data Analysis
- `pandas_profiling.ipynb` — Automated data profiling report
- `univariate_analysis.ipynb` — Single-variable distribution analysis
- `multivariate analysis.ipynb` — Correlation and multi-variable analysis
- `output_report.html` — Exported HTML report of the profiling analysis
- `insights.ipynb` — Key findings and insights from the exploration phase

### 3. Feature Engineering & Selection
- `feature_engineering.ipynb` — Creating new features and transformations
- `missing_value_imputation.ipynb` — Handling missing values
- `outlier_detection.ipynb` — Identifying and treating outliers
- `Feature_Selection.ipynb` — Selecting the most relevant features for modeling

### 4. Modeling
- `Baseline_model.ipynb` — Initial baseline model
- `model_selection.ipynb` — Comparing algorithms and selecting the best-performing model
- `pipeline.pkl` — Serialized end-to-end trained pipeline (preprocessing + model)
- `regenerate_pickle.py` — Script to regenerate the pipeline/model pickle files locally

### 5. Recommender System
- `Recommender_system.ipynb` — Builds a property recommendation engine
- `cosine_sim1.pkl`, `cosine_sim2.pkl`, `cosine_sim3.pkl` — Precomputed cosine similarity matrices used for recommending similar properties
- `location_df.pkl`, `feature_text.pkl`, `df.pkl` — Supporting data used by the recommender

### 6. Application
- `Home.py` — Entry point for the web app (Streamlit) that serves predictions and recommendations
- `pages/` — Additional app pages/screens

## Key Property Features Used

- Property type, society, price, price per sqft
- Built-up area, number of bedrooms, bathrooms, balconies
- Age of possession, furnishing type
- Luxury category, floor category
- Additional amenities

## Machine Learning Approach

- **Target Variable**: Property price (log-transformed)
- **Preprocessing**: One-hot encoding for categorical features, standard scaling for numerical features
- **Validation**: Cross-validation across multiple folds
- **Evaluation Metric**: R² score

## Technologies Used

- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib / Seaborn
- Streamlit (for the app interface)
- Jupyter Notebooks

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/NIKIT0501/GurgaonPropertyAnalytics--main.git
   cd GurgaonPropertyAnalytics--main
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Regenerate the trained model/pickle files (not stored in the repo — see note below):
   ```bash
   python regenerate_pickle.py
   ```

4. Run the app:
   ```bash
   streamlit run Home.py
   ```

> **Note:** Large `.pkl` files (trained models, similarity matrices) are excluded from this repository via `.gitignore` to keep the repo lightweight. Run `regenerate_pickle.py` and the relevant notebooks to regenerate them locally after cloning.

## Project Workflow

1. Clean and merge raw data (`flats_cleaning`, `house_cleaning`, `merging_flats_and_houses`)
2. Explore the data (`pandas_profiling`, `univariate_analysis`, `multivariate analysis`)
3. Engineer and select features (`feature_engineering`, `missing_value_imputation`, `outlier_detection`, `Feature_Selection`)
4. Train and evaluate models (`Baseline_model`, `model_selection`)
5. Build the recommender system (`Recommender_system`)
6. Serve results through the Streamlit app (`Home.py`)

## Future Enhancements

- Experiment with advanced models (Random Forest, XGBoost, Neural Networks)
- Hyperparameter tuning
- Deploy as a hosted web application
- Real-time price prediction API
- Incorporate additional data sources

---

*This project demonstrates an end-to-end data science workflow for real estate price prediction and property recommendation in the Gurgaon market.*

