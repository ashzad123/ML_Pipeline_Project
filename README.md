# 📚 Student Performance Prediction - ML Pipeline Project

A comprehensive machine learning pipeline that predicts student math scores based on demographic factors and other academic indicators. This project demonstrates end-to-end ML model development from data ingestion to production deployment with a modern Flask web interface.

## 🎯 Overview

The **Student Performance Predictor** uses machine learning to estimate a student's math score based on:
- **Demographics**: Gender, Race/Ethnicity
- **Socioeconomic Factors**: Parental education level, Lunch type
- **Academic Indicators**: Reading score, Writing score, Test preparation course completion

This project demonstrates industry-standard ML practices including data preprocessing, model training, evaluation, and deployment.

## ✨ Features

- **Machine Learning Pipeline**: Full ML workflow from data ingestion to prediction
- **Data Processing**: Automatic handling of categorical and numerical features
- **Model Training**: Multiple model training and hyperparameter tuning
- **Web Interface**: Beautiful, responsive UI for making predictions
- **Error Handling**: Comprehensive logging and custom exception handling
- **Production Ready**: Structured code following best practices
- **Jupyter Notebooks**: Exploratory Data Analysis (EDA) and model training notebooks

## 📁 Project Structure

```
ML_Pipeline_Project/
├── app.py                          # Flask application and route handlers
├── requirements.txt                # Project dependencies
├── setup.py                        # Package installation configuration
├── README.md                       # This file
│
├── src/                            # Source code package
│   ├── __init__.py                # Package initializer
│   ├── exception.py               # Custom exception handling
│   ├── logger.py                  # Logging configuration
│   ├── utils.py                   # Utility functions
│   │
│   ├── components/                # ML Pipeline components
│   │   ├── data_ingestion.py      # Data loading and splitting
│   │   ├── data_transformation.py # Feature engineering and preprocessing
│   │   └── model_trainer.py       # Model training and evaluation
│   │
│   └── pipeline/                  # Prediction pipeline
│       └── predict_pipeline.py    # Inference pipeline and data validation
│
├── notebook/                       # Jupyter notebooks for analysis
│   ├── 1. EDA STUDENT PERFORMANCE.ipynb      # Exploratory Data Analysis
│   ├── 2. MODEL TRAINING.ipynb              # Model development and training
│   └── data/
│       └── stud.csv               # Raw student data
│
├── artifacts/                      # Generated outputs
│   ├── train.csv                  # Training dataset
│   ├── test.csv                   # Testing dataset
│   └── data.csv                   # Full dataset
│
├── templates/                      # Flask HTML templates
│   ├── index.html                 # Results display page
│   └── home.html                  # Prediction form page
│
├── logs/                          # Application logs
└── ML_Pipeline_Project.egg-info/  # Package metadata
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Installation

1. **Clone or navigate to the project directory**:
   ```bash
   cd ML_Pipeline_Project
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   # or
   venv\Scripts\activate     # On Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Usage

### Running the Web Application

Start the Flask development server:

```bash
python app.py
```

The application will be available at:
- Local: `http://127.0.0.1:8080`
- Network: `http://192.168.178.119:8080` (adjust IP as needed)

### Using the Application

1. **Navigate to the home page**: Visit `http://127.0.0.1:8080/`
2. **Start prediction**: Click "Start Prediction" button
3. **Fill the form** with student information:
   - Gender (Male/Female)
   - Race/Ethnicity (Group A-E)
   - Parental Education Level
   - Lunch Type (Standard/Free/Reduced)
   - Test Preparation Course Status
   - Reading Score (0-100)
   - Writing Score (0-100)
4. **Get prediction**: Submit the form to receive the predicted math score
5. **Make another prediction**: Click the button to predict for another student

## 🔄 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Home/Welcome page |
| `/predictdata` | GET | Display prediction form |
| `/predictdata` | POST | Submit form and get prediction |

### Request/Response Example

**Request** (POST `/predictdata`):
```
gender=male
race_ethnicity=group C
parental_level_of_education=bachelor's degree
lunch=standard
test_preparation_course=completed
reading_score=85
writing_score=90
```

**Response**: Displays results page with predicted math score and student information summary

## 📊 Data Pipeline

### 1. Data Ingestion (`components/data_ingestion.py`)
- Loads raw student data from CSV
- Performs train-test split (typically 80-20)
- Saves processed datasets to artifacts folder

### 2. Data Transformation (`components/data_transformation.py`)
- **Numerical Features**: StandardScaler normalization
- **Categorical Features**: One-hot encoding
- **Feature Handling**: Handles missing values and outliers

