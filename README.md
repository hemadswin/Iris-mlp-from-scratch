# Iris Flower Classification using MLP Neural Network from Scratch

![Python](https://img.shields.io/badge/Python-3.12-blue)
![NumPy](https://img.shields.io/badge/NumPy-Neural%20Network-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)

## Live Demo

**Streamlit Application:**
https://iris-mlp-from-scratch-svssxtzvu88thyrxjxcwsm.streamlit.app/

---

## Project Overview

This project implements a **Multi-Layer Perceptron (MLP) Neural Network from Scratch using NumPy** without relying on deep learning frameworks such as TensorFlow or PyTorch.

The model is trained on the famous **Iris Dataset** and deployed using **Streamlit** to provide an interactive web application for flower species prediction.

### Key Highlights

* Built an MLP Neural Network completely from scratch using NumPy
* Implemented Forward Propagation manually
* Implemented Backpropagation manually
* Applied Gradient Descent optimization
* Used ReLU and Softmax activation functions
* Achieved **98.3% Training Accuracy**
* Achieved **96.7% Test Accuracy**
* Deployed as a Streamlit web application

---

## Dataset

The project uses the Iris Dataset available in Scikit-Learn.

### Input Features

* Sepal Length
* Sepal Width
* Petal Length
* Petal Width

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

## Results

* Training Accuracy: 98.3%
* Test Accuracy: 96.7%
* Successfully implemented a Multi-Layer Perceptron (MLP) from scratch
* Performed multi-class classification on the Iris Dataset
* Built and deployed an interactive Streamlit application

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

### Run Streamlit Application

```bash
streamlit run SRC/app.py
```

---

## Project Structure

```text
IRIS_MLP_APP/

├── Images/
│   ├── training_metrics.png
│   └── Iris_App.png
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
├── README.md
└── .gitignore
```

---

## Learning Outcomes

Through this project, I gained hands-on experience with:

* Neural Network Fundamentals
* Forward Propagation
* Backpropagation
* Gradient Descent Optimization
* Matrix Operations using NumPy
* Model Serialization using Pickle
* Streamlit Deployment
* Git & GitHub Workflow

---

## Future Improvements

* Add Multiple Hidden Layers
* Implement Dropout Regularization
* Add Advanced Evaluation Metrics
* Improve UI/UX Design
* Compare Performance with TensorFlow and PyTorch Implementations

---

## Author

**N Hema Sathya Kumari**

Aspiring Data Scientist | Machine Learning Enthusiast

GitHub: https://github.com/hemadswin

LinkedIn: https://www.linkedin.com/in/n-hema/

---

## License

This project is open for educational and portfolio purposes.
