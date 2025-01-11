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

### ** Prerequisites**
Ensure you have the following installed:
- Python 3.8+
- Required libraries (listed in `requirements.txt`):
  - NumPy
  - Pandas
  - Matplotlib
  - TensorFlow
  - Scikit-learn
  - Seaborn


## **Workflow**
The following steps outline the workflow of this project:

### **1. Data Preprocessing:**
   - **Flipping backward-moving vehicles** for consistency across the two-way highway data.
   - **Creating a matrix** for the ego vehicle and its surrounding vehicles (up to 8).
   - **Handling missing values** with ghost vehicles, assigning default values (e.g., `-1` for positions, `0` for velocities).

### **2. Dimensionality Reduction:**
   - **Applied AutoEncoders** to reduce high-dimensional traffic data into a latent space representation, retaining critical features for clustering.

### **3. Clustering with GMM:**
   - **Modeled clusters** for lane-change behaviors using the **Expectation-Maximization (EM)** algorithm.
   - **Handled covariance matrix issues** with regularization techniques, ensuring stability during GMM iterations.

### **4. Visualization:**
   - **Visualized clusters** and latent space projections for interpretability, enabling the understanding of vehicle behaviors (left, straight, right lane changes).

---

## **Results**
The GMM successfully clustered vehicle trajectories into three meaningful categories:
1. **Left Lane Changes**  
2. **Right Lane Changes**  
3. **Straight Driving**

### **Key Highlights:**
- **Addressed singular covariance matrices** with regularization techniques, preventing errors during model iterations.
- **Dimensionality reduction** significantly improved the GMM’s clustering accuracy, reducing overfitting.
- **Meaningful 2D visualizations** provided an intuitive understanding of lane-change patterns.

---

## **Future Directions**
- **Extend the model** to handle temporal dependencies for dynamic traffic predictions and better understanding of lane-change behaviors over time.
- **Integrate external factors** such as **weather** and **traffic density** for improved robustness in traffic prediction.
- **Adapt the framework** for **real-time traffic modeling** in autonomous driving systems, allowing for predictive decision-making and safer vehicle behavior analysis.

---
