import streamlit as st
import numpy as np
import pickle
import os
class NeuralNetwork:
    def __init__ (self,
                  input_size,
                  hidden_size,
                  output_size,
                  learning_rate=0.01,
                  epochs=100):
        self.input_size=input_size
        self.hidden_size=hidden_size
        self.output_size=output_size
        self.learning_rate=learning_rate
        self.epochs=epochs

        self.W1=np.random.randn(self.input_size,self.hidden_size)*0.01
        self.b1=np.zeros((1,self.hidden_size))
        self.W2=np.random.randn(self.hidden_size,self.output_size)*0.01
        self.b2=np.zeros((1,self.output_size))

        self.loss_history=[]
        self.accuracy_history=[]
    def relu(self,z):
        return np.maximum(0,z)
    def relu_derivative(self,z):
        return np.where(z>0,1,0)
    def softmax(self,z):
        exp_values=np.exp(z-np.max(z,axis=1,keepdims=True))
        return exp_values/np.sum(exp_values,axis=1,keepdims=True)
    def forward(self,X):
        self.z1=np.dot(X,self.W1)+self.b1
        self.a1=self.relu(self.z1)
        self.z2=np.dot(self.a1,self.W2)+self.b2
        self.probs=self.softmax(self.z2)
        return self.probs
    def compute_loss(self,y_true,probs):
        loss=-np.mean(np.sum(y_true*np.log(probs),axis=1))
        return loss
    def compute_accuracy(self,y_true,probs):
        predictions=np.argmax(probs,axis=1)
        true_labels=np.argmax(y_true,axis=1)
        return np.mean(predictions==true_labels)
    def backward(self,X,y):
        m=X.shape[0]
        delta3=self.probs-y
        dW2=np.dot(self.a1.T,delta3)/m
        db2=np.sum(delta3,axis=0,keepdims=True)/m
        delta2=np.dot(delta3,self.W2.T)*self.relu_derivative(self.z1)
        dW1=np.dot(X.T,delta2)/m
        db1=np.sum(delta2,axis=0,keepdims=True)/m
        
        self.W2-=self.learning_rate*dW2
        self.W1-=self.learning_rate*dW1
        self.b2-=self.learning_rate*db2
        self.b1-=self.learning_rate*db1
    def train(self,X,y):
        for epoch in range(self.epochs):
            probs=self.forward(X)
            loss=self.compute_loss(y,probs)
            accuracy=self.compute_accuracy(y,probs)
            self.loss_history.append(loss)
            self.accuracy_history.append(accuracy)

            self.backward(X,y)
            if epoch%10==0:
              print(f"Training metrics : Epoch: {epoch},loss: {loss:.4f},accuracy: {accuracy:.4f}")
model_path=os.path.join('..','Model','iris_mlp.pkl')
with open (model_path,'rb') as file:
    model=pickle.load(file)

st.title("Iris Flower Prediction App")

sepal_length = st.number_input("Sepal Length")
sepal_width = st.number_input("Sepal Width")
petal_length = st.number_input("Petal Length")
petal_width = st.number_input("Petal Width")

if st.button("Predict"):

    sample = np.array([
        [
            sepal_length,
            sepal_width,
            petal_length,
            petal_width
        ]
    ])

    probs = model.forward(sample)

    prediction = np.argmax(probs, axis=1)[0]

    species = [
        "Setosa",
        "Versicolor",
        "Virginica"
    ]

    st.success(
        f"Prediction: {species[prediction]}"
    )