### 3. Model Training (`components/model_trainer.py`)
- Trains multiple regression models
- Performs hyperparameter tuning
- Evaluates model performance (R² score, MSE, RMSE, MAE)
- Saves best model to disk

### 4. Prediction Pipeline (`pipeline/predict_pipeline.py`)
- Loads trained model and preprocessors
- Validates input data
- Returns predicted math score

## 🤖 Machine Learning Details

### Models Evaluated
- Linear Regression
- Ridge Regression
- Lasso Regression
- ElasticNet
- Random Forest
- Gradient Boosting
- Support Vector Machines
- K-Neighbors Regression
- XGBoost
- CatBoost (if available)

### Feature Engineering
- Categorical encoding for demographic features
- Standardization of numerical features
- Missing value imputation
- Feature scaling for better model performance

### Model Selection
The best performing model is automatically selected based on evaluation metrics and saved for production use.

## 📈 Performance Metrics

The model is evaluated using:
- **R² Score**: Coefficient of determination (model explanatory power)
- **Mean Absolute Error (MAE)**: Average absolute prediction error
- **Mean Squared Error (MSE)**: Penalizes larger errors
- **Root Mean Squared Error (RMSE)**: Interpretable in original units

## 🛠️ Development Workflow

### Running Analysis Notebooks

1. **EDA Notebook**: `notebook/1. EDA STUDENT PERFORMANCE.ipynb`
   - Data exploration and visualization
   - Statistical analysis
   - Feature relationships

2. **Training Notebook**: `notebook/2. MODEL TRAINING.ipynb`
   - Model development
   - Hyperparameter tuning
   - Performance evaluation

### Logging

The application uses custom logging throughout:
- Logs are saved to the `logs/` directory
- Both file and console output
- Tracks data processing and model predictions

### Exception Handling

Custom exceptions are raised for:
- Data validation errors
- Missing required fields
- Model loading failures
- Prediction errors

## 📋 Technologies Used

| Category | Technologies |
|----------|--------------|
| **Backend** | Flask |
| **Data Processing** | Pandas, NumPy |
| **Machine Learning** | Scikit-learn |
| **Advanced ML** | XGBoost, CatBoost (optional) |
| **Visualization** | Matplotlib, Seaborn |
| **Frontend** | HTML5, CSS3 |
| **Logging** | Loguru |

## 🎨 UI Features

- **Modern Design**: Gradient backgrounds and smooth transitions
- **Responsive Layout**: Works on desktop, tablet, and mobile devices
- **Form Validation**: Real-time input validation
- **Results Display**: Clear presentation of predictions and student info
- **Error Handling**: User-friendly error messages

## 🔍 How to Customize

### Add New Features
1. Update `src.pipeline.predict_pipeline.CustomData` class
2. Modify the form in `templates/home.html`
3. Retrain the model with new feature

### Change Model
1. Edit model training in `src.components.model_trainer.py`
2. Retrain using notebook or directly
3. Update model loading in `src.pipeline.predict_pipeline.py`

### Modify UI
1. Edit HTML templates in `templates/` folder
2. Update CSS styles directly in template `<style>` tags
3. Add JavaScript for enhanced interactivity

## 📝 Project Workflow

```
Raw Data
    ↓
Data Ingestion (train-test split)
    ↓
Data Transformation (encoding, scaling)
    ↓
Model Training (multiple models)
    ↓
Model Evaluation (select best)
    ↓
Model Deployment (save artifacts)
    ↓
Prediction Pipeline (inference)
    ↓
Web Interface (user interaction)
```

## 🚨 Troubleshooting

### Common Issues

**Error: "Found unknown categories [None]"**
- Ensure form fields are not empty before submission
- Check field names match between form and Python code

**Error: "Model file not found"**
- Ensure model has been trained using notebooks
- Check artifacts folder contains model files

**Port already in use**
- Change port in `app.py`: `app.run(port=8081)`

**Missing dependencies**
- Run: `pip install -r requirements.txt`

## 📚 Learning Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Scikit-learn Guide](https://scikit-learn.org/stable/documentation.html)
- [Pandas Tutorial](https://pandas.pydata.org/docs/user_guide/index.html)
- [Machine Learning Best Practices](https://www.coursera.org/learn/machine-learning)

## 🤝 Contributing

To contribute to this project:

1. Create a feature branch
2. Make your changes
3. Test thoroughly
4. Submit a pull request with description

## 📄 License

This project is open source and available for educational and research purposes.

## 🎓 Author Notes

This project demonstrates:
- Professional ML pipeline structure
- Production-ready code organization
- End-to-end ML workflow
- Web deployment of ML models
- Industry best practices

Perfect for portfolio, learning, or as a template for similar ML projects.

---

**Last Updated**: January 2026
**Status**: Production Ready ✅