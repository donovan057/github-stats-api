from github_service import fetch_github_data
from svg_generator import generate_svg

def main():
    # 1. Récupère les données
    data = fetch_github_data("donovan057")

    # 2. Génère le SVG
    svg_content = generate_svg(data)

    # 3. Sauvegarde dans un fichier stats.svg
    with open("stats.svg", "w", encoding="utf-8") as f:
        f.write(svg_content)
    print("Fichier stats.svg généré avec succès !")

if __name__ == "__main__":
    main()