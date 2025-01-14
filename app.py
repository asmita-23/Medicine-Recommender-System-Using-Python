import streamlit as st
import pickle
import pandas as pd

# Load the data
medicines_dict = pickle.load(open('medicine_dict.pkl', 'rb'))
medicines = pd.DataFrame(medicines_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Function to recommend medicines
def recommend(medicine):
    medicine_index = medicines[medicines['Drug_Name'] == medicine].index[0]
    distances = similarity[medicine_index]
    medicines_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_medicines = []
    for i in medicines_list:
        recommended_medicines.append(medicines.iloc[i[0]].Drug_Name)
    return recommended_medicines

# Function to set background image with stronger blur effect and improved visibility for content
def set_background_image(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url('{image_url}') no-repeat center center fixed;
            background-size: cover;
        }}
        .blur-overlay {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            backdrop-filter: blur(80px); /* Stronger blur effect */
            z-index: -1;
        }}
        .content {{
            position: relative;
            z-index: 1;
        }}
        /* Stronger black overlay for better content visibility */
        .content-overlay {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.9); /* Darker black overlay */
            z-index: 0;
        }}
        .title-box {{
            border: 2px solid white; /* White border for the title box */
            padding: 15px;
            display: inline-block;
            background-color: rgba(0, 0, 0, 0.5); /* Semi-transparent background for better readability */
            border-radius: 8px;
        }}
        .white-text {{
            color: white !important; /* White text for key elements */
        }}
        .medicine-box {{
            background-color: rgba(255, 255, 255, 0.9); /* Slightly opaque box for medicines */
            padding: 12px;
            border-radius: 8px;
            margin-bottom: 12px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
            display: flex;
            justify-content: space-between; /* Align button to the right */
            align-items: center;
            transition: transform 0.3s ease-in-out; /* Smooth hover effect */
        }}
        .medicine-box:hover {{
            transform: scale(1.05); /* Slight zoom effect on hover */
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3); /* Larger shadow on hover */
        }}
        .medicine-text {{
            font-size: 18px;
            color: black !important; /* Black font for medicine names */
            font-weight: 600;
        }}
        .selectbox label {{
            color: white !important; /* White font for select box label */
            font-weight: bold;
            font-size: 22px; /* Increased font size */
        }}
        .highlighted-text {{
            font-weight: bold;
            color: #ffcc00; /* Gold color for highlighting */
        }}
        .btn-container {{
            text-align: right; /* Align button to the right */
        }}
        .btn-container button {{
            background-color: #28a745;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
            font-weight: bold;
            transition: background-color 0.3s ease; /* Smooth background transition */
        }}
        .btn-container button:hover {{
            background-color: #218838; /* Darker green when hovered */
        }}
        .footer {{
            text-align: center;
            color: white;
            font-size: 18px;
            margin-top: 30px;
        }}
        </style>
        <div class="blur-overlay"></div>
        <div class="content-overlay"></div>  <!-- Stronger black overlay -->
        """,
        unsafe_allow_html=True
    )

# Set the background image
set_background_image('https://img.freepik.com/premium-photo/pile-several-medicines-black-background-generative-ai_666746-4365.jpg')

# Title
st.markdown(
    """
    <div class="content" style="text-align: center;">
        <div class="title-box">
            <h1 style="font-size: 56px; font-weight: bold; margin: 0;" class="white-text">
                Medicine Recommender System
            </h1>
        </div>
        <p style="font-size: 30px; margin: 10px 0;" class="white-text">
            Type your medicine name whose alternative is to be recommended
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# Medicine selection dropdown
st.markdown(
    """
    <div class="content" style="text-align: center;">
        <label for="medicine-dropdown" class="highlighted-text">Select a Medicine</label>
    </div>
    """,
    unsafe_allow_html=True
)

selected_medicine_name = st.selectbox(
    "Select a Medicine", medicines['Drug_Name'].values, key="medicine_dropdown"
)

# Function to recommend medicines
def recommend(medicine):
    medicine_index = medicines[medicines['Drug_Name'] == medicine].index[0]
    distances = similarity[medicine_index]
    medicines_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_medicines = []
    for i in medicines_list:
        recommended_medicines.append(medicines.iloc[i[0]].Drug_Name)
    return recommended_medicines

# Button to recommend medicines
if st.button("Recommend Medicines"):
    if selected_medicine_name:
        recommendations = recommend(selected_medicine_name)
        st.markdown(
            f"<h2 class='white-text'>Recommended Medicines for {selected_medicine_name}:</h2>",
            unsafe_allow_html=True
        )
        for idx, medicine in enumerate(recommendations, start=1):
            # PharmEasy link
            pharmeasy_url = f"https://pharmeasy.in/search/all?name={medicine.replace(' ', '+')}"
            # Display medicine name with a "Click to Buy" button
            st.markdown(
                f"""
                <div class="medicine-box">
                    <div class="medicine-text">
                        {idx}. {medicine}
                    </div>
                    <div class="btn-container">
                        <a href="{pharmeasy_url}" target="_blank" style="text-decoration: none;">
                            <button>Click to Buy</button>
                        </a>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
    else:
        st.warning("Please select a medicine.")

# Footer with white font
st.markdown(
    """
    <div class="footer">
        <p>Created by Asmita Chavan</p>
    </div>
    """,
    unsafe_allow_html=True
)
