# Gaussian Mixture Model for Traffic Behavior Analysis

## **Overview**
This repository contains the implementation of a **Gaussian Mixture Model (GMM)**-based framework for analyzing and predicting **vehicle lane-change behaviors** using real-world traffic trajectory data. The project integrates **dimensionality reduction (AutoEncoders)**, **data preprocessing**, and **clustering techniques** to study traffic patterns and model complex driving scenarios.

The workflow connects every step, from raw data preprocessing to final clustering visualization, making it easy to follow and understand the implemented techniques.

---

## **Repository Structure**

### **1. Documentation**
- **`/docs`**  
  Contains all project documentation, including:
  - Problem statement
  - Workflow diagrams
  - Methodology details
  - Results and future directions

### **2. Source Code**
- **`/src`**  
  Includes the main implementation files for:
  - **`preprocessing.py`**: Preprocessing raw trajectory data (e.g., flipping two-way data, handling ghost vehicles).  
  - **`autoencoder.py`**: AutoEncoder implementation for dimensionality reduction.  
  - **`gmm_model.py`**: GMM implementation using the Expectation-Maximization (EM) algorithm.  
  - **`visualization.py`**: Visualization scripts for clusters and latent space representations.  

### **3. Data**
- **`/data`**  
  Contains the datasets used for this project (raw and preprocessed).  
  - **Raw Data:** Original trajectory dataset in CSV format.  
  - **Preprocessed Data:** Cleaned and structured datasets for model training.  

### **4. Results**
- **`/results`**  
  Includes the outputs of the model:
  - Clustered results and plots.
  - Visualizations of lane-change behaviors in 2D and latent spaces.
  - Metrics and evaluations.

### **5. Models**
- **`/models`**  
  Saved model files:
  - AutoEncoder weights and configurations.
  - Trained GMM model parameters.

---

## **Setup and Installation**
To run this project locally, follow the steps below:

### **1. Prerequisites**
Ensure you have the following installed:
- Python 3.8+
- Required libraries (listed in `requirements.txt`):
  - NumPy
  - Pandas
  - Matplotlib
  - TensorFlow
  - Scikit-learn
  - Seaborn

### **2. Installation**
Clone this repository and install the required dependencies:
```bash
git clone https://github.com/your-repository-link.git
cd your-repository-name
pip install -r requirements.txt
