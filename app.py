import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px

# Database Connection
engine = create_engine("mysql+pymysql://root:tiger=123@127.0.0.1:3306/phonepe")

# Streamlit UI
st.sidebar.title("📊 PhonePe Insights Dashboard")
section = st.sidebar.radio(
    "Navigate to:",
    ["Transaction Dynamics", "Device Engagement", "Insurance Analysis", "Market Expansion", "User Registration Analysis"]
)

# -------------------------------
# Transaction Dynamics Section

if section == "Transaction Dynamics":
    st.title("📈 Transaction Dynamics")
    
    # Sidebar filters
    states = pd.read_sql("SELECT DISTINCT State FROM transaction_data ORDER BY State;", engine)['State'].tolist()
    years = pd.read_sql("SELECT DISTINCT Year FROM transaction_data ORDER BY Year;", engine)['Year'].tolist()
    quarters = pd.read_sql("SELECT DISTINCT Quarter FROM transaction_data ORDER BY Quarter;", engine)['Quarter'].tolist()
    
    # Streamlit Selectboxes
    selected_state = st.sidebar.selectbox("Select State", states)
    selected_year = st.sidebar.selectbox("Select Year", years)
    selected_quarter = st.sidebar.selectbox("Select Quarter", quarters)
    
    # SQL Query with filters
    query = """
    SELECT State, Year, Quarter, Transaction_Name, SUM(Transaction_Count) AS Transaction_Count
    FROM transaction_data
    WHERE State = %s AND Year = %s AND Quarter = %s
    GROUP BY State, Year, Quarter, Transaction_Name
    """
    
    df_transaction = pd.read_sql(
        query,
        engine,
        params=(selected_state, selected_year, selected_quarter)
    )
    
    # Bar chart (better for category vs count)
    if not df_transaction.empty:
        fig = px.bar(
            df_transaction,
            x="Transaction_Name",
            y="Transaction_Count",
            color="Transaction_Name",
            labels= {"Transaction_Name" : "Payment category"},
            title=f"Transactions in {selected_state} | Year: {selected_year} | Quarter: {selected_quarter}"
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("No data available for the selected filters.")


#-------------------------------
# Device Engagement Section

elif section == "Device Engagement":
    st.title("📱 Device Engagement")

    # Sidebar filters
    states = pd.read_sql("SELECT DISTINCT State FROM user_data ORDER BY State;", engine)['State'].tolist()
    years = pd.read_sql("SELECT DISTINCT Year FROM user_data ORDER BY Year;", engine)['Year'].tolist()
    quarters = pd.read_sql("SELECT DISTINCT Quarter FROM user_data ORDER BY Quarter;", engine)['Quarter'].tolist()

    # Streamlit Selectboxes
    selected_state = st.sidebar.selectbox("Select State", states)
    selected_year = st.sidebar.selectbox("Select Year", years)
    selected_quarter = st.sidebar.selectbox("Select Quarter", quarters)

    # SQL Query with filters
    query = """
    SELECT 
        UD.State,
        UD.Year,
        UD.Quarter,
        UD.Device_Brand,
        UD.Device_Count,
        UD.Device_Percentage,
        UD2.District,
        UD2.Registered_users,
        UD2.App_opens
    FROM user_data UD
    INNER JOIN user_data_map UD2
        ON UD.State = UD2.State
       AND UD.Year = UD2.Year
       AND UD.Quarter = UD2.Quarter
    WHERE UD.State = %s AND UD.Year = %s AND UD.Quarter = %s
    """

    df_device = pd.read_sql(
        query,
        engine,
        params=(selected_state, selected_year, selected_quarter)
    )

    # Bar chart
    if not df_device.empty:
        fig = px.bar(
            df_device,
            x="Device_Brand",
            y="Device_Count",
            color="Device_Brand",
            hover_data= ["Device_Percentage", "Registered_users", "App_opens","District","Year"] , 
            labels={"Device_Brand": "Device Brand","Device_Count": "Number of Devices"},
            title=f"Device Usage in {selected_state} | Year: {selected_year} | Quarter: {selected_quarter}"
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("No device engagement data available for the selected filters.")


# -------------------------------
# Insurance Analysis Section

elif section == "Insurance Analysis":
    st.title("🛡️ Insurance Analysis")

    # Sidebar filters
    states = pd.read_sql("SELECT DISTINCT State FROM insurance_data ORDER BY State;", engine)['State'].tolist()
    years = pd.read_sql("SELECT DISTINCT Year FROM insurance_data ORDER BY Year;", engine)['Year'].tolist()

    # Streamlit Selectboxes
    selected_state = st.sidebar.selectbox("Select State", states)
    selected_year = st.sidebar.selectbox("Select Year", years)

    # SQL Query with filters
    query = """
    SELECT State, Year, Quarter, Insurance_Count, Insurance_Amount
    FROM insurance_data
    WHERE State = %s AND Year = %s
    ORDER BY Quarter;
    """

    df_insurance = pd.read_sql(query, engine, params=(selected_state, selected_year))

    # Line chart
    if not df_insurance.empty:
        fig = px.line(
            df_insurance,
            x="Quarter",
            y=["Insurance_Count", "Insurance_Amount"],
            markers=True,
            title=f"Insurance Growth Trajectory in {selected_state} and Year: {selected_year}",
            labels={"value": "Count / Amount", "Quarter": "Quarter"}
        )

        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("No insurance data available for the selected filters.")

# -------------------------------
# Market Expansion Section

elif section == "Market Expansion":
    st.title("🌍 Market Expansion")
    
     # Sidebar filters
    states = pd.read_sql("SELECT DISTINCT State FROM transaction_data ORDER BY State;", engine)['State'].tolist()
    transaction_Name = pd.read_sql("SELECT DISTINCT Transaction_Name FROM transaction_data ORDER BY Transaction_Name;", engine)['Transaction_Name'].tolist()
    
    # Streamlit Selectboxes
    selected_state = st.sidebar.selectbox("Select State", states)
    selected_transaction = st.sidebar.selectbox("Select Transaction Type", transaction_Name)
    
    # SQL Query with filters
    query = """
    SELECT State, Year, Quarter, Transaction_Name, SUM(Transaction_Count) AS Transaction_Count
    FROM transaction_data
    WHERE State = %s AND Transaction_Name = %s
    GROUP BY State, Year, Quarter, Transaction_Name
    """
    
    df_transaction = pd.read_sql(
        query,
        engine,
        params=(selected_state, selected_transaction)
    )
    
    # Bar chart (better for category vs count)
    if not df_transaction.empty:
        fig = px.bar(
            df_transaction,
            x="Year",
            y="Transaction_Count",
            hover_data=["Quarter"],
            color="Quarter",
            title=f"Transactions in {selected_state} | State : {selected_transaction}"
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("No data available for the selected filters.")


# -------------------------------
# User Engagement Section

elif section == "User Registration Analysis":
    st.title("🧑‍💻 User Registration Analysis")

    # Sidebar filters
    years = pd.read_sql("SELECT DISTINCT Year FROM user_data_top ORDER BY Year;", engine)['Year'].tolist()
    quarters = pd.read_sql("SELECT DISTINCT Quarter FROM user_data_top ORDER BY Quarter;", engine)['Quarter'].tolist()

    #selectbars
    selected_year = st.sidebar.selectbox("Select Year", years)
    selected_quarter = st.sidebar.selectbox("Select Quarter", quarters)

    # Top States
    query_states = """
    SELECT State, SUM(Registered_users) AS Total_Registered
    FROM user_data_top
    WHERE Year = %s AND Quarter = %s
    GROUP BY State
    ORDER BY Total_Registered DESC
    LIMIT 10;
    """
    df_states = pd.read_sql(query_states, engine, params=(selected_year, selected_quarter))

    fig_states = px.bar(
        df_states,
        x="State",
        y="Total_Registered",
        color="State",
        title=f"Top 10 States by User Registrations | Year: {selected_year}, Quarter: {selected_quarter}"
    )
    st.plotly_chart(fig_states, use_container_width=True)

    # Top Districts
    query_districts = """
    SELECT District, SUM(Registered_users) AS Total_Registered
    FROM user_data_top
    WHERE Year = %s AND Quarter = %s
    GROUP BY District
    ORDER BY Total_Registered DESC
    LIMIT 10;
    """
    df_districts = pd.read_sql(query_districts, engine, params=(selected_year, selected_quarter))

    fig_districts = px.bar(
        df_districts,
        x="District",
        y="Total_Registered",
        color="District",
        title=f"Top 10 Districts by User Registrations | Year: {selected_year}, Quarter: {selected_quarter}"
    )
    st.plotly_chart(fig_districts, use_container_width=True)

    # Top Pin Codes
    query_pins = """
    SELECT Pincodes, SUM(Pin_registered_users) AS Total_Pin_Registered
    FROM user_data_top
    WHERE Year = %s AND Quarter = %s
    GROUP BY Pincodes
    ORDER BY Total_Pin_Registered DESC
    LIMIT 10;
    """
    df_pins = pd.read_sql(query_pins, engine, params=(selected_year, selected_quarter))

    fig_pins = px.bar(
        df_pins,
        x="Pincodes",
        y="Total_Pin_Registered",
        color="Pincodes",
        title=f"Top 10 Pin Codes by User Registrations | Year: {selected_year}, Quarter: {selected_quarter}"
    )
    st.plotly_chart(fig_pins, use_container_width=True)
