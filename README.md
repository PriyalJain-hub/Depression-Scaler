# Depression-Scaler

## Introduction
When it comes to depression, people tend to avoid talking about their feelings in order to avoid rejection and alienation among peers. In such a situation, many of them seek help from the internet. There aren't many medically reliable websites that allow a user to navigate through their problems related to depression.  
We believe that this project will help address the above-mentioned issue and help increase awareness through a reliable depression scaling system - DASS42 along with Ten Item Personality Inventory- TIPI and background information of users that directly or indirectly have an impact on the mental health of the users.
The raw dataset acquired from Kaggle consists of answers from different participants to a series of questions. This survey can be accessed on openpsychometrics.org.
This project currently focuses on building a model for depression. Hence, the dataset is thoroughly pre- processed and depression dataset is extracted. The level of depression for the dataset is calculated using the DASS-42 scale and an indirect relationship between DAS features and other features of the dataset is formed which then act as one unit to predict the target variable. This paper walks through all stages of implementation in detail. 

## Objectives
•	To secure a reliable dataset to train the machine learning model to take survey questions as input and produce the level of depression as output that is evaluated through psychology standards.
•	 To understand the dataset and proceed with pre-processing of the data. This includes data imputation, feature scaling, dimension reduction, etc. Followed by producing a cleaned dataset for training.
•	To apply various machine learning algorithms to find the best fit model with high accuracy and efficiency.
•	To use the trained model to predict the scale of depression with new input (testing the data).
•	Finally, to create a user interface for the model developed.

## Background Information
Depression and COVID-19:
•	In the first year of the COVID-19 pandemic, global prevalence of anxiety and depression increased by a massive 25%, according to a scientific brief released by the World Health Organization (WHO) today.
•	Despite its high treatment success rate, nearly two out of three people suffering with depression do not actively seek nor receive proper treatment. (DBSA, 1996).
•	Although there are known, effective treatments for mental disorders, more than 75% of people in low- and middle-income countries receive no treatment (WHO).

DASS42:
•	The Depression, Anxiety, and Stress Scales were developed by researchers at the University of New South Wales (Australia). 
•	It is a 42 item self-report scale designed to measure the emotional states of depression, anxiety, and stress.
•	The essential function of the DASS is to assess the severity of the core symptoms of Depression, Anxiety and Stress. 
•	Accordingly, the DASS allows not only a way to measure the severity of a patient’s symptoms but a means by which a patient’s response to treatment can also be measured.
TIPI:
•	The Ten-Item Personality Inventory (TIPI) was developed by Ursula Oberst and Vanessa Renau Ruiz.
•	It is a brief assessment of the Big Five personality dimensions: 
(1) Extraversion, 
(2) Agreeableness, 
(3) Conscientiousness, 
(4) Emotional Stability, and 
(5) Openness to Experience. 
Items are rated on a scale from 1, disagree strongly, to 7, agree strongly.

##Files
1. Results.docx: Contains the inferences and results from EDA to outputs from various algorithms experimented with, and the rationale behind the best-fit model for the project.
2. Colab_Code.docx: Since the original model is too large to upload here, the code to generate the trained machine learning is covered in this document.

##Final Implementation
Web Page implementation (Local tunnel)
About page:
![image](https://github.com/user-attachments/assets/b7f28105-7e3b-45e9-94bb-f88f4c872d8c)
 
Depression Scaler page: Consists of 34 survey questions that user must fill. When predict button is clicked, the level of depression predicted is displayed.
Total question for depression from DASS- 42: 14
TIPI questions: 10
Background information questions: 10
 
 ![image](https://github.com/user-attachments/assets/67ebacc8-8ced-479b-82bb-4881370933fc)
![image](https://github.com/user-attachments/assets/3b7a1399-f130-4c1f-8df1-ee9d7fb3c3e3)
![image](https://github.com/user-attachments/assets/e0ba9a9e-4ba0-4b6e-aea3-e5178f1c1346)
![image](https://github.com/user-attachments/assets/4e06658d-12d4-40c3-9399-6f4e0fa27c87)



   
 

   

