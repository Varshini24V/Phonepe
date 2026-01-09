# PhonePe Insights Dashboard

This repository explores various use cases of the PhonePe application using data from the PhonePe Pulse dataset(https://github.com/PhonePe/pulse).  
The project connects to a MySQL database via **SQLAlchemy** and visualizes insights interactively with **Streamlit** and **Plotly Express**.

--------------------------------------------

Dataset
The dataset is sourced from **PhonePe Pulse** and organized into three categories of tables:

- **Aggregated Tables**
  - `Aggregated_user`
  - `Aggregated_transaction`
  - `Aggregated_insurance`

- **Map Tables**
  - `Map_user`
  - `Map_transaction`
  - `Map_insurance`

- **Top Tables**
  - `Top_user`
  - `Top_transaction`
  - `Top_insurance`

--------------------------------------------

Technical skills
- **Python** (data processing & visualization)
- **SQLAlchemy** (database connection)
- **MySQL Workbench** (data storage & queries)
- **Streamlit** (interactive dashboard)
- **Plotly Express** (visualizations)

--------------------------------------------

## Use Cases
The dashboard provides insights into the following areas:

1. **Transaction Dynamics**  
   Analyze transaction categories, counts, and trends across states and quarters.

2. **Device Engagement**  
   Explore user preferences across device brands, comparing registrations vs. app opens.

3. **Insurance Analysis**  
   Track growth trajectory of insurance adoption and identify untapped opportunities.

4. **Market Expansion**  
   Study transaction types and their growth patterns to highlight expansion potential.

5. **User Registration Analysis**  
   Identify top states, districts, and pin codes driving user registrations.
