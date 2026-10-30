# Dataset provenance

**Source:** scikit-learn diabetes dataset (`sklearn.datasets.load_diabetes`), bundled with scikit-learn.

**Official documentation:** https://scikit-learn.org/stable/datasets/toy_dataset.html#diabetes-dataset

**Loading API:** https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html

**Original dataset context:** Efron, Hastie, Johnstone, and Tibshirani (2004), *Least Angle Regression*, *Annals of Statistics*, 32(2), 407–499. https://doi.org/10.1214/009053604000000067

This file is a two-column extraction of the bundled dataset: standardized baseline BMI (`data[:, 2]`) and quantitative disease progression (`target`), 442 rows. BMI is standardized and must not be interpreted as raw kg/m². The target is a quantitative progression score, not a diagnosis or individual clinical prediction.

To recreate: `load_diabetes()` then export `data[:, 2]` and `target`.
