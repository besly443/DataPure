============================================================
🧼 DataPure – Smart Data Cleaning
Developed by: Dr Nabari T. – Palestine / Negev
© 2025 Dr Nabari T. — All Rights Reserved
License: MIT License (see below)
Unauthorized copying, removal of attribution, or rebranding is prohibited.
Ownership marker: 3c7d99b8-DataPure-DrNabariT-2025
============================================================

-------------------------
[ SOURCE CODE ]
-------------------------
import streamlit as st
import pandas as pd
import io

# Hidden HTML ownership marker (appears in page source)
st.markdown(
    "<!-- DataPure | © 2025 Dr Nabari T. | Palestine / Negev | Ownership marker: 3c7d99b8 -->",
    unsafe_allow_html=True
)

st.set_page_config(page_title="DataPure", layout="centered")

st.title("🧼 DataPure – تنظيف البيانات الذكي")
st.markdown("### ارفع ملفك، نظّفه، وحمّله نظيفًا ✨")

uploaded_file = st.file_uploader("📂 اختر ملف Excel أو CSV", type=["csv", "xlsx"])

if uploaded_file:
    try:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        st.subheader("📊 معاينة البيانات الأصلية")
        st.dataframe(df.head())

        # تنظيف البيانات
        cleaned_df = df.drop_duplicates()
        cleaned_df = cleaned_df.dropna(how='all')  # حذف الصفوف الفارغة تمامًا

        st.subheader("✅ البيانات بعد التنظيف")
        st.dataframe(cleaned_df.head())

        # تحميل الملف النظيف
        buffer = io.BytesIO()
        cleaned_df.to_csv(buffer, index=False)
        buffer.seek(0)

        st.download_button(
            label="⬇️ تحميل الملف النظيف",
            data=buffer,
            file_name="cleaned_data.csv",
            mime="text/csv"
        )

    except Exception as e:
        st.error(f"حدث خطأ أثناء معالجة الملف: {e}")

# Footer with visible attribution
st.markdown("---")
st.caption("© 2025 Dr Nabari T. — DataPure. جميع الحقوق محفوظة. لا يُسمح بإزالة النسبة أو إعادة النشر دون إذن.")

-------------------------
[ README ]
-------------------------
🧼 DataPure – Smart Data Cleaning
Developed by: Dr Nabari T. – Palestine / Negev
© 2025 All Rights Reserved

Description:
DataPure is an interactive Streamlit application designed to clean datasets quickly and intelligently.
It removes duplicates, deletes empty rows, and prepares your data for analysis with minimal effort.

Features:
- Automatic duplicate removal
- Empty row deletion
- Supports CSV and Excel formats
- Easy-to-use interface
- Fast processing

How to Run Locally:
1. Install Python 3.9 or later.
2. Install required packages:
   pip install streamlit pandas openpyxl
3. Run the application:
   streamlit run app.py

Supported File Types:
- CSV (.csv)
- Excel (.xlsx)

License:
This project is licensed under the MIT License.
Unauthorized copying, modification, rebranding, or redistribution is strictly prohibited without prior written permission from the author.

Legal Notice:
This software and its source code are the intellectual property of Dr Nabari T.
Any use, reproduction, or distribution without explicit permission is a violation of applicable copyright laws.
The author's name and attribution must remain visible in all copies or derivatives.

Change Log:
v1.0.0 – Initial release (2025-09-06)
- Core functionality: file upload, duplicate removal, empty row deletion, download cleaned file.

Contact:
Dr Nabari T.
Palestine / Negev
Email: busidoors@gmail.com

-------------------------
[ MIT LICENSE ]
-------------------------
MIT License

Copyright (c) 2025 Dr Nabari T.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
(Complete MIT text here)
