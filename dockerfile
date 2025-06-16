FROM python:3.12-slim

# répertoire de travail dans le conteneur

WORKDIR /app

# Copie des fichiers de requirements

COPY requirements.txt /app

# installer les dépendances 

ENV PIP_NO_REQUIRE_HASHES=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1

RUN pip cache purge



RUN pip install --no-cache-dir --no-deps --disable-pip-version-check -r requirements.txt

# Copie du code source dans le conteneur
COPY . /app

# commande pour exécuter l'application streamlit

CMD ["streamlit", "run", "rag_streamlit.py", "--server.port=8501","--reload-on-change"]