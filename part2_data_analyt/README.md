The repository contains scripts for cleaning and analyzing a real estate dataset and training machine learning models to predict house prices. The Markdown cells in the associated Jupyter notebook provide documentation for part 2 of the analysis. Below is a technical overview that would help to set up and run the code.

# Requirements
Before running the code, make sure the following libraries are installed. We can install them using pip or conda.

kaggle (for fetching the dataset off Kaggle)

pandas (used for data manipulation and analysis)

numpy (for numerical operations)

matplotlib (to visualize data)

scikit-learn (for machine learning models and evaluation)

# Machine Learning Models
We use multiple machine learning models to predict house prices.

Linear Regression: Simple regression to which houses gives continuous predictions.

Lasso Regression: A linear regression to which regularization is applied to avoid overfitting.

Decision Tree Regressor: It works as a non-linear model on different decision nodes, splitting up the data into the decision nodes based on feature values.

Hyperparameter Tuning
In addition to the simple models, we perform hyperparameter tuning using GridSearchCV to choose the best parameters from a defined set.
