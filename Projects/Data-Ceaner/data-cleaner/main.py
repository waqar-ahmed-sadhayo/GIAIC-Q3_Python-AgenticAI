import streamlit as st
import pandas as pd
from io import BytesIO

# Set page configuration
st.set_page_config(page_title="📁 File Converter & Cleaner", layout="wide")
st.title("📁 File Converter & Cleaner")
st.write("📁 Upload your CSV or Excel files to ✨ clean data and 🔄 convert formats effortlessly!")

# File uploader
files = st.file_uploader(
    "Upload CSV or Excel Files",
    type=["csv", "xlsx"],
    accept_multiple_files=True
)

# Process each uploaded file
if files:
    for file in files:
        ext = file.name.split(".")[-1].lower()
        df = pd.read_csv(file) if ext == "csv" else pd.read_excel(file)

        st.subheader(f"🔎 {file.name} - Preview")
        st.dataframe(df.head())

        # Fill missing values
        if st.checkbox(f"🛠 Fill Missing Values - {file.name}"):
            df.fillna(df.select_dtypes(include='number').mean(), inplace=True)
            st.success("✅ Missing values filled successfully!")
            st.dataframe(df.head())

        # Column selection
        selected_columns = st.multiselect(
            f"🧩 Select Columns - {file.name}",
            df.columns,
            default=df.columns
        )
        df = df[selected_columns]
        st.dataframe(df.head())

        # Show chart
        if st.checkbox(f"📊 Show Chart - {file.name}") and not df.select_dtypes(include='number').empty:
            st.bar_chart(df.select_dtypes(include='number').iloc[:, :2])

        # Format conversion choice
        format_choice = st.radio(
            f"🧾 Convert {file.name} to:",
            ["CSV", "Excel"],
            key=file.name
        )

        # Prepare and show download button
        output = BytesIO()
        if format_choice == "CSV":
            df.to_csv(output, index=False)
            mime = "text/csv"
            new_name = file.name.rsplit(".", 1)[0] + ".csv"
        else:
            df.to_excel(output, index=False, engine='openpyxl')
            mime = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            new_name = file.name.rsplit(".", 1)[0] + ".xlsx"
        output.seek(0)

        st.download_button(
            label=f"⬇ Download {new_name}",
            data=output,
            file_name=new_name,
            mime=mime,
            key=f"download-{file.name}"
        )

        st.success("🎉 Processing Completed!")


