import streamlit as st
import pandas as pd
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

            
st.title("Data Explorer")
st.subheader("Automatic Data Analysis using Python" )
upload=st.file_uploader("Upload dataset here",type=['csv'])
if upload:
   data=pd.read_csv(upload)
   
use_defo = st.checkbox('Use example Dataset')
if use_defo:
    upload = 'Bengaluru_House_Data.csv'
    data=pd.read_csv(upload)
  #Show dataset  
if upload is not None:
   
    sample_data=st.radio("Preview Dataset Sample",("Random Sample","Head","Tail"))
    
    if sample_data=="Random Sample":
        st.write(data.sample(5))
    if sample_data=="Head":
        st.write(data.head())
    if sample_data=="Tail":
        st.write(data.tail())

        
#Show shape  
if upload is not None:
    
  data_shape=st.radio("Dimensions",('Rows','Columns'))    
  if data_shape=='Rows':
      st.text('No.of rows')
      st.write(data.shape[0])
  

  if data_shape=='Columns':
      st.text('No.of columns')
      st.write(data.shape[1])
      
#COlumn names
if upload is not None:
    if st.button("Check Features"):
        st.write("Names of features:")
        st.write(data.columns)            
#Datatype of each column        
if upload is not None:
    if st.button('Check Datatype'):
       st.write("Dataype of features:")
       res=data.dtypes.astype(str)
       st.write(res)
       
        
#Descriptive stats
if upload is not None:
    if st.button('Data Statistics'):
       st.write("Statistical Description of data")
       st.write(data.describe()) 
            
#check nullvalues
if upload is not None:
    if st.button('Check null values'):
        test=data.isnull().values.any()
        if test==True:
            st.write(data.isnull().sum())
        
        else:
            st.write("No null values in data")
            

#Duplicate values
if upload is not None:
    if st.button('Check for Duplicates'):
        test=data.duplicated().any()
        if test==True:
            st.write(f'Data contains {data.duplicated().sum()} duplicate rows')
           
        else:
            st.write("No duplicates founds")
        
#remove duplicates
if upload is not None:
   test=data.duplicated().any()
   if test==True:
          old_shape=data.shape[0]
          dup=st.radio("Remove Duplicated values", ('No','Yes'))
          if dup=="No":
              st.warning("Duplicates Conserved")
          if dup=='Yes':
              data=data.drop_duplicates()
              new_rows=data.shape[0]
              n=old_shape-new_rows
              st.warning(f"{n} rows dropped")
              st.warning(f"New Shape: {data.shape}")
              
#Profiling
if upload is not None:
    if st.button("Generate Profile Report"):
         pr = ProfileReport(data, explorative=True)
         st.header('**Input DataFrame**')
         st.write(data)
         st.write('---')
         st.header('**Pandas Profiling Report**')
         st_profile_report(pr)
         export=pr.to_html()
         st.download_button(label="Download Full Report", data=export, file_name='report.html')
        
        
            
            
            
            
            
            
            