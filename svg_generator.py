def calculate_grade(repos: int, followers: int) -> str:
    """Calcule un grade basé sur l'activité GitHub."""
    score = (repos * 2) + (followers * 5)
    if score > 50: return "A+"
    if score > 20: return "A"
    return "B"

def generate_svg(data: dict) -> str:
    """Génère une carte SVG professionnelle style GitHub Dark Mode."""
    login = data.get("login", "Inconnu")
    public_repos = data.get("public_repos", 0)
    followers = data.get("followers", 0)
    following = data.get("following", 0)
    private_repos = data.get("total_private_repos", 0)
    
    grade = calculate_grade(public_repos, followers)
    
    # Palette de couleurs
    bg_color, border_color, title_color, text_color, icon_color = "#0D1117", "#30363D", "#58A6FF", "#C9D1D9", "#8B949E"
    
    return f"""
    <svg width="450" height="230" viewBox="0 0 450 230" fill="none" xmlns="http://www.w3.org/2000/svg">
        <style>
            .header {{ font: 600 18px 'Segoe UI', Ubuntu, sans-serif; fill: {title_color}; }}
            .stat-text {{ font: 400 14px 'Segoe UI', Ubuntu, sans-serif; fill: {text_color}; }}
            .stat-val {{ font: 600 14px 'Segoe UI', Ubuntu, sans-serif; fill: #FFFFFF; }}
            .bg {{ fill: {bg_color}; stroke: {border_color}; stroke-width: 1.5; rx: 6; }}
            .icon {{ fill: {icon_color}; }}
        </style>
        
        <rect class="bg" x="0.5" y="0.5" width="449" height="229" />
        <text x="25" y="35" class="header">{login}'s GitHub Stats</text>
        
        <g transform="translate(25, 65)">
            <path class="icon" d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 110-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8zM5 12.25v3.25a.25.25 0 00.4.2l1.45-1.087a.249.249 0 01.3 0L8.6 15.7a.25.25 0 00.4-.2v-3.25a.25.25 0 00-.25-.25h-3.5a.25.25 0 00-.25.25z" transform="scale(0.8)"/>
            <text x="25" y="12" class="stat-text">Public Repos:</text>
            <text x="180" y="12" class="stat-val">{public_repos}</text>
        </g>
        
        <g transform="translate(25, 100)">
            <path class="icon" d="M7 1h2a1 1 0 011 1v2H7V2a1 1 0 011-1zM6 2v2H4a1 1 0 00-1 1v6a1 1 0 001 1h8a1 1 0 001-1V5a1 1 0 00-1-1h-2V2a2 2 0 00-4 0z" transform="scale(0.8)"/>
            <text x="25" y="12" class="stat-text">Private Repos:</text>
            <text x="180" y="12" class="stat-val">{private_repos}</text>
        </g>
        
        <g transform="translate(25, 135)">
            <path class="icon" d="M5.5 3.5a2 2 0 100 4 2 2 0 000-4zM2 5.5a3.5 3.5 0 115.898 2.549 5.507 5.507 0 013.034 4.084.75.75 0 11-1.482.235 4.001 4.001 0 00-7.9 0 .75.75 0 01-1.482-.236A5.507 5.507 0 013.102 8.05 3.49 3.49 0 012 5.5zM11 4a.75.75 0 100 1.5 1.5 1.5 0 01.666 2.844.75.75 0 00-.416 1.336 5.526 5.526 0 013.208 2.739.75.75 0 101.32-.678 7.026 7.026 0 00-4.11-3.486 3 3 0 00-1.485-4.877zM4.5 15a.75.75 0 000-1.5.75.75 0 000 1.5z" transform="scale(0.8)"/>
            <text x="25" y="12" class="stat-text">Followers:</text>
            <text x="180" y="12" class="stat-val">{followers}</text>
        </g>
        
        <g transform="translate(25, 170)">
            <path class="icon" d="M8 .25a.75.75 0 01.673.418l1.882 3.815 4.21.612a.75.75 0 01.416 1.279l-3.046 2.97.719 4.192a.75.75 0 01-1.088.791L8 12.347l-3.766 1.98a.75.75 0 01-1.088-.79l.72-4.194L.818 6.374a.75.75 0 01.416-1.28l4.21-.611L7.327.668A.75.75 0 018 .25zm0 2.445L6.615 5.5a.75.75 0 01-.564.41l-3.097.45 2.24 2.184a.75.75 0 01.216.664l-.528 3.084 2.769-1.456a.75.75 0 01.698 0l2.77 1.456-.53-3.084a.75.75 0 01.216-.664l2.24-2.183-3.096-.45a.75.75 0 01-.564-.41L8 2.694v.001z" transform="scale(0.8)"/>
            <text x="25" y="12" class="stat-text">Following:</text>
            <text x="180" y="12" class="stat-val">{following}</text>
        </g>
        
        <g transform="translate(350, 100)">
            <circle cx="0" cy="0" r="35" fill="none" stroke="{border_color}" stroke-width="4"/>
            <circle cx="0" cy="0" r="35" fill="none" stroke="{title_color}" stroke-width="4" stroke-dasharray="140" stroke-linecap="round" transform="rotate(-90)"/>
            <text x="0" y="8" font-family="'Segoe UI', Ubuntu, sans-serif" font-size="24" font-weight="bold" fill="{title_color}" text-anchor="middle">{grade}</text>
        </g>  
    </svg>
    """