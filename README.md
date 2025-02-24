# Kidney_disease_classifier

export MLFLOW_TRACKING_URI=https://dagshub.com/LearningBoy2002/Kidney_disease_classifier.mlflow 
export MLFLOW_TRACKING_USERNAME=LearningBoy2002 
export MLFLOW_TRACKING_PASSWORD=
python script.py


save the URI : 905418434851.dkr.ecr.eu-north-1.amazonaws.com/kidney_classifier

# Kidney Disease Classifier

## Overview
This repository contains a deep learning project that classifies kidney images using a VGG16 model. It follows a full machine learning pipeline and leverages **DVC** (Data Version Control) and **Dagshub's MLflow** to monitor the training process, ensuring reproducibility and efficiency. The project has been dockerized and was temporarily deployed on **AWS EC2**. However, since this was a personal project, the deployment was not permanent due to AWS Free Tier limitations.

## Features
- **Deep Learning Model:** Utilizes **VGG16** for kidney disease classification.
- **Full Pipeline Implementation:** Includes data preprocessing, training, and evaluation.
- **DVC & MLflow Integration:** Tracks and monitors experiments effectively.
- **Dockerized:** Ensures environment consistency.
- **AWS Deployment:** Temporarily deployed on an EC2 instance.

## Project Structure
```
Kidney_disease_classifier/
├── app.py              # Main application file
├── config/             # Configuration files
├── data/               # Dataset directory
├── docker/             # Docker-related files
├── models/             # Trained models
├── notebooks/          # Jupyter notebooks for EDA and training
├── src/                # Source code for training and inference
├── dvc.yaml            # DVC pipeline configuration
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

## How to Run?
### Steps to Set Up
1. **Clone the repository:**
   ```sh
   git clone https://github.com/LearningBoy2002/Kidney_disease_classifier.git
   cd Kidney_disease_classifier
   ```
2. **Create a Conda environment:**
   ```sh
   conda create -n cnncls python=3.8 -y
   conda activate cnncls
   ```
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Run the application:**
   ```sh
   python app.py
   ```
5. **Open the local host and port in your browser.**

### DVC Commands
```sh
   dvc init
   dvc repro
   dvc dag
```

## MLflow & DVC
### MLflow
- **Production-grade experiment tracking**
- **Trace all model training experiments**
- **Logging & tagging models for version control**

### DVC
- **Lightweight and efficient for Proof of Concept (POC)**
- **Tracks lightweight experiments**
- **Performs orchestration (creating pipelines)**

## AWS Deployment (CI/CD with GitHub Actions)
### Steps to Deploy on AWS
1. **Login to AWS Console.**
2. **Create an IAM user for deployment** with specific access:
   - **EC2 Access:** To launch and manage a virtual machine.
   - **ECR Access:** To store Docker images in AWS Elastic Container Registry.

### Deployment Process
1. **Build a Docker image of the source code.**
2. **Push the Docker image to ECR.**
3. **Launch an EC2 instance.**
4. **Pull the Docker image from ECR on EC2.**
5. **Run the Docker image in EC2.**

### Required IAM Policies
- **AmazonEC2ContainerRegistryFullAccess**
- **AmazonEC2FullAccess**

## Notes
- This project was deployed **temporarily** on AWS EC2 as it was a personal project.
- The **AWS Free Tier** has limitations, so the deployment was not permanent.





