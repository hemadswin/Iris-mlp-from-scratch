# Iris Flower Classification using MLP Neural Network from Scratch

![Python](https://img.shields.io/badge/Python-3.12-blue)
![NumPy](https://img.shields.io/badge/NumPy-Neural%20Network-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)

## Project Overview

This project implements a **Multi-Layer Perceptron (MLP) Neural Network from Scratch using NumPy** without using deep learning frameworks such as TensorFlow or PyTorch.

The model is trained on the famous **Iris Dataset** and deployed using **Streamlit** to provide an interactive web application for flower species prediction.

The goal of this project was to understand the complete working of neural networks by manually implementing:

* Forward Propagation
* Backpropagation
* Gradient Descent
* ReLU Activation
* Softmax Activation
* Cross Entropy Loss

---

## Features

* Built MLP Neural Network completely from scratch using NumPy
* Manual implementation of Forward Propagation
* Manual implementation of Backpropagation
* ReLU Activation Function
* Softmax Output Layer
* Cross Entropy Loss Function
* Gradient Descent Optimization
* Training and Accuracy Visualization
* Model Serialization using Pickle
* Interactive Streamlit Web Application

---

## Dataset

The project uses the Iris Dataset available in Scikit-Learn.

### Input Features

1. Sepal Length
2. Sepal Width
3. Petal Length
4. Petal Width

### Target Classes

* Setosa
* Versicolor
* Virginica

---

## Neural Network Architecture

### Input Layer

* 4 Neurons

### Hidden Layer

* 8 Neurons
* ReLU Activation

### Output Layer

* 3 Neurons
* Softmax Activation

### Training Configuration

* Learning Rate: 0.04
* Epochs: 500
* Loss Function: Cross Entropy Loss
* Optimizer: Gradient Descent

---

## Technologies Used

* Python
* NumPy
* Matplotlib
* Scikit-Learn
* Streamlit
* Pickle

---

## Project Structure

```text
IRIS_MLP_APP/

├── Data/
│
├── Images/
│   ├── training_metrics.png
│   └── app_screenshot.png
│
├── Model/
│   └── iris_mlp.pkl
│
├── Notebooks/
│   └── MLP_Neural_Network.ipynb
│
├── SRC/
│   └── app.py
│
├── requirements.txt
│
├── README.md
│
└── .gitignore
```

---

## Training Process

The neural network follows the standard deep learning workflow:

1. Initialize Weights and Biases
2. Forward Propagation
3. Compute Loss
4. Backpropagation
5. Calculate Gradients
6. Update Parameters
7. Repeat for Multiple Epochs
8. Save Trained Model using Pickle

---


## Results

## Results

- Training Accuracy: 98.3%
- Test Accuracy: 96.7%
- Successfully implemented a Multi-Layer Perceptron (MLP) from scratch using NumPy
- Performed multi-class classification on the Iris Dataset
- Built an interactive prediction application using Streamlit

---


## Training Metrics

![Training Metrics](Images/training_metrics.png)

---


## Application Preview

![Application Screenshot](Images/Iris_App.png)


---

## Run Locally

### Clone Repository

```bash
git clone https://github.com/hemadswin/iris-mlp-from-scratch.git
```

### Navigate to Project Folder

```bash
cd iris-mlp-from-scratch
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Navigate to Source Folder

```bash
cd SRC
```

### Run Streamlit Application

```bash
streamlit run app.py
```

---

## Learning Outcomes

Through this project, I gained hands-on experience with:

* Neural Network Fundamentals
* Matrix Operations using NumPy
* Forward Propagation
* Backpropagation
* Gradient Descent Optimization
* Model Serialization
* Streamlit Deployment
* Git & GitHub Project Management

---

## Future Improvements

* Add Multiple Hidden Layers
* Implement Dropout Regularization
* Add Model Evaluation Metrics
* Deploy Application on Streamlit Cloud
* Improve UI/UX Design
* Compare Performance with TensorFlow and PyTorch Models

---

## Author

N Hema Sathya Kumari

Aspiring Data Scientist | Machine Learning Enthusiast

GitHub: [hemadswin](https://github.com/hemadswin)

LinkedIn: [N Hema Sathya Kumari](https://www.linkedin.com/in/n-hema/)


---


## License

This project is open for educational and learning purposes.


