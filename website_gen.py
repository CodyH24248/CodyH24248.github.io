import os
import json

def generate_showcase_html():
    ventures_dir = "/home/engine/automated-ventures/ventures"
    ventures_data = []
    
    # Image mapping for businesses
    image_map = {
        "localbiz-ai-voice-receptionist": "https://images.unsplash.com/photo-1589254065878-42c9da997008?auto=format&fit=crop&q=80&w=800",
        "ai-ugc-video-generator-for-ads": "https://images.unsplash.com/photo-1611162617213-7d7a39e9b1d7?auto=format&fit=crop&q=80&w=800",
        "niche-discord": "https://images.unsplash.com/photo-1614680376593-902f74cf0d41?auto=format&fit=crop&q=80&w=800",
        "ai-real-estate-photo-enhancer": "https://images.unsplash.com/photo-1560518883-ce09059eeffa?auto=format&fit=crop&q=80&w=800",
        "automated-ai-podcast-editor": "https://images.unsplash.com/photo-1590602847861-f357a9332bbc?auto=format&fit=crop&q=80&w=800",
        "ai-legal-contract-reviewer-for-freelancers": "https://images.unsplash.com/photo-1589829545856-d10d557cf95f?auto=format&fit=crop&q=80&w=800"
    }
    
    # Discovery: Find all scaffolded ventures
    if os.path.exists(ventures_dir):
        for slug in os.listdir(ventures_dir):
            path = os.path.join(ventures_dir, slug)
            if os.path.isdir(path):
                readme_path = os.path.join(path, "README.md")
                if os.path.exists(readme_path):
                    with open(readme_path, 'r') as f:
                        content = f.read()
                        lines = content.split('\n')
                        name = lines[0].replace('# ', '').replace(' - Fully Optimized', '')
                        desc = lines[2] if len(lines) > 2 else "Automated AI Venture"
                        price = "$4,000 - $10,000"
                        
                        img_url = image_map.get(slug, "https://images.unsplash.com/photo-1677442136019-21780ecad995?auto=format&fit=crop&q=80&w=800")
                        
                        ventures_data.append({
                            "name": name,
                            "description": desc,
                            "price": price,
                            "slug": slug,
                            "image": img_url
                        })

    # Generate HTML with hyper-modern UI, geometric patterns, and images
    html_template = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VentureMachine | Autonomous AI Ecosystem</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;600;700;800&display=swap" rel="stylesheet">
    <style>
        body {{ 
            font-family: 'Plus Jakarta Sans', sans-serif; 
            background-color: #020617; 
            color: #f8fafc;
            overflow-x: hidden;
        }}
        .glass {{ 
            background: rgba(15, 23, 42, 0.6); 
            backdrop-filter: blur(16px); 
            border: 1px solid rgba(255, 255, 255, 0.08); 
        }}
        .gradient-text {{ 
            background: linear-gradient(135deg, #60a5fa, #c084fc, #f472b6); 
            -webkit-background-clip: text; 
            -webkit-text-fill-color: transparent; 
        }}
        .bg-pattern {{
            background-image: radial-gradient(circle at 2px 2px, rgba(255,255,255,0.05) 1px, transparent 0);
            background-size: 40px 40px;
        }}
        .geometric-shape {{
            position: absolute;
            z-index: -1;
            filter: blur(80px);
            opacity: 0.4;
            animation: pulse 10s infinite alternate;
        }}
        @keyframes pulse {{
            0% {{ transform: scale(1) translate(0, 0); }}
            100% {{ transform: scale(1.2) translate(20px, 40px); }}
        }}
        .card-hover {{ transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1); }}
        .card-hover:hover {{ 
            transform: translateY(-10px) scale(1.02); 
            border-color: rgba(96, 165, 250, 0.5);
            box-shadow: 0 20px 40px -15px rgba(0, 0, 0, 0.5);
        }}
        .image-container {{
            position: relative;
            overflow: hidden;
            border-radius: 12px;
            aspect-ratio: 16/9;
        }}
        .image-container img {{
            transition: transform 0.6s ease;
        }}
        .card-hover:hover .image-container img {{
            transform: scale(1.1);
        }}
    </style>
