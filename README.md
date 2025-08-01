# 🧠 Student Performance Prediction - End-to-End ML Project

This project is an end-to-end machine learning pipeline built to predict student performance using various regression algorithms. It walks through data ingestion, preprocessing, exploratory data analysis (EDA), model training, evaluation, and saving the best model and preprocessor for future use.

---

## 📂 Project Structure

```
End-to-end-ML-project-main/
├── artifacts/
│   ├── data.csv
│   ├── train.csv
│   ├── test.csv
│   ├── model.pkl
│   └── preprocessor.pkl
├── notebook/
│   └── data/
│       └── stud.csv
│   ├── 1. EDA STUDENT PERFORMANCE.ipynb
│   └── 2. MODEL TRAINING.ipynb
├── src/
│   ├── components/
│   ├── pipeline/
│   ├── __init__.py
│   ├── exception.py
│   ├── logger.py
│   └── utils.py
├── .gitignore
├── README.md
├── requirements.txt
└── setup.py
```

---

## 📝 Dataset

- The dataset is stored in `notebook/data/stud.csv`.
- It contains academic, social, and demographic features of students.
- The target variable is **"math_score"**.

---

## 🔍 Project Phases

### 1. Exploratory Data Analysis (EDA)
Performed in `notebook/1. EDA STUDENT PERFORMANCE.ipynb`:
- Missing value treatment
- Feature distributions
- Correlation heatmap
- Outlier inspection
- Initial data insights

### 2. Model Training & Evaluation
Performed in `notebook/2. MODEL TRAINING.ipynb`:
- Data split into train/test
- Categorical feature encoding and numerical scaling using pipelines
- Multiple regression models trained and compared using:
  - R² Score
  - Mean Absolute Error (MAE)
  - Root Mean Squared Error (RMSE)

---

## 🤖 Models Trained and Evaluated

| Model                    | R² Score (Test Set) |
|--------------------------|---------------------|
| Ridge Regression         | 0.8806              |
| Linear Regression        | 0.8803              |
| CatBoosting Regressor    | 0.8516              |
| AdaBoost Regressor       | 0.8498              |
| Random Forest Regressor  | 0.8473              |
| Lasso                    | 0.8253              |
| XGBoost Regressor        | 0.8216              |
| K-Neighbors Regressor    | 0.7838              |
| Decision Tree            | 0.7603              |

✅ **Ridge Regression** had the best performance and was selected for saving and future inference.

---

## 💾 Saved Artifacts

- `artifacts/model.pkl` → Best trained model (Ridge Regression)
- `artifacts/preprocessor.pkl` → Preprocessing pipeline (for consistent input transformation)
- `artifacts/train.csv` and `test.csv` → Split datasets
- `artifacts/data.csv` → Raw merged dataset

---

## 🛠️ How to Run

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/end-to-end-ml-project.git
   cd end-to-end-ml-project
   ```

2. **Create Virtual Environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Notebooks or Python Scripts**
   - For EDA: open and run `notebook/1. EDA STUDENT PERFORMANCE.ipynb`
   - For model training: run `notebook/2. MODEL TRAINING.ipynb`

---

## 📦 Dependencies

Major packages used:
- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `scikit-learn`
- `xgboost`
- `catboost`
- `joblib`

> Full list in `requirements.txt`

---

## 📌 Notes

- This is a beginner-level ML project focused on building a complete ML pipeline.
- You can extend this project by:
  - Turning it into a Flask/Django web app
  - Using advanced hyperparameter tuning (GridSearchCV, Optuna)
  - Deploying the model via Streamlit or FastAPI

---

## 🙌 Acknowledgements

This project is inspired by academic datasets and educational purposes. Built as part of a hands-on machine learning learning journey.
