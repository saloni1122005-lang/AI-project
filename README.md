# AI-project

☀️ Solar DC Power Forecasting System for Renewable Energy Optimization

Project Overview  
This project develops a machine learning–based solar DC power forecasting system. It predicts solar panel output using environmental parameters such as irradiation, module temperature, and ambient temperature. The system helps optimize renewable energy planning, grid stability, and efficient resource utilization.  

❗ Problem Statement  
Solar energy generation is highly variable due to environmental factors:  
- Fluctuating irradiation levels  
- Temperature effects on panel efficiency  
- Unpredictable weather conditions  

These challenges lead to:  
- Inconsistent energy supply  
- Difficulty in grid integration  
- Inefficient resource management  

💡 Proposed Solution  
The system leverages AI/ML techniques to:  
- Analyze solar plant and weather sensor data  
- Preprocess inputs for accurate modeling  
- Predict DC power output in real time  
- Provide actionable insights for energy optimization  

🔄 System Workflow  
Solar Data → Preprocessing (Scaler) → Trained ML Model → Forecasting App → DC Power Prediction  


🧩 System Architecture  

1. Data Acquisition  
   - Historical datasets from solar plants and weather sensors  
   - Attributes: irradiation, module temperature, ambient temperature  

2. Preprocessing  
   - Normalization using saved scaler (scaler.pkl)  
   - Cleaning and merging datasets  

3. Machine Learning Model  
   - Trained regression model (solarPowerGeneration_model.pkl)  
   - Predicts DC power output based on input parameters  

4. Deployment  
   - Flask-based web app (app.py)  
   - User inputs environmental data → system outputs predicted DC power  

5. Documentation & Reproducibility  
   - README.md for usage instructions  
   - requirements.txt for dependencies  


🛠️ Technology Stack  
- Frontend: HTML, CSS, JavaScript  
- Backend: Python, Flask  
- Machine Learning: Regression modeling, Scikit-learn  
- Data Handling: Pandas, CSV datasets  
- Deployment: Web app interface  



📊 Expected Outcomes  
- Improved accuracy in solar power forecasting  
- Better grid stability and planning  
- Efficient renewable energy utilization  
- Reduced dependency on non-renewable sources  

🌍 Impact  
The system supports sustainable energy development by enabling accurate solar power forecasting, reducing inefficiencies, and promoting renewable energy adoption.  


👨‍💻 Author  
Saloni Prasad  

