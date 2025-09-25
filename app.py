import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load the dataset
data = pd.read_csv('cleaned_metadata.csv')

st.title("COVID-19 Research Analysis")
st.write("This dashboard lets you explore COVID-19 research data using the widgets on the sidebar to interact with the dataset.")

# Show sample of dataset
st.subheader("Dataset Overview")
st.dataframe(data.head(40))

# Sidebar filters
st.sidebar.header("Filters")

# Year filter
year_options = data['publish_year'].dropna().unique()
year_selected = st.sidebar.selectbox("Select Year", sorted(year_options))

# Journal filter (limit to first 50 for usability)
journal_options = data['journal'].dropna().unique()
journal_selected = st.sidebar.selectbox(
    "Select Journal", sorted(journal_options[:50]))

# Visualization 1: Publications Over Time
st.header("Publications Over Time")
fig, ax = plt.subplots(figsize=(10, 8))
year = data.groupby("publish_year")["title"].count().sort_index()
sns.lineplot(x=year.index, y=year.values, color='green', marker='o', ax=ax)
ax.set_title("Number of Papers Published Over Time")
ax.set_xlabel("Publication Year")
ax.set_ylabel("Number of Papers")
ax.grid()
st.pyplot(fig)

# Visualization 2: Top Journals
st.subheader("Top Journals Publishing COVID-19 Research")
fig, ax = plt.subplots(figsize=(11, 6))
top_journals = data['journal'].value_counts().head(10)
sns.barplot(x=top_journals.index, y=top_journals.values,
            palette='viridis', ax=ax)
ax.set_title("Top 10 Journals Publishing COVID-19 Research")
ax.set_xlabel("Journal")
ax.set_ylabel("Number of Papers")
plt.xticks(rotation=45, ha='right')
st.pyplot(fig)

# Visualization 3: Distribution of Paper Counts by Source
st.subheader("Distribution of Paper Counts by Source")
fig, ax = plt.subplots(figsize=(10, 6))
url_count = data['url'].value_counts().head(10)  # top 10 only
sns.barplot(x=url_count.index, y=url_count.values, palette='viridis', ax=ax)
ax.set_title("Top 10 URLs with Most Papers")
ax.set_xlabel("URL")
ax.set_ylabel("Number of Papers")
plt.xticks(rotation=45, ha='right')
st.pyplot(fig)
