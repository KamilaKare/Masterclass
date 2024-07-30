Ce repo contient les codes utilisés lors des wébinaires sur l'IA générative.

-  [Session 1](https://github.com/KamilaKare/Masterclass/blob/main/Masterclass_1.ipynb) : Tokenization & embedding
-  [Session 2](https://github.com/KamilaKare/Masterclass/blob/main/Notebook_Masterclass_2.ipynb) Agent RAG
-  [Session 2](https://github.com/KamilaKare/Masterclass/blob/main/views.py)  RAG
-  Session 3:

Pour la session 2, le RAG ([rag](https://github.com/KamilaKare/Masterclass/blob/main/views.py)) a été encapsulé dans une application streamlit ([app](https://github.com/KamilaKare/Masterclass/blob/main/views.py)). Installer les dépendances disponibles dans le fichier requirements.txt et exécuter la commande 
streamlit run views.py afin de lancer l'application. 

Vous devriez aussi créer un fichier .env qui contiendra votre clé api openai. Sinon, vous pouvez installer [ollama](https://ollama.com/) sur votre pc afin de disposer d'un endpoint local qui alimentera votre RAG. Dans ce cas d'espèce, il faudra décommenter dans le fichier views.py les lignes faisant appel à Ollama.  

Voici une version reformulée de votre `README.md` pour la session 2 :

---

## Session 2

Pour cette session, le modèle RAG a été encapsulé dans une application Streamlit. Vous pouvez trouver le code de l'application [ici](https://github.com/KamilaKare/Masterclass/blob/main/views.py).

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

---
