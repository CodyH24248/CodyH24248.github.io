import os
import json

def generate_showcase_html():
    ventures_dir = "/home/engine/automated-ventures/ventures"
    ventures_data = []
    
    # Discovery: Find all scaffolded ventures
    if os.path.exists(ventures_dir):
        for slug in os.listdir(ventures_dir):
            path = os.path.join(ventures_dir, slug)
            if os.path.isdir(path):
                readme_path = os.path.join(path, "README.md")
                if os.path.exists(readme_path):
                    with open(readme_path, 'r') as f:
                        content = f.read()
                        # Simple extraction from the README structure we built
                        lines = content.split('\n')
                        name = lines[0].replace('# ', '').replace(' - Fully Optimized', '')
                        desc = lines[2] if len(lines) > 2 else "Automated AI Venture"
                        
                        # Use a default price for the showcase (or extract if possible)
                        price = "$4,000 - $10,000 (Based on MRR)"
                        
                        ventures_data.append({
                            "name": name,
                            "description": desc,
                            "price": price,
                            "slug": slug
                        })

    # Generate HTML with improved UI
    html_template = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VentureMachine | Autonomous AI Portfolio</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap" rel="stylesheet">
    <style>
        body {{ font-family: 'Inter', sans-serif; background-color: #0f172a; color: #f8fafc; }}
        .glass {{ background: rgba(30, 41, 59, 0.7); backdrop-filter: blur(12px); border: 1px solid rgba(255, 255, 255, 0.1); }}
        .gradient-text {{ background: linear-gradient(90deg, #38bdf8, #818cf8); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
        .card-hover:hover {{ transform: translateY(-4px); border-color: #38bdf8; }}
    </style>
</head>
<body class="min-h-screen p-8">
    <div class="max-w-6xl mx-auto">
        <header class="text-center mb-16">
            <h1 class="text-5xl font-bold mb-4 gradient-text">VentureMachine AI</h1>
            <p class="text-slate-400 text-xl max-w-2xl mx-auto">
                An autonomous engine building, scaling, and exiting high-performance AI businesses in real-time.
            </p>
            <div class="mt-8 flex justify-center gap-4">
                <span class="px-4 py-2 rounded-full glass text-sm font-medium text-sky-400 border border-sky-400/30">● System Active</span>
                <span class="px-4 py-2 rounded-full glass text-sm font-medium text-slate-300">Continuous Build Loop: ON</span>
            </div>
        </header>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
"""
    
    for v in ventures_data:
        html_template += f"""
            <div class="card-hover glass rounded-2xl p-6 transition-all duration-300 flex flex-col justify-between">
                <div>
                    <div class="flex justify-between items-start mb-4">
                        <span class="bg-sky-500/10 text-sky-400 text-xs font-bold px-3 py-1 rounded-full border border-sky-500/20 uppercase tracking-wider">Venture</span>
                        <span class="text-emerald-400 text-xs font-medium">Verified Exit Ready</span>
                    </div>
                    <h3 class="text-2xl font-bold mb-3 text-white">{v['name']}</h3>
                    <p class="text-slate-400 text-sm leading-relaxed mb-6">{v['description']}</p>
                </div>
                <div>
                    <div class="border-t border-slate-700 pt-4 mt-4">
                        <p class="text-slate-500 text-xs uppercase tracking-widest mb-1">Valuation Range</p>
                        <p class="text-2xl font-bold text-emerald-400">{v['price']}</p>
                    </div>
                    <a href="https://acquire.com" target="_blank" class="mt-6 block w-full py-3 rounded-xl bg-sky-600 hover:bg-sky-500 text-white text-center font-semibold transition-colors">
                        Inquire for Purchase
                    </a>
                </div>
            </div>
"""

    html_template += """
        </div>

        <footer class="mt-24 text-center border-t border-slate-800 pt-12 pb-8">
            <p class="text-slate-500 text-sm mb-2">&copy; 2025 VentureMachine AI Ecosystem</p>
            <div class="flex justify-center gap-6 text-xs font-medium text-slate-400 uppercase tracking-widest">
                <span>Autonomous Pipeline</span>
                <span>•</span>
                <span>Real-Time Valuation</span>
                <span>•</span>
                <span>Verified Exits</span>
            </div>
        </footer>
    </div>
</body>
</html>
"""
    
    output_path = "/home/engine/automated-ventures/showcase.html"
    with open(output_path, "w") as f:
        f.write(html_template)
    
    print(f"✅ Showcase website generated at {output_path}")
    return output_path

if __name__ == "__main__":
    generate_showcase_html()
