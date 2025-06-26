FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt /app/
COPY wheelhouse /app/wheelhouse



# Installer les paquets à partir du dossier local
RUN pip install --no-cache-dir --find-links=/app/wheelhouse -r requirements.txt

# Téléchargement du modèle à la construction de l'image
RUN python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('sentence-transformers/all-mpnet-base-v2')"




# Copier le reste du code source dans le conteneur
COPY . /app

# Commande pour exécuter l'application Streamlit
CMD ["streamlit", "run", "rag_streamlit.py", "--server.port=8501"]












