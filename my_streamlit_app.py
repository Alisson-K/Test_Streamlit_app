import streamlit as st
import pandas as pd
import seaborn as sns
from streamlit_lottie import st_lottie

def main():
    st.title('Hello Wilders, welcome to my application!')
    # Ajouter un loader 
    animation_path = "/Users/alisson/Desktop/Animation - 1714473007617.json"
    # Affichage de l'animation Lottie
    st_lottie(animation_path)

    st.write("I enjoy to discover stremalit possibilities")

if __name__ == "__main__":
    main()

# Afficher un df qu'on a eu dans les quêtes 
link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/weather2019.csv"
df_weather = pd.read_csv(link)
st.write(df_weather)

# Affichier un graphique 

st.line_chart(df_weather['MAX_TEMPERATURE_C'])

# Afficher un graphique Seaborn 
# 1. Créer une variable avec ton graphique dedans 
# 2. pour l'affichier st.pyplot(nom de la variable)

viz_correlation = sns.heatmap(df_weather.corr(), 
								center=0,
								cmap = sns.color_palette("vlag", as_cmap=True)
								)

st.pyplot(viz_correlation.figure)

# Application dynamique
# Exemple : faire des calculs avec un input

name = st.text_input("Please give me your name :")
name_length = len(name)
st.write("Your name has ",name_length,"characters")

# Intégrer musique fichier MP3

st.audio("https://ia804508.us.archive.org/20/items/keys-of-moon-the-epic-hero/KeysOfMoon-TheEpicHero.mp3", format="audio/mpeg", loop=True)

# Integrer video MP4 - La faire tourner en boucle 

video_file = open('/Users/alisson/Desktop/7989632-uhd_2160_4096_25fps.mp4', 'rb',)
video_bytes = video_file.read()

st.video(video_bytes, format='video/mp4', start_time=0, loop= True)





