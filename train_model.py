import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# ✅ Load the dataset
data_path = "data/career_dataset_7000.csv"
df = pd.read_csv(data_path)

# ✅ Print columns for reference
print("Available Columns in Dataset:\n", df.columns.tolist())

# ✅ Automatically detect the target column (case-insensitive match)
target_col = None
for col in df.columns:
    if "career" in col.lower():
        target_col = col
        break

if target_col is None:
    raise ValueError("❌ Could not find target column like 'Recommended Career Path' or similar.")

# ✅ Drop unused columns (like Name if exists)
drop_cols = [target_col]
if "Name" in df.columns:
    drop_cols.append("Name")

X = df.drop(drop_cols, axis=1)
y = df[target_col]

# ✅ One-hot encode categorical features
X = pd.get_dummies(X)
X.columns = X.columns.astype(str)

# ✅ Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ✅ Train Random Forest Classifier
model = RandomForestClassifier()
model.fit(X_train, y_train)

# ✅ Save trained model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model training complete. File saved as 'model.pkl'.")
