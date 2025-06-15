
import gdown

import os

import zipfile
import requests




folder = "chromadb"
file_id = "1_X2ZnuLuPsqSO2JGLbxQOY44T9JN85rB"
url = f"https://drive.google.com/uc?id={file_id}&export=download"
output_zip = "chromadb.zip"
destination = "chromadb1"



gdown.download(url, output=output_zip, quiet=False)


if not zipfile.is_zipfile(output_zip):
    raise Exception("❌ Le fichier téléchargé n'est pas un ZIP valide. Vérifie que le lien pointe bien vers un fichier .zip et non une page HTML.")

else:
# Décompression
    with zipfile.ZipFile(output_zip, "r") as zip_ref:
        zip_ref.extractall(destination)


