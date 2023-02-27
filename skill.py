import streamlit as st
import snowflake.connector

# Connect to Snowflake
conn = snowflake.connector.connect(
    user='learnatozaboutdata02',
    password='Snowflake@143#',
    account='kl98250.ca-central-1.aws',
    warehouse='COMPUTE_WH',
    database='YT',
    schema='SF_SQL'
)

# Define the dropdown options
skill_options = ['Java', 'Python', 'SQL', 'C++']
interest_options = ['Hiking', 'Reading', 'Cooking', 'Traveling']
certification_options = ['AWS Certified Developer', 'CCNA', 'PMP', 'Scrum Master']

# Define the Snowflake table schema
table_schema = '''
CREATE TABLE IF NOT EXISTS employee_skillset (
   employee_id INTEGER,
   primary_skill VARCHAR(50),
   secondary_skill VARCHAR(50),
   personal_interest VARCHAR(50),
   certification VARCHAR(50)
);
'''

# Execute the CREATE TABLE statement
with conn.cursor() as cursor:
    cursor.execute(table_schema)

# Define the Streamlit app
def app():
    st.title("Employee Skillset")
    
    # Get employee information from the user
    employee_id = st.number_input("Employee ID")
    primary_skill = st.selectbox("Primary Skill", skill_options)
    secondary_skill = st.selectbox("Secondary Skill", skill_options)
    personal_interest = st.selectbox("Personal Interest", interest_options)
    certification = st.selectbox("Certification", certification_options)
    
    # Insert the employee information into the Snowflake table
    if st.button("Submit"):
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO employee_skillset VALUES (%s, %s, %s, %s, %s)", 
                           (employee_id, primary_skill, secondary_skill, personal_interest, certification))
            conn.commit()
        st.success("Employee information added successfully.")

# Run the Streamlit app
if __name__ == '__main__':
    app()
