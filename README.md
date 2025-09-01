# 🏦 Loan Approval Prediction System

An end-to-end **Data Engineering & Machine Learning Project** that predicts whether a loan application will be **Approved** or **Rejected**.  
This project covers the full pipeline: **Data Engineering → Model Training → Deployment with Streamlit**.

---

## 🚀 Project Workflow

1. **Data Engineering**
   - Loaded JSON datasets (`applicant_info.json`, `financial_info.json`, `loan_info.json`) into a MySQL database (`loan_db`).
   - Designed relational tables and stored structured data for analysis.

2. **Data Preprocessing**
   - Retrieved data into Pandas DataFrames.
   - Merged datasets on `Applicant_ID`.
   - Handled missing values:
     - Used median for numerical features like `LoanAmount`.
     - Filled defaults for categorical values (`Married=No`, etc.).
   - Encoded categorical variables (`Gender`, `Education`, `Property_Area`, etc.).
   - Scaled numerical features where necessary.
   - Split dataset into Train/Test.

3. **Model Training**
   - Trained a `RandomForestClassifier` for loan approval prediction.
   - Evaluated with Accuracy, Precision, Recall, and F1-score.
   - Saved trained model as **`model.pkl`** using `pickle`.

4. **Deployment with Streamlit**
   - Built an interactive **Streamlit App** (`app.py`) for real-time predictions.
   - Users input loan details → App preprocesses data → Model predicts `Approved` ✅ or `Rejected` ❌.

---

## 📂 Project Structure

```
.
├── applicant_info.json         # Applicant demographics
├── financial_info.json         # Financial details
├── loan_info.json              # Loan details
├── LoanPrediction_ML_Model.ipynb # Model training notebook
├── model.pkl                   # Trained RandomForest model
├── app.py                      # Streamlit application
├── Requirements.txt            # Dependencies
└── README.md                   # Project documentation
```

---

## ⚙️ Installation & Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/loan-prediction-app.git
   cd loan-prediction-app
   ```

2. Install dependencies:
   ```bash
   pip install -r Requirements.txt
   ```

3. Run Streamlit App:
   ```bash
   streamlit run app.py
   ```

---

## 🌐 Deployment

This project can be deployed using **Streamlit Cloud**:
1. Push code to GitHub.
2. Go to [Streamlit Cloud](https://streamlit.io/cloud).
3. Connect your repo and deploy.
4. The app will be accessible via a public URL.

---

## 📊 Example Prediction

- **Input**:  
  - Gender: Male  
  - Married: Yes  
  - Income: 5000  
  - Loan Amount: 150  
  - Credit History: 1  
  - Property Area: Urban  

- **Output**:  
  ✅ Loan Approved!

---

## 🛠️ Tech Stack

- **Python** (pandas, numpy, scikit-learn, pickle)
- **MySQL** (data storage & retrieval)
- **Streamlit** (app deployment)
- **Machine Learning** (RandomForestClassifier)

---

## 📌 Future Improvements
- Add more ML algorithms (XGBoost, Logistic Regression).
- Build API endpoints for model inference.
- Deploy with Docker + AWS/GCP for scalability.

---

## 👨‍💻 Author
**Srinivasan Sriram Tirunelvelli**  
💡 Passionate about Data Engineering, ML, and End-to-End AI solutions.
