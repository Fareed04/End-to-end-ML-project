# 📊 Student Performance Indicator – End-to-End ML Project

This is an end-to-end machine learning project focused on analyzing and predicting student academic performance. It simulates a real-world ML workflow using Python and Scikit-learn from raw data ingestion to model training and evaluation in a production-ready pipeline.

---

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Enabled-orange)
![MIT License](https://img.shields.io/badge/License-MIT-green)

---

## 🧠 Project Overview

This project tackles a regression problem to predict students' final grades based on features like study time, past failures, and parental education.

It includes:

- Clean and modular Python codebase
- Componentized structure for easy maintenance
- Metrics comparison for model evaluation
- Serialized model output (`.pkl`)
- CI-ready structure with GitHub Actions

---

## 📂 Folder Structure

```
📁 StudentPerformanceML/
│
├── artifacts/                        # Intermediate files: data, models
│   ├── data.csv
│   └── model.pkl
│
├── notebooks/
│   └── student-performance.ipynb     # Data exploration notebook
│
├── src/
│   ├── components/                   # ML components (data ingestion, transformation, training)
│   ├── pipelines/                    # Training pipeline
│   ├── utils.py                      # Reusable utility functions
│   ├── logger.py, exception.py       # Logging & error handling
│
├── app.py                            # Script to trigger training pipeline
├── setup.py                          # Package setup
├── requirements.txt                  # Python dependencies
└── README.md
```

---

## ⚙️ Workflow Breakdown

### 1. Data Ingestion
- Reads data from CSV and saves it to an artifact folder.
- Splits the data into training and testing sets.

### 2. Data Transformation
- Handles missing values.
- Encodes categorical features.
- Scales features with `StandardScaler`.

### 3. Model Training
- Uses multiple regression models: `LinearRegression`, `RandomForestRegressor`.
- Selects the best-performing model based on R² score.
- Saves the final model to `model.pkl`.

### 4. Evaluation
- Compares models using MAE, MSE, and R².

---

## ✅ Model Metrics

| Model               | MAE   | MSE   | R² Score |
|--------------------|-------|-------|----------|
| Linear Regression   | 1.89  | 5.23  | 0.78     |
| Random Forest       | 1.23  | 3.45  | 0.89 ✅   |

**🎯 Best Model:** Random Forest Regressor

---

## 📈 Key Findings

- **Top Predictive Features:**  
  - Study time  
  - Number of past failures  
  - Parental education  
- Random Forest consistently outperforms linear models in this context.

---

## 🧰 Tech Stack

- **Language:** Python 3.10+
- **Libraries:** Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn
- **Tools:** Jupyter, VS Code, Git/GitHub

---

## 🚀 How to Run Locally

```bash
# Clone repo
git clone https://github.com/yourusername/StudentPerformanceML.git
cd StudentPerformanceML

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the pipeline
python app.py
```

---

## 🎯 Future Enhancements

- Integrate Streamlit/Flask for a web-based frontend
- Add MLflow for experiment tracking
- Deploy with Docker for production readiness
- Implement feature selection and hyperparameter tuning

---

## 🤝 Contributing

Contributions, issues and feature requests are welcome!

To contribute:

1. Fork the repo
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes
4. Push to the branch (`git push origin feature-branch`)
5. Open a pull request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

