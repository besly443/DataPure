import streamlit as st
import pandas as pd
import io

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
