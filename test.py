import streamlit as st

st.set_page_config(page_title="Test App", layout="wide")

st.title("✅ Test App is Working")
st.write("If you see this, Streamlit is running correctly!")

try:
    import joblib
    st.success("✅ joblib is installed")
except ImportError:
    st.error("❌ joblib is not installed")

try:
    import sklearn
    st.success(f"✅ scikit-learn version: {sklearn.__version__}")
except ImportError:
    st.error("❌ scikit-learn is not installed")