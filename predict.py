import numpy as np
import streamlit as st 
import pandas as pd
import pickle

def load_model():
    with open('saved_model.pkl','rb') as file:
        data=pickle.load(file)
    return data

data=load_model()

model=data["model"]
labels=data["labels"]

def show_prediction():
    st.title('Depression Scaler')
    st.subheader('Scaler Questions')

    Q1 =  st.selectbox("I couldn't seem to experience any positive feeling at all",["Did not apply to me at all", "Applied to me to some degree, or some of the time", "Applied to me to a considerable degree, or a good part of the time", "Applied to me very much, or most of the time"])

    Q2 = st.selectbox("I just couldn't seem to get going",["Did not apply to me at all", "Applied to me to some degree, or some of the time", "Applied to me to a considerable degree, or a good part of the time", "Applied to me very much, or most of the time"])

    Q3 = st.selectbox("I felt that I had nothing to look forward to",["Did not apply to me at all", "Applied to me to some degree, or some of the time", "Applied to me to a considerable degree, or a good part of the time", "Applied to me very much, or most of the time"])

    Q4 = st.selectbox("I felt sad and depressed",["Did not apply to me at all", "Applied to me to some degree, or some of the time", "Applied to me to a considerable degree, or a good part of the time", "Applied to me very much, or most of the time"])

    Q5 = st.selectbox("I felt that I had lost interest in just about everything",["Did not apply to me at all", "Applied to me to some degree, or some of the time", "Applied to me to a considerable degree, or a good part of the time", "Applied to me very much, or most of the time"])

    Q6 = st.selectbox("I felt I wasn't worth much as a person",["Did not apply to me at all", "Applied to me to some degree, or some of the time", "Applied to me to a considerable degree, or a good part of the time", "Applied to me very much, or most of the time"])

    Q7 = st.selectbox("I felt that life wasn't worthwhile",["Did not apply to me at all", "Applied to me to some degree, or some of the time", "Applied to me to a considerable degree, or a good part of the time", "Applied to me very much, or most of the time"])

    Q8 = st.selectbox("I couldn't seem to get any enjoyment out of the things I did",["Did not apply to me at all", "Applied to me to some degree, or some of the time", "Applied to me to a considerable degree, or a good part of the time", "Applied to me very much, or most of the time"])

    Q9 = st.selectbox("I felt down-hearted and blue",["Did not apply to me at all", "Applied to me to some degree, or some of the time", "Applied to me to a considerable degree, or a good part of the time", "Applied to me very much, or most of the time"])

    Q10 = st.selectbox("I was unable to become enthusiastic about anything",["Did not apply to me at all", "Applied to me to some degree, or some of the time", "Applied to me to a considerable degree, or a good part of the time", "Applied to me very much, or most of the time"])

    Q11 = st.selectbox("I felt I was pretty worthless",["Did not apply to me at all", "Applied to me to some degree, or some of the time", "Applied to me to a considerable degree, or a good part of the time", "Applied to me very much, or most of the time"])

    Q12 = st.selectbox("I could see nothing in the future to be hopeful about",["Did not apply to me at all", "Applied to me to some degree, or some of the time", "Applied to me to a considerable degree, or a good part of the time", "Applied to me very much, or most of the time"])

    Q13 = st.selectbox("I felt that life was meaningless",["Did not apply to me at all", "Applied to me to some degree, or some of the time", "Applied to me to a considerable degree, or a good part of the time", "Applied to me very much, or most of the time"])

    Q14 = st.selectbox("I found it difficult to work up the initiative to do things",["Did not apply to me at all", "Applied to me to some degree, or some of the time", "Applied to me to a considerable degree, or a good part of the time", "Applied to me very much, or most of the time"])

    st.subheader('10 Personality Questions')

    TIP1 = st.selectbox("I see myself as extraverted and enthusiastic",["Disagree strongly", "Disagree moderately", "Disagree a little", "Neither agree nor disagree", "Agree a little", "Agree moderately", "Agree strongly"])

    TIP2 = st.selectbox("I see myself as critical and quarrelsome",["Disagree strongly","Disagree moderately","Disagree a little","Neither agree nor disagree","Agree a little","Agree moderately","Agree strongly"])

    TIP3 = st.selectbox("I see myself as dependable and self- disciplined",["Disagree strongly","Disagree moderately","Disagree a little","Neither agree nor disagree","Agree a little","Agree moderately","Agree strongly"])

    TIP4 = st.selectbox("I get anxious and easily upset",["Disagree strongly","Disagree moderately","Disagree a little","Neither agree nor disagree","Agree a little","Agree moderately","Agree strongly"])

    TIP5 = st.selectbox("I am open to new experiences, complex",["Disagree strongly","Disagree moderately","Disagree a little","Neither agree nor disagree","Agree a little","Agree moderately","Agree strongly"])

    TIP6 = st.selectbox("I see myself as reserved and quiet",["Disagree strongly","Disagree moderately","Disagree a little","Neither agree nor disagree","Agree a little","Agree moderately","Agree strongly"])

    TIP7 = st.selectbox("I see myself as sympathetic and warm",["Disagree strongly","Disagree moderately","Disagree a little","Neither agree nor disagree","Agree a little","Agree moderately","Agree strongly"])

    TIP8 = st.selectbox("I see myself as disorganized and careless",["Disagree strongly","Disagree moderately","Disagree a little","Neither agree nor disagree","Agree a little","Agree moderately","Agree strongly"])

    TIP9 = st.selectbox("I see myself as calm and emotionally stable",["Disagree strongly","Disagree moderately","Disagree a little","Neither agree nor disagree","Agree a little","Agree moderately","Agree strongly"])

    TIP10 = st.selectbox("I see myself as conventional and uncreative",["Disagree strongly","Disagree moderately","Disagree a little","Neither agree nor disagree","Agree a little","Agree moderately","Agree strongly"])

    st.subheader('Extra information')

    Education = st.selectbox("How much education have you completed?", ["Less than high school","High school","University degree","Graduate degree"])

    Urban = st.selectbox("What type of area did you live when you were a child?", ["Rural","Suburban","Urban"])

    Gender = st.selectbox("What is your gender?", ["Male","Female","Other"])

    Religion = st.selectbox("What is your religion?", ["Agnostic","Atheist","Buddhist","Christian (Catholic)","Christian (Mormon)","Christian (Protestant)","Christian (Other)","Hindu","Jewish","Muslim","Sikh","Other"])

    Orientation = st.selectbox("What is your sexual orientation?", ["Heterosexual","Bisexual","Homosexual","Asexual","Other"])

    Race = st.selectbox("What is your race?", ["Asian","Arab","Black","Indigenous Australian","Native American","White","Other"])

    Voted = st.selectbox("Have you voted in the national elections in the past year?", ["Yes","No"])

    Married = st.selectbox("What is your marital status?", ["Never married","Currently married","Previously married"])

    Family = st.number_input("Including you, how many children did your mother have?", min_value=1, max_value=13)

    AgeGroup = st.selectbox("Which age class do you belong to?", ["Under 10","Primary Children","Secondary Children","Adults","Elder Adults","Older People"])
    
    # st.markdown('##')
    ok=st.button('Predict')
    # st.markdown('##')
    
    if ok:
        def qoptions(value):
            if value =='Did not apply to me at all':
                return 0
            if  value=='Applied to me to some degree, or some of the time':
                return 1
            if value=='Applied to me to a considerable degree, or a good part of the time':
                return 2
            if value=='Applied to me very much, or most of the time':
                return 3

        def tipoptions(value):
            if value =='Disagree strongly':
                return 1
            if  value=='Disagree moderately':
                return 2
            if value=='Disagree a little':
                return 3
            if value=='Neither agree nor disagree':
                return 4
            if value=='Agree a little':
                return 5
            if value=='Agree moderately':
                return 6
            if value=='Agree strongly':
                return 7

        def education(value):
            if value == 'Less than high school':
                return 1
            if value=='High school':
                return 2
            if value=='University degree':
                return 3
            if value=='Graduate degree':
                return 4

        def urban(value):
            if value == 'Rural':
                return 1
            if value=='Suburban':
                return 2
            if value=='Urban':
                return 3

        def gender(value):
            if value == 'Male':
                return 1
            if value=='Female':
                return 2
            if value=='Other':
                return 3

        def religion(value):
            if value =='Agnostic':
                return 1
            if  value=='Atheist':
                return 2
            if value=='Buddhist':
                return 3
            if value=='Christian (Catholic)':
                return 4
            if value=='Christian (Mormon)':
                return 5
            if value=='Christian (Protestant)':
                return 6
            if value=='Christian (Other)':
                return 7
            if value=='Hindu':
                return 8
            if value=='Jewish':
                return 9
            if value=='Muslim':
                return 10
            if value=='Sikh':
                return 11
            if value=='Other':
                return 12

        def orientation(value):
            if value =='Heterosexual':
                return 1
            if  value=='Bisexual':
                return 2
            if value=='Homosexual':
                return 3
            if value=='Asexual':
                return 4
            if value=='Other':
                return 5

        def race(value):
            if value =='Asian':
                return 1
            if  value=='Arab':
                return 2
            if value=='Black':
                return 3
            if value=='Indigenous Australian':
                return 4
            if value=='Native American':
                return 5
            if value=='White':
                return 6
            if value=='Other':
                return 7

        def voted(value):
            if value=='Yes':
                return 1
            if value =='No':
                return 2

        def married(value):
            if value=='Never married':
                return 1
            if value =='Currently married':
                return 2
            if value =='Previously married':
                return 3

        def ageClass(value):
            if value =='Under 10':
                return 1
            if  value=='Primary Children':
                return 2
            if value=='Secondary Children':
                return 3
            if value=='Adults':
                return 4
            if value=='Elder Adults':
                return 5
            if value =='Older People':
                return 6

        df_pred = pd.DataFrame([[Q1,Q2, Q3,Q4,Q5,Q6,Q7,Q8,Q9,Q10,Q11,Q12,Q13,Q14,TIP1,TIP2,TIP3,TIP4,TIP5,TIP6,TIP7,TIP8,TIP9,TIP10,Education,Urban,Gender,Religion,Orientation,Race,Voted,Married,Family,AgeGroup]],
        columns= ['Q1','Q2','Q3','Q4','Q5','Q6','Q7','Q8','Q9','Q10','Q11','Q12','Q13','Q14','TIP1','TIP2','TIP3','TIP4','TIP5','TIP6','TIP7','TIP8','TIP9','TIP10','Education','Urban','Gender','Religion','Orientation','Race','Voted','Married','Family','AgeGroup'])

        df_pred['Q1'] = df_pred['Q1'].apply(qoptions)
        df_pred['Q2'] = df_pred['Q2'].apply(qoptions)
        df_pred['Q3'] = df_pred['Q3'].apply(qoptions)
        df_pred['Q4'] = df_pred['Q4'].apply(qoptions)
        df_pred['Q5'] = df_pred['Q5'].apply(qoptions)
        df_pred['Q6'] = df_pred['Q6'].apply(qoptions)
        df_pred['Q7'] = df_pred['Q7'].apply(qoptions)
        df_pred['Q8'] = df_pred['Q8'].apply(qoptions)
        df_pred['Q9'] = df_pred['Q9'].apply(qoptions)
        df_pred['Q10'] = df_pred['Q10'].apply(qoptions)
        df_pred['Q11'] = df_pred['Q11'].apply(qoptions)
        df_pred['Q12'] = df_pred['Q12'].apply(qoptions)
        df_pred['Q13'] = df_pred['Q13'].apply(qoptions)
        df_pred['Q14'] = df_pred['Q14'].apply(qoptions)
        df_pred['TIP1'] = df_pred['TIP1'].apply(tipoptions)
        df_pred['TIP2'] = df_pred['TIP2'].apply(tipoptions)
        df_pred['TIP3'] = df_pred['TIP3'].apply(tipoptions)
        df_pred['TIP4'] = df_pred['TIP4'].apply(tipoptions)
        df_pred['TIP5'] = df_pred['TIP5'].apply(tipoptions)
        df_pred['TIP6'] = df_pred['TIP6'].apply(tipoptions)
        df_pred['TIP7'] = df_pred['TIP7'].apply(tipoptions)
        df_pred['TIP8'] = df_pred['TIP8'].apply(tipoptions)
        df_pred['TIP9'] = df_pred['TIP9'].apply(tipoptions)
        df_pred['TIP10'] = df_pred['TIP10'].apply(tipoptions)
        df_pred['Education'] = df_pred['Education'].apply(education)
        df_pred['Urban'] = df_pred['Urban'].apply(urban)
        df_pred['Gender'] = df_pred['Gender'].apply(gender)
        df_pred['Religion'] = df_pred['Religion'].apply(religion)
        df_pred['Orientation'] = df_pred['Orientation'].apply(orientation)
        df_pred['Race'] = df_pred['Race'].apply(race)
        df_pred['Voted'] = df_pred['Voted'].apply(voted)
        df_pred['Married'] = df_pred['Married'].apply(married)
        df_pred['AgeGroup'] = df_pred['AgeGroup'].apply(ageClass)

        df_pred = df_pred[:].values
        prediction = model.predict(df_pred)
        if(labels.inverse_transform([prediction[0]])=="Extremely Severe"):
            st.write('<p>Level Predicted: <b style="color:#8B0001">Extremely Severe</b></p>',unsafe_allow_html=True)
        if(labels.inverse_transform([prediction[0]])=="Severe"):
            st.write('<p>Level Predicted: <b style="color:#B12E21">Severe</b></p>',unsafe_allow_html=True)
        if(labels.inverse_transform([prediction[0]])=="Moderate"):
            st.write('<p>Level Predicted: <b style="color:#83D475">Moderate</b></p>',unsafe_allow_html=True)
        if(labels.inverse_transform([prediction[0]])=="Mild"):
            st.write('<p>Level Predicted: <b style="color:#57C84D">Mild</b></p>',unsafe_allow_html=True)
        if(labels.inverse_transform([prediction[0]])=="Normal"):
            st.write('<p>Level Predicted: <b style="color:#2EB62C">Normal</b></p>',unsafe_allow_html=True)
