# Data Explorer
![DATA](https://user-images.githubusercontent.com/95062628/187087508-4a16a57e-bf16-4d16-9c84-3e7fbf75e0f7.jpg)

# Demo
<a href="https://drive.google.com/file/d/1jB2iTbMt5GOz0wvp4OUbyI_VyD0emFIo/view?usp=sharing"> Demo </a>
Launch the web app:

[![Streamlit App]

# Analysis and Pandas Profiling
The various functions lets us undertstand the data, it's `datatypes` and  describe the features. We can get basic details about data as well as advanced `descriptive statistcs`. We can check if any `null values` are present, if yes we have the functionality to `fill` them using appropriate logic. Another automation method lets us check for `duplicates` and lets us `remove` them if desired.`pandas-profiling` generates profile reports from a pandas `DataFrame`. `pandas-profiling` extends pandas `DataFrame` with `df.profile_report()`, which automatically generates a standardized univariate and multivariate report for data understanding. We are proviede with an option to `download` the pandas `profile report`.

For each column, the following information (whenever relevant for the column type) is presented in an interactive HTML report:

- **Type inference**: detect the types of columns in a DataFrame
- **Essentials**: type, unique values, indication of missing values
- **Quantile statistics**: minimum value, Q1, median, Q3, maximum, range, interquartile range
- **Descriptive statistics**: mean, mode, standard deviation, sum, median absolute deviation, coefficient of variation, kurtosis, skewness
- **Most frequent and extreme values**
- **Histograms**: categorical and numerical
- **Correlations**: high correlation warnings, based on different correlation metrics (Spearman, Pearson, Kendall, Cramér’s V, Phik)
- **Missing values**: through counts, matrix, heatmap and dendrograms
- **Duplicate rows**: list of the most common duplicated rows
- **Text analysis**: most common categories (uppercase, lowercase, separator), scripts (Latin, Cyrillic) and blocks (ASCII, Cyrilic)
- **File and Image analysis**: file sizes, creation dates, dimensions, indication of truncated images and existance of EXIF metadata

# Reproducing this web app
To recreate this web app on your own computer, do the following.

### Create conda environment
Firstly, we will create a conda environment called *dex*
```
conda create -n dex python=3.7.9
```
Secondly, we will login to the *eda* environment
```
conda activate dex
```
### Install prerequisite libraries

Download requirements.txt file

```
wget https://raw.githubusercontent.com/gmayuriiii/data-explorer/main/requirements.txt

```

Pip install libraries
```
pip install -r requirements.txt
```

###  Download and unzip contents from GitHub repo

Download and unzip contents from 

###  Launch the app

```
streamlit run dataexplorer.py
```
