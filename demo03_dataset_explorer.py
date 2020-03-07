import streamlit as st 
import os 


# EDA Pkgs 
import pandas as pd 

# Viz Pkgs 
import matplotlib.pyplot as plt 
import matplot
import seaborn as sns 


def main():
    """
        Common ML Dataset Explorer
    """

    st.title("Common ML Dataset Explorer")
    st.subheader("Simple Data Science Explorer with Streamlit")

    html_temp = """
        <div style="background-color:tomato;"><p style="color:white;font-size:50px;">Streamlit is Awesome</p></div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    def file_selector(folder_path='./datasets'):
        filenames = os.listdir(folder_path)
        selected_filename = st.selectbox("Select A file", filenames)
        return os.path.join(folder_path, selected_filename)        

    filename = file_selector()
    st.info("You Selected {}".format(filename))

    # Read Data
    df = pd.read_csv(filename)
    
    # Show Dataset 
    if st.checkbox("Show dataset"):
        number = st.number_input("number of rows to view", 5, 10)
        st.dataframe(df.head(number))

    # Show Columns 
    if st.button("Column Names"):
        st.write(df.columns)        

    # Show Shape
    if st.checkbox("Shape of Dataset"):
        st.write(df.shape)
        data_dim = st.radio("Show Dimension By ", ("Rows", "Columns"))
        if data_dim == 'Columns':
            st.text("Number of Columns")
            st.write(df.shape[1])
        elif data_dim == 'Rows':
            st.text("Number of Rows")
            st.write(df.shape[0])
        else:
            st.write(df.shape)

    # Select Columns
    if st.checkbox("Select Columns To Show"):
        all_columns = df.columns.tolist() 
        selected_columns = st.multiselect("Select", all_columns)
        new_df = df[selected_columns]
        st.dataframe(new_df)    

    # Show Values 
    if st.button("Value Counts"):
        st.text("Value Counts by Target/Class")
        st.write(df.iloc[:,1].value_counts())

    # Show DataTypes
    if st.button("Data Type"):
        st.write(df.dtypes)

    # Show Summary 
    if st.checkbox("Summary"):
        st.write(df.describe().T)

    ## Plot and Visualization
    st.subheader("Data Visualization")

    # Correlation


    # Seaborn Plot


    # Count Plot 


    # Pie Chart 


    # Customizable Plot
    st.subheader("Customizable Plot")
    all_columns_names = df.columns.tolist()
    type_of_plot = st.selectbox("Select Type of Plot", ["area", "bar", "line", "hist", "box", "kde"])
    selected_columns_names = st.multiselect("Select Columns To Plot", all_columns_names)

    if st.button("Generate Plot"):
        st.success("Generation Customizable Plot of {} for {}".format(type_of_plot, selected_columns_names))

        # Plot by Streamlit 
        if type_of_plot == 'area':
            cust_data = df[selected_columns_names]
            st.area_chart(cust_data)




if __name__ == "__main__":
    main()