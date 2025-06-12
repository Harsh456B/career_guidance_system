import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import pandas as pd

def visualize_recommendations(model):
    feature_importance = model.feature_importances_
    features = model.feature_names_in_

    data = pd.DataFrame({
        "Feature": features,
        "Importance": feature_importance
    })

    data = data.sort_values("Importance", ascending=False).head(10)

    plt.figure(figsize=(10, 5))
    sns.barplot(data=data, x="Importance", y="Feature", palette="Purples")
    plt.title("Top 10 Important Features")
    st.pyplot(plt)
