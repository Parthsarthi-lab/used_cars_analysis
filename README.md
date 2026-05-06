# Used Car Market Analysis: Identifying Key Price Drivers

## 📌 Project Overview
The used car market is characterized by high information asymmetry between buyers and sellers[cite: 1]. This project performs an in-depth Exploratory Data Analysis (EDA) on a vehicle dataset to identify the primary factors influencing resale value. By moving beyond basic descriptive statistics, this analysis identifies critical price drivers, depreciation patterns, and data integrity issues often overlooked in standard reports.

## 📖 Research Context & Literature Review
This analysis was informed by existing industry research, specifically the study by **Xinru Chen et al.** regarding used car pricing[cite: 1]. Key findings from the literature include:
*   **Primary Predictors:** "Max Power" is identified as the most significant technical predictor of price, followed by "Vehicle Age" and "Average Cost Price"[cite: 1].
*   **Key Correlations:** Research highlights a strong positive correlation between engine size and power, while vehicle age and kilometers driven typically show negative correlations with resale value[cite: 1].
*   **Visualization Standards:** Industry standards suggest using histograms to address price distribution skewness and box plots to isolate outliers across categorical variables[cite: 1].

## 📊 Key Analytical Insights
*   **Price Skewness:** Initial visualization revealed a heavily right-skewed price distribution, necessitating log transformations to normalize data for potential modeling[cite: 1].
*   **The Depreciation Curve:** Analysis identifies a non-linear depreciation rate, with significant value loss occurring within the first few years[cite: 1].
*   **Power vs. Utility:** Corroborating literature, vehicle power was a significantly stronger price driver than utility features such as seating capacity[cite: 1].
*   **Data Integrity Matters:** A systematic **Data Audit** identified that roughly 11% of raw records contained impossible values (e.g., negative mileage or future years) that would have invalidated basic metric calculations[cite: 1].

## 📖 Data Dictionary
This dataset contains 10,000 observations representing vehicle records within the used car market[cite: 1].

| Column Name | Data Type | Description | Values/Constraints |
| :--- | :--- | :--- | :--- |
| **car_id** | Integer | Unique identifier for each vehicle record[cite: 1]. | Primary Key |
| **brand** | String | The automobile manufacturer[cite: 1]. | e.g., Honda, Audi, BMW |
| **model** | String | The specific model name of the vehicle[cite: 1]. | e.g., Model A, Model B |
| **year** | Integer | The manufacturing year of the vehicle[cite: 1]. | Validated to $\leq 2025$ |
| **mileage** | Float | Total distance driven by the vehicle in kilometers[cite: 1]. | Must be $\geq 0$ |
| **fuel_type** | String | The type of fuel used by the engine[cite: 1]. | Petrol, Diesel, Hybrid |
| **transmission** | String | The type of gearbox in the vehicle[cite: 1]. | Manual, Automatic |
| **sale_month** | Integer | The month in which the vehicle was listed for sale. | 1 (Jan) to 12 (Dec) |
| **zip_prefix** | Integer | Geographic identifier for the vehicle location. | Regional code |
| **price** | Integer | The final resale/selling price of the vehicle[cite: 1]. | Target Variable ($) |
| **age** | Integer | Calculated vehicle age (Reference year - year)[cite: 1]. | Derived Feature |

### 🛠️ Data Audit & Integrity Notes
A systematic data audit revealed the following anomalies which were corrected during the preprocessing phase to ensure model reliability:
*   **Temporal Anomalies:** Records with manufacturing years listed as 2030 (future cars) were excluded[cite: 1].
*   **Impossible Metrics:** Vehicles with negative mileage values were corrected or imputed[cite: 1].
*   **Categorical Errors:** The invalid fuel category 'XYZ' was identified as a typo and mapped to 'Petrol' based on brand distributions[cite: 1].
*   **Price Cleaning:** Observations with a price of \$0 or extreme outliers above \$200,000 were removed to prevent distribution distortion[cite: 1].

## 🛠️ Tech Stack
*   **Language:** Python 3.10+
*   **Libraries:** Pandas, NumPy, Matplotlib, Seaborn, Scipy[cite: 1]
*   **Environment:** Jupyter Notebook

## 📈 Methodology
*   **Systematic Data Audit:** Checking for logical anomalies and categorical validity[cite: 1].
*   **Informed Cleaning:** Rectifying "future" car years and invalid fuel categories discovered during the audit[cite: 1].
*   **Intelligent Imputation:** Using median-by-age groups for missing mileage data to maintain age-dependent utility relationships[cite: 1].
*   **Advanced Visualization:** Implementing regression plots, log-transformed histograms, and heatmaps to reveal non-obvious market trends[cite: 1].

## 📁 Repository Structure
```text
├── data/
│   └── used_cars_mock.csv       # Raw dataset
├── notebooks/
│   └── Used_Car_Analysis.ipynb  # Primary analytical notebook
├── requirements.txt             # Required Python libraries
└── README.md                    # Project documentation
```

## 👤 Author
*   **Name:** [Your Name]
*   **LinkedIn:** [Your Link]
*   **Portfolio:** [Your Link]

---
*Note: This analysis serves as a record of analytical rigor, transforming raw data into actionable business strategy.*