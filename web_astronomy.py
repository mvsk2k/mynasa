import streamlit as st
import requests

st.set_page_config(layout="wide")

# Prepare Api key and API Url
api_key = "D0uidDFXjuIaF3nXbH8eBeS94F4sok22R4xmL4id"
url1 = "https://api.nasa.gov/planetary/apod?" \
      f"api_key={api_key}"
url2 = "https://api.nasa.gov/EPIC/api/natural/images?" \
      f"api_key={api_key}"


def convertdateformt(dt):
    year = dt.split('-')[0]
    month = dt.split('-')[1]
    day = dt.split('-')[2][:2]
    ttl = year + "/" + month + "/" + day
    return ttl


def imagename(imagepart):
    image = imagepart + ".png"
    return image


nowdate = "2023/03/31"
epic = "epic_1b_20230331002712.png"

url3 = "https://epic.gsfc.nasa.gov/archive/natural/" \
       f"{nowdate}""/png/" \
       f"{epic}"

# Get the request data as  dictionary
response1 = requests.get(url1)
data = response1.json()

# Extract the Image title,url and Explanation
title = data["title"]
image_url = data['url']
explanation = data['explanation']

# Download the Image
image_filepath = 'image1.png'
response2 = requests.get(image_url)
with open (image_filepath, 'wb') as file:
    file.write(response2.content)

# Download the Earth Images details
response3 = requests.get(url2)
data2 = response3.json()
earthdata = len(data2)


#earthimage = ['earthimage1.png', 'earthimage2.png', 'earthimage3.png', 'earthimage4.png']


# Download the Earth Image

# EarthImage0
caption = data2[0]['caption']
imagepart = data2[0]['image']
dt1 = data2[0]['date']
img = imagename(imagepart)
dte = convertdateformt(dt1)
url3 = "https://epic.gsfc.nasa.gov/archive/natural/" \
       f"{dte}""/png/" \
       f"{img}"
resp2 = requests.get(url3)
with open ('earthimage1.png', 'wb') as file:
    file.write(resp2.content)


# EarthImage1
imagepart = data2[1]['image']
dt2 = data2[1]['date']
img = imagename(imagepart)
dte = convertdateformt(dt2)
url3 = "https://epic.gsfc.nasa.gov/archive/natural/" \
       f"{dte}""/png/" \
       f"{img}"
resp2 = requests.get(url3)
with open ("earthimage2.png", 'wb') as file:
    file.write(resp2.content)

# EarthImage2
imagepart = data2[2]['image']
dt3 = data2[2]['date']
img = imagename(imagepart)
dte = convertdateformt(dt3)
url3 = "https://epic.gsfc.nasa.gov/archive/natural/" \
       f"{dte}""/png/" \
       f"{img}"
resp2 = requests.get(url3)
with open ("earthimage3.png", 'wb') as file:
    file.write(resp2.content)

# EarthImage3
imagepart = data2[3]['image']
dt4 = data2[3]['date']
img = imagename(imagepart)
dte = convertdateformt(dt4)
url3 = "https://epic.gsfc.nasa.gov/archive/natural/" \
       f"{dte}""/png/" \
       f"{img}"
resp2 = requests.get(url3)
with open ("earthimage4.png", 'wb') as file:
    file.write(resp2.content)


st.write("WebApp from M V SIVAKUMAR using NASA APIs")

emptycontent = """

"""
st.title(title)

col1, col2 = st.columns(2)

with col1:
    st.image(image_filepath)

with col2:
    st.write(explanation)

st.write(emptycontent)
st.write(caption)

col3, col4 = st.columns(2)
with col3:
    st.image('earthimage1.png')
    st.write(dt1)

with col4:
    st.image('earthimage2.png')
    st.write(dt2)

st.write(emptycontent)

col5, col6 = st.columns(2)
with col5:
    st.image('earthimage3.png')
    st.write(dt3)

with col6:
    st.image('earthimage4.png')
    st.write(dt4)








