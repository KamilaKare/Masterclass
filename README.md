
# Masterclass sur l'IA Générative

Ce repo contient les codes utilisés lors des wébinaires sur l'IA générative.

-  [Session 1](https://github.com/KamilaKare/Masterclass/blob/main/Masterclass_1.ipynb) : Tokenization & embedding
-  [Session 2](https://github.com/KamilaKare/Masterclass/blob/main/Notebook_Masterclass_2.ipynb) : Agent RAG
-  [Session 2](https://github.com/KamilaKare/Masterclass/blob/main/views.py) : RAG encapsulé dans une application Streamlit
-  [Session 3](https://github.com/KamilaKare/Masterclass/blob/main/GenAI_Training_SFT.ipynb): Supervised Fine-tuning (Text to SQL)

## Session 2: Application RAG avec Streamlit

Pour cette session, le modèle RAG a été encapsulé dans une application Streamlit. Vous pouvez trouver le code de l'application [ici](https://github.com/KamilaKare/Masterclass/blob/main/app.py).

### Installation

1. **Installer les dépendances** :
   ```bash
   pip install -r requirements.txt
   ```

2. **Lancer l'application Streamlit** :
   ```bash
   streamlit run views.py
   ```

### Configuration

1. **Fichier `.env`** :
   Créez un fichier `.env` dans le répertoire de l'application et ajoutez votre clé API OpenAI.

2. **Utiliser Ollama comme Endpoint Local** :
   - Installez [Ollama](https://ollama.com/) sur votre PC.
   - Décommentez les lignes correspondantes dans le fichier `views.py` pour utiliser Ollama comme endpoint local pour votre RAG.



