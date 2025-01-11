import streamlit as st
import pickle
import pandas as pd

# Load the data
medicines_dict = pickle.load(open('medicine_dict.pkl', 'rb'))
medicines = pd.DataFrame(medicines_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Recommendation function
def recommend(medicine):
    medicine_index = medicines[medicines['Drug_Name'] == medicine].index[0]
    distances = similarity[medicine_index]
    medicines_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_medicines = []
    for i in medicines_list:
        recommended_medicines.append(medicines.iloc[i[0]].Drug_Name)
    return recommended_medicines

# Streamlit page setup
st.set_page_config(page_title="Medicine Recommendation System", page_icon="💊")

# Background image style using Markdown
background_image_url = 'https://static.vecteezy.com/system/resources/previews/004/987/898/large_2x/doctor-in-medical-lab-coat-with-a-stethoscope-doctor-in-hospital-background-with-copy-space-low-poly-wireframe-vector.jpg'
st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("{background_image_url}");
        background-size: cover;
        background-position: center;
        color: white;
        padding-top: 50px;
        font-family: Arial, sans-serif;
    }}
    .header-box {{
        background-color: rgba(0, 0, 0, 0.6);
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 30px;
    }}
    .header-box h1 {{
        font-weight: bold;
        font-size: 42px;
        color: #FFFFFF;
    }}
    .header-box p {{
        font-size: 20px;
        color: #FFFFFF;
    }}
    .stButton>button {{
        background-color: #FF6347;
        color: white;
        font-size: 20px;
        padding: 12px 25px;
        border-radius: 5px;
        border: none;
        cursor: pointer;
    }}
    .stButton>button:hover {{
        background-color: #FF4500;
    }}
    .footer {{
        text-align: center;
        padding: 25px;
        margin-top: 50px;
        background-color: rgba(0, 0, 0, 0.6);
        color: white;
        font-size: 18px;
        border-radius: 10px;
    }}
    .recommendation-box {{
        background-color: rgba(255, 255, 255, 0.7);
        padding: 30px;
        border-radius: 15px;
        margin-top: 30px;
        color: #000000;
    }}
    .recommendation-list {{
        font-size: 26px;  /* Increased font size for recommended medicines */
        list-style: none;
        margin-top: 20px;
    }}
    .recommendation-list li {{
        background-color: rgba(255, 255, 255, 0.8);
        margin: 15px 0;
        padding: 15px;
        border-radius: 5px;
        font-size: 26px;  /* Increased font size for each medicine inside the box */
    }}
    </style>
""", unsafe_allow_html=True)

# Header box with title
st.markdown("""
    <div class="header-box">
        <h1>Medicine Recommendation System</h1>
        <p>Select a medicine to get similar recommendations.</p>
    </div>
""", unsafe_allow_html=True)

# Dropdown for selecting a medicine
selected_medicine_name = st.selectbox("Select a medicine:", medicines['Drug_Name'].values)

# Recommend button
if st.button("Get Recommendations"):
    recommendations = recommend(selected_medicine_name)
    
    # Display recommendations inside the box with larger font
    st.markdown("<div class='recommendation-box'>", unsafe_allow_html=True)
    st.write("### Recommended Medicines:")
    st.markdown("<ul class='recommendation-list'>", unsafe_allow_html=True)
    for med in recommendations:
        st.write(f"<li>{med}</li>", unsafe_allow_html=True)
    st.markdown("</ul>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Footer with your name
st.markdown("""
    <div class="footer">
        <p>Created by Asmita Chavan</p>
    </div>
""", unsafe_allow_html=True)
