Titanic Survival Prediction API

A Machine Learning-powered API that predicts whether a passenger would survive the Titanic disaster based on passenger information such as age, gender, and ticket class.

This project is built to help me understand:

Machine Learning fundamentals
Classification and prediction
Data preprocessing
Model training workflows
FastAPI integration with ML models
Real-world ML system architecture
🚀 Project Goal

The goal of this project is not just to train a model, but to understand the complete lifecycle of a Machine Learning system:

Understanding and exploring data
Cleaning and preprocessing datasets
Training a classification model
Evaluating prediction performance
Serving predictions through an API
🧠 What This Project Predicts

Given passenger information such as:

Age
Gender
Passenger class

The model predicts:

Survival outcome
Probability of survival
🛠️ Tech Stack
Python
FastAPI
scikit-learn
Pandas
NumPy
Uvicorn
📂 Project Structure
titanic_project/
│
├── train.csv           # Titanic dataset
├── train_model.py      # Model training logic
├── model.pkl           # Saved trained model
├── main.py             # FastAPI application
├── requirements.txt
└── README.md
⚙️ How the System Works
1. Dataset

The Titanic dataset is used to train the model on historical passenger data.

2. Training Phase

The model learns patterns from passenger information and survival outcomes.

3. Model Saving

After training, the trained model is saved for reuse.

4. API Phase

FastAPI loads the trained model and exposes prediction endpoints.

🔍 Machine Learning Concepts Practiced

This project focuses on understanding:

Binary Classification
Features and Labels
Data Cleaning
Encoding Categorical Variables
Model Training
Prediction Probabilities
Accuracy Evaluation
Model Serialization
📡 API Endpoint
Predict Survival
POST /predict
Example Request
{
  "age": 22,
  "sex": "female",
  "pclass": 1
}
Example Response
{
  "survived": true,
  "probability": 0.87
}
📚 Learning Objectives

Through this project, I aim to improve my understanding of:

How Machine Learning models make predictions
How APIs interact with ML systems
Structuring backend ML applications
Building production-style ML services
📈 Future Improvements
Add more passenger features
Improve model accuracy
Add model evaluation metrics
Dockerize the application
Deploy the API
Add authentication
Store prediction logs in a database
📖 Dataset Source

Titanic Dataset from Kaggle:

Titanic - Machine Learning from Disaster

🤝 Acknowledgment

This project is part of my journey into Machine Learning engineering, backend development, and building intelligent systems.