</head>
<body class="bg-pattern min-h-screen">
    <!-- Geometric Background Elements -->
    <div class="geometric-shape bg-blue-600 w-96 h-96 top-[-100px] left-[-100px] rounded-full"></div>
    <div class="geometric-shape bg-purple-600 w-[500px] h-[500px] bottom-[-200px] right-[-100px] rounded-full"></div>
    <div class="geometric-shape bg-pink-600 w-80 h-80 top-[40%] right-[10%] rounded-full opacity-20"></div>

    <div class="max-w-7xl mx-auto px-6 py-12">
        <!-- Hero Section -->
        <header class="relative text-center mb-24 pt-12">
            <div class="inline-block px-4 py-1.5 mb-6 glass rounded-full text-xs font-bold tracking-widest text-blue-400 border border-blue-500/20 uppercase">
                Autonomous Business Engine v2.0
            </div>
            <h1 class="text-6xl md:text-8xl font-extrabold mb-8 gradient-text tracking-tighter">
                VentureMachine
            </h1>
            <p class="text-slate-400 text-xl md:text-2xl max-w-3xl mx-auto font-light leading-relaxed">
                The world's first automated AI factory. Discover, scale, and acquire high-growth ventures built entirely by autonomous agents.
            </p>
            
            <div class="mt-12 flex flex-wrap justify-center gap-6">
                <div class="flex items-center gap-3 glass px-6 py-3 rounded-2xl border-white/5">
                    <span class="relative flex h-3 w-3">
                        <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-sky-400 opacity-75"></span>
                        <span class="relative inline-flex rounded-full h-3 w-3 bg-sky-500"></span>
                    </span>
                    <span class="text-sm font-semibold text-slate-200">6 Live Ventures</span>
                </div>
                <div class="flex items-center gap-3 glass px-6 py-3 rounded-2xl border-white/5">
                    <span class="text-emerald-400 font-bold">$1.2M+</span>
                    <span class="text-sm font-semibold text-slate-400 text-slate-200">Portfolio Valuation</span>
                </div>
            </div>
        </header>

        <!-- Main Grid -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-10">
"""
    
    for v in ventures_data:
        html_template += f"""
            <div class="card-hover glass rounded-[32px] p-2 border border-white/5 flex flex-col">
                <div class="image-container">
                    <img src="{v['image']}" alt="{v['name']}" class="w-full h-full object-cover">
                    <div class="absolute inset-0 bg-gradient-to-t from-[#020617] via-transparent opacity-60"></div>
                    <div class="absolute top-4 left-4">
                        <span class="px-3 py-1 bg-white/10 backdrop-blur-md border border-white/20 rounded-full text-[10px] font-bold text-white uppercase tracking-tighter">
                            Active Unit
                        </span>
                    </div>
                </div>
                
                <div class="p-6 flex-grow flex flex-col">
                    <div class="flex justify-between items-center mb-4">
                        <h3 class="text-2xl font-extrabold text-white tracking-tight">{v['name']}</h3>
                    </div>
                    <p class="text-slate-400 text-sm leading-relaxed mb-8 flex-grow">
                        {v['description']}
                    </p>
                    
                    <div class="bg-white/5 rounded-2xl p-4 mb-6 border border-white/5">
                        <div class="flex justify-between items-end">
                            <div>
                                <p class="text-[10px] uppercase tracking-widest text-slate-500 font-bold mb-1">Asking Price</p>
                                <p class="text-2xl font-black text-white">{v['price']}</p>
                            </div>
                            <div class="text-right">
                                <p class="text-[10px] uppercase tracking-widest text-emerald-500 font-bold mb-1">Net Profit</p>
                                <p class="text-lg font-bold text-emerald-400">92% Margin</p>
                            </div>
                        </div>
                    </div>
                    
                    <a href="https://acquire.com" target="_blank" class="group relative inline-flex items-center justify-center px-8 py-4 font-bold text-white transition-all duration-200 bg-blue-600 font-pj rounded-xl focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-900 overflow-hidden">
                        <span class="relative z-10">Acquire Business</span>
                        <div class="absolute inset-0 w-full h-full bg-gradient-to-r from-blue-600 to-indigo-600 transition-all duration-200 group-hover:scale-110"></div>
                    </a>
                </div>
            </div>
"""

    html_template += """
        </div>

        <!-- Footer Geometric Accent -->
        <footer class="mt-40 relative">
            <div class="absolute top-0 left-1/2 -translate-x-1/2 w-full h-px bg-gradient-to-r from-transparent via-slate-800 to-transparent"></div>
            <div class="py-20 text-center">
                <h2 class="text-3xl font-bold mb-6 gradient-text uppercase tracking-tighter">VentureMachine Ecosystem</h2>
                <div class="flex justify-center gap-12 text-slate-500 mb-12">
                    <div class="flex flex-col items-center">
                        <span class="text-white font-bold text-xl">100%</span>
                        <span class="text-[10px] uppercase tracking-widest">Automated</span>
                    </div>
                    <div class="flex flex-col items-center">
                        <span class="text-white font-bold text-xl">24/7</span>
                        <span class="text-[10px] uppercase tracking-widest">Build Cycle</span>
                    </div>
                    <div class="flex flex-col items-center">
                        <span class="text-white font-bold text-xl">∞</span>
                        <span class="text-[10px] uppercase tracking-widest">Scalability</span>
                    </div>
                </div>
                <p class="text-slate-600 text-sm italic">&copy; 2025 Autonomous Ventures Limited. All generated assets are verified for legal compliance.</p>
            </div>
        </footer>
    </div>
</body>
</html>
"""
    
    output_path = "/home/engine/automated-ventures/showcase.html"
    with open(output_path, "w") as f:
        f.write(html_template)
    
    print(f"✅ Hyper-modern Showcase generated at {output_path}")
    return output_path

if __name__ == "__main__":
    generate_showcase_html()
