import streamlit as st
import requests
import time

# Configuration du backend
BACKEND_URL = "http://localhost:8000"

st.title("📄 Générateur de questions à partir d'un PDF")

# Composant d'upload
uploaded_file = st.file_uploader("📂 Choisissez un fichier PDF", type=["pdf"])

# Sélection des types de questions
question_types = st.multiselect(
    "📌 Choisissez les types de questions :",
    ["MCQ", "Question-Réponse", "Oui/Non"],
    default=["MCQ"]  # Sélection par défaut
)
difficulty_level = st.radio(
    "📊 Choisissez le niveau de difficulté :",
    ("Facile", "Moyenne", "Difficile"),
    index=1  # Option par défaut
)
number_of_questions = st.number_input(
    "⏳ Nombre de questions à générer :",
    min_value=1,  # Min value
    max_value=10,  # Max value
    value=5,  # Default value
    step=1  # Step of 1
)

# Bouton d'envoi
if uploaded_file is not None and st.button("📤 Envoyer et générer des questions"):
    try:
        # Affichage de la barre de progression et du spinner pendant l'upload et le traitement
        with st.spinner("📤 Téléchargement et génération des questions..."):
            # Simuler un délai de traitement (peut être ajusté selon le temps réel d'upload)
            progress = st.progress(0)
            for percent_complete in range(100):
                time.sleep(0.05)  # Simule un petit délai pour la progression
                progress.progress(percent_complete + 1)

            # Envoi du fichier et des types de questions au backend
            response = requests.post(
                f"{BACKEND_URL}/generate-questions",
                files={"file": uploaded_file},
                data={"question_types": ",".join(question_types),
                      "difficulty_level": difficulty_level,
                      "num_questions": number_of_questions}  # Envoi sous forme de chaîne
            )

            # Vérification de la réponse
            if response.status_code == 200:
                data = response.json()
                if "questions" in data:
                    st.success("✅ Questions générées avec succès !")
                    questions = data["questions"]

                    # Affichage des questions générées sous forme de liste
                    for question in questions:
                        st.write(question)
                else:
                    st.error(data)
            else:
                st.error(f"🚨 Erreur {response.status_code} : {response.text}")

    except Exception as e:
        st.error(f"🚨 Échec de connexion : {str(e)}")