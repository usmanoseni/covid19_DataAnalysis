# 📊 COVID-19 Research Analysis Dashboard  

## 📝 Project Overview  
This Streamlit dashboard provides an interactive way to explore COVID-19 research publications.  
It allows filtering by publication year and journal, and includes visualizations to understand publication trends, top journals, and distribution of research sources.  

---

## 🔍 Key Findings  
1. **Publications Over Time**  
   - A significant increase in research publications was observed during the peak pandemic years (2020–2021).  
   - After 2021, the number of publications started to stabilize.  

2. **Top Journals**  
   - A small number of journals contributed the majority of COVID-19 papers.  
   - These top 10 journals reflect where most researchers preferred to publish.  

3. **Research Sources**  
   - Certain URLs/sources hosted more papers, showing centralized repositories of COVID-19 studies.  

---

## ⚡ Challenges Faced  
- **Figure vs Axes Confusion**  
  - Initially, there was confusion about why both `fig` and `ax` objects were required in `matplotlib`.  
  - Learned that `fig` is the overall canvas (for displaying/saving), while `ax` is the plotting area (for customizing).  

- **Streamlit Integration**  
  - Using `st.pyplot(fig)` was necessary to properly display plots inside Streamlit.  
  - Direct use of `plt.show()` worked locally but not inside the Streamlit app.  

- **Large Dataset Handling**  
  - The dataset was big, requiring filtering (e.g., limiting journal options to the first 50) to keep the dashboard responsive.  

---

## 📚 Learning Outcomes  
- Improved understanding of **matplotlib’s object-oriented interface** (`fig`, `ax`) vs. pyplot state-based plotting.  
- Learned best practices for embedding visualizations in **Streamlit dashboards**.  
- Gained insights into COVID-19 research trends through **exploratory data analysis (EDA)**.  
