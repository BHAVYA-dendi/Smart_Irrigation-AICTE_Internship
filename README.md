# Smart/Automated Irrigation using Soil Moisture and Weather Data

This project is developed as part of the **AICTE Internship Program**.  
It uses machine learning to predict the ON/OFF status of sprinklers based on **20 soil moisture and weather sensor inputs**.

## 🌱 Objective

To automate irrigation by predicting sprinkler status using AI, optimizing water usage and supporting precision farming.

## 📂 Files Included

- `Farm_Irrigation_System.pkl` – Trained machine learning model  
- `Smart_Irrigation1.ipynb` – Jupyter notebook for model training  
- `irrigation_machine.csv` – Dataset used for training  
- `app.py` – Streamlit web app for sprinkler prediction  
- `README.md` – Project documentation

## 🛠️ Tools & Technologies Used

- **Language**: Python  
- **Platform**: Google Colab, VS Code  
- **Environment**: Jupyter Notebook, Streamlit  
- **Libraries**: scikit-learn, pandas, numpy, joblib, streamlit  
- **Interface**: Streamlit Web App  
- **Model**: Random Forest Classifier  
 **Dataset**: Custom/generated soil moisture and weather data  
- **Version Control**: Git & GitHub

## ⚙️ Methodology

- **Data Collection**: Sensor data with 20 input features.
- **Preprocessing**: Scaling inputs between 0 and 1.
- **Model Training**: Random Forest Classifier to predict 3 sprinkler statuses.
- **Model Deployment**: Exported using `joblib` and integrated into a Streamlit app.
- **User Interaction**: Web sliders allow manual input of sensor values for real-time prediction.

## 🚀 How to Run

1. Clone this repo or download the files.
2. Ensure `Farm_Irrigation_System.pkl` and `app.py` are in the same folder.
3. Open terminal and run:
   ```bash
   streamlit run app.py
4. Enter sensor valuesvand click Predict Sprinklers

## 💧 Sample Output

Sprinkler 0: ON 
Sprinkler 1: OFF 
Sprinkler 2: ON

## 👩‍💻 Developed By

**Dendi Bhavya Reddy**  
For **AICTE Internship Project**
