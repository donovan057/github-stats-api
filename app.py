from flask import Flask, request, Response
import requests
from dotenv import load_dotenv
from github_service import fetch_github_data
from svg_generator import generate_svg

# Charge les variables cachées du fichier .env
load_dotenv()

# Initialisation du serveur Flask 
app = Flask(__name__)


    
# Création de la route API principale
@app.route('/api/stats')
def get_stats():
    # Paramètre dans l'URL: ?username=TonPseudo
    username = request.args.get('username')
    
    if not username:
        return "Erreur : Veuillez fournir un nom d'utilisateur dans l'URL (?username=TonPseudo)", 400
    
    try:
        data = fetch_github_data(username)
        svg_image = generate_svg(data)
        return Response(
            svg_image,
            mimetype='image/svg+xml',
            headers={'Cache-Control': 'public, max-age=7200'}
        )
        
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            return "Utilisateur introuvable", 404
        return f"Erreur API GitHub : {e.response.status_code}", 500
    except Exception as e:
        return f"Erreur interne du serveur : {str(e)}", 500
    
if __name__ == '__main__':
    # Lance le serveur localement sur le port 3000
    app.run(port=3000, debug=True)  