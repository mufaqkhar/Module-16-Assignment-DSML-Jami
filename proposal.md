# Research Proposal: Predicting Diabetes Disease Progression from BMI

## 1. Research question
**How well does a single baseline predictor, standardized body mass index (BMI), explain and predict a quantitative diabetes disease progression score measured one year later?**

This is a basic **simple linear regression** task with one numerical predictor and one numerical target. The goal is educational model evaluation, not clinical diagnosis.

## 2. Dataset and source
- **Dataset:** Diabetes regression dataset, distributed publicly with scikit-learn (`sklearn.datasets.load_diabetes`).
- **Official dataset description:** https://scikit-learn.org/stable/datasets/toy_dataset.html#diabetes-dataset
- **Dataset loader:** https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html
- **Observations:** 442.
- **Available features:** 10 standardized baseline measurements, including age, sex, BMI, blood pressure, and blood serum measurements.
- **Feature selected:** `bmi` (`data[:, 2]`), a *standardized* BMI variable rather than raw BMI in kg/m².
- **Target:** Quantitative measure of diabetes disease progression one year after baseline.
- **Project file:** `data/diabetes_bmi.csv`, a faithful two-column export of the public bundled dataset.

## 3. Short scan of existing work (two sources)

**Source 1 — Efron, B., Hastie, T., Johnstone, I., & Tibshirani, R. (2004).** *Least Angle Regression.* Annals of Statistics, 32(2), 407–499. https://doi.org/10.1214/009053604000000067

This paper introduces least angle regression (LARS), a method for fitting and selecting variables in linear models, and uses diabetes data to illustrate regression with multiple baseline predictors. It shows that the diabetes dataset is a recognized example for investigating linear relationships. **Relation to this project:** Instead of the paper's more advanced variable-selection techniques, this assignment deliberately starts with only BMI and ordinary least squares as an interpretable baseline. Results from the paper are not assumed to be directly comparable to our one-feature model.

**Source 2 — scikit-learn developers.** *Linear Regression Example.* https://scikit-learn.org/stable/auto_examples/linear_model/plot_ols.html

The official example fits ordinary least squares linear regression to the diabetes dataset using a single feature and illustrates predicted versus observed values with evaluation metrics. **Relation to this project:** It provides a reproducible reference workflow for a train/test split, fitting `LinearRegression`, and interpreting regression error. Our project uses a fixed 80/20 split (`random_state=42`) and reports MAE, RMSE, and R², so exact numbers need not match the example.

## 4. Method
1. Load `data/diabetes_bmi.csv` and check the number of observations and columns.
2. Set standardized BMI as `X` and progression score as `y`.
3. Split data into 80% training and 20% testing (`random_state=42`).
4. Fit `sklearn.linear_model.LinearRegression` on the training data.
5. Evaluate held-out predictions with MAE, RMSE, and R²; report the coefficient and intercept.
6. Discuss limitations: one predictor cannot capture the full variation in disease progression; associations are not causal.

## 5. Expected outcome and limitations
The analysis will establish an interpretable baseline and quantify how much prediction error remains when only BMI is used. The dataset is small and the predictor is standardized. It is not suitable for medical decision-making or individual diagnosis. This is a Git/GitHub workflow assignment; the runnable model is included as an optional demonstration.
