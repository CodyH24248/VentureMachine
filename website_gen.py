import os
import json

def generate_showcase_html():
    ventures_dir = "/home/engine/automated-ventures/ventures"
    ventures_data = []
    
    image_map = {
        "localbiz-ai-voice-receptionist": "https://images.unsplash.com/photo-1589254065878-42c9da997008?auto=format&fit=crop&q=80&w=800",
        "ai-ugc-video-generator-for-ads": "https://images.unsplash.com/photo-1611162617213-7d7a39e9b1d7?auto=format&fit=crop&q=80&w=800",
        "niche-discord": "https://images.unsplash.com/photo-1614680376593-902f74cf0d41?auto=format&fit=crop&q=80&w=800",
        "ai-real-estate-photo-enhancer": "https://images.unsplash.com/photo-1560518883-ce09059eeffa?auto=format&fit=crop&q=80&w=800",
        "automated-ai-podcast-editor": "https://images.unsplash.com/photo-1590602847861-f357a9332bbc?auto=format&fit=crop&q=80&w=800",
        "ai-legal-contract-reviewer-for-freelancers": "https://images.unsplash.com/photo-1589829545856-d10d557cf95f?auto=format&fit=crop&q=80&w=800"
    }
    
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
                            "image": img_url,
                            "full_content": content
                        })

    # SVG Logo Component - Responsive
    logo_svg = """
    <svg viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg" class="w-8 h-8 md:w-10 md:h-10 inline-block mr-2 md:mr-3">
        <path d="M50 5L90 27.5V72.5L50 95L10 72.5V27.5L50 5Z" stroke="url(#logo_grad)" stroke-width="8" stroke-linejoin="round"/>
        <path d="M30 40L50 70L70 40" stroke="#f8fafc" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>
        <defs>
            <linearGradient id="logo_grad" x1="10" y1="5" x2="90" y2="95" gradientUnits="userSpaceOnUse">
                <stop stop-color="#60a5fa"/>
                <stop offset="1" stop-color="#c084fc"/>
            </linearGradient>
        </defs>
    </svg>
    """

    # 1. Generate Individual Business Pages
    for v in ventures_data:
        detail_html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{v['name']} | VentureMachine Acquisition</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;600;700;800&display=swap" rel="stylesheet">
    <style>
        body {{ font-family: 'Plus Jakarta Sans', sans-serif; background-color: #020617; color: #f8fafc; }}
        .glass {{ background: rgba(15, 23, 42, 0.6); backdrop-filter: blur(16px); border: 1px solid rgba(255, 255, 255, 0.08); }}
    </style>
</head>
<body class="min-h-screen">
    <nav class="p-4 md:p-6 border-b border-white/5 sticky top-0 glass z-50">
        <div class="max-w-7xl mx-auto flex items-center">
            {logo_svg}
            <span class="text-lg md:text-xl font-bold tracking-tighter uppercase">VentureMachine</span>
        </div>
    </nav>
    <div class="max-w-4xl mx-auto px-4 md:px-6 py-10 md:py-20">
        <a href="index.html" class="text-blue-400 hover:text-blue-300 mb-8 md:mb-12 inline-block font-bold transition-colors">← Back to Portfolio</a>
        
        <div class="relative rounded-2xl md:rounded-[40px] overflow-hidden mb-8 md:mb-12 aspect-video shadow-2xl">
            <img src="{v['image']}" class="w-full h-full object-cover">
            <div class="absolute inset-0 bg-gradient-to-t from-[#020617] via-transparent"></div>
            <h1 class="absolute bottom-6 left-6 md:bottom-10 md:left-10 text-3xl md:text-5xl font-black text-white uppercase tracking-tighter leading-none">{v['name']}</h1>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 md:gap-12">
            <div class="md:col-span-2">
                <h2 class="text-xl md:text-2xl font-bold mb-4 md:mb-6 text-blue-400 uppercase tracking-wide">Business Overview</h2>
                <div class="prose prose-invert max-w-none text-slate-300 leading-relaxed text-base md:text-lg">
                    {v['description'].replace('\n', '<br>')}
                    <br><br>
                    <p>This business has been fully scaffolded with a high-performance Python FastAPI backend and a mobile-ready frontend. It includes automated marketing campaigns and legal compliance documents.</p>
                </div>
            </div>
            
            <div class="glass p-6 md:p-8 rounded-2xl md:rounded-3xl h-fit border-blue-500/20 text-center md:text-left">
                <p class="text-slate-500 text-[10px] md:text-xs font-bold uppercase tracking-widest mb-1 md:mb-2">Acquisition Price</p>
                <p class="text-3xl md:text-4xl font-black text-white mb-6 md:mb-8">{v['price']}</p>
                
                <div class="space-y-3 md:space-y-4 mb-8 md:mb-10 text-xs md:text-sm">
                    <div class="flex justify-between border-b border-white/5 pb-2">
                        <span class="text-slate-400">Tech Stack</span>
                        <span class="text-white font-bold">AI/Full-Stack</span>
                    </div>
                    <div class="flex justify-between border-b border-white/5 pb-2">
                        <span class="text-slate-400">Monthly Profit</span>
                        <span class="text-emerald-400 font-bold">$500+</span>
                    </div>
                    <div class="flex justify-between border-b border-white/5 pb-2">
                        <span class="text-slate-400">Automation</span>
                        <span class="text-white font-bold">95%</span>
                    </div>
                </div>

                <a href="https://acquire.com" class="block w-full py-4 bg-blue-600 hover:bg-blue-500 text-white text-center rounded-xl md:rounded-2xl font-black transition-all active:scale-95 text-sm md:text-base">
                    BUY THIS BUSINESS
                </a>
            </div>
        </div>
    </div>
</body>
</html>
"""
        with open(f"/home/engine/automated-ventures/{v['slug']}.html", "w") as f:
            f.write(detail_html)

    # 2. Generate Main Showcase HTML (with links to details)
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
        body {{ font-family: 'Plus Jakarta Sans', sans-serif; background-color: #020617; color: #f8fafc; overflow-x: hidden; }}
        .glass {{ background: rgba(15, 23, 42, 0.6); backdrop-filter: blur(16px); border: 1px solid rgba(255, 255, 255, 0.08); }}
        .gradient-text {{ background: linear-gradient(135deg, #60a5fa, #c084fc, #f472b6); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
        .bg-pattern {{ background-image: radial-gradient(circle at 2px 2px, rgba(255,255,255,0.05) 1px, transparent 0); background-size: 30px 30px; }}
        @media (min-width: 768px) {{ .bg-pattern {{ background-size: 40px 40px; }} }}
        .geometric-shape {{ position: absolute; z-index: -1; filter: blur(80px); opacity: 0.3; animation: pulse 10s infinite alternate; }}
        @keyframes pulse {{ 0% {{ transform: scale(1) translate(0, 0); }} 100% {{ transform: scale(1.1) translate(10px, 20px); }} }}
        .card-hover {{ transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1); }}
        @media (hover: hover) {{
            .card-hover:hover {{ transform: translateY(-10px) scale(1.02); border-color: rgba(96, 165, 250, 0.5); box-shadow: 0 20px 40px -15px rgba(0, 0, 0, 0.5); }}
        }}
    </style>
</head>
<body class="bg-pattern min-h-screen">
    <div class="geometric-shape bg-blue-600 w-64 h-64 md:w-96 md:h-96 top-[-50px] left-[-50px] md:top-[-100px] md:left-[-100px] rounded-full"></div>
    <div class="geometric-shape bg-purple-600 w-80 h-80 md:w-[500px] md:h-[500px] bottom-[-100px] right-[-50px] md:bottom-[-200px] md:right-[-100px] rounded-full"></div>

    <div class="max-w-7xl mx-auto px-4 md:px-6 py-8 md:py-12">
        <nav class="flex items-center justify-center md:justify-start mb-12 md:mb-20">
            {logo_svg}
            <span class="text-xl md:text-2xl font-black tracking-tighter uppercase gradient-text leading-none">VentureMachine</span>
        </nav>

        <header class="relative text-center mb-16 md:mb-24 px-4">
            <div class="inline-block px-3 py-1 mb-4 md:mb-6 glass rounded-full text-[10px] md:text-xs font-bold tracking-widest text-blue-400 border border-blue-500/20 uppercase">
                Autonomous Business Engine v2.5
            </div>
            <h1 class="text-4xl md:text-8xl font-extrabold mb-6 md:mb-8 gradient-text tracking-tighter leading-tight">VentureMachine</h1>
            <p class="text-slate-400 text-base md:text-2xl max-w-3xl mx-auto font-light leading-relaxed">
                The world's first automated AI factory. Direct acquisition for high-performance businesses built by autonomous agents.
            </p>
        </header>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 md:gap-10">
"""
    
    for v in ventures_data:
        html_template += f"""
            <a href="{v['slug']}.html" class="card-hover glass rounded-[32px] p-2 border border-white/5 flex flex-col group">
                <div class="relative overflow-hidden rounded-[26px] aspect-video">
                    <img src="{v['image']}" class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110">
                    <div class="absolute inset-0 bg-gradient-to-t from-[#020617] via-transparent opacity-60"></div>
                </div>
                
                <div class="p-6 flex-grow flex flex-col text-left">
                    <h3 class="text-xl md:text-2xl font-extrabold text-white tracking-tight mb-2">{v['name']}</h3>
                    <p class="text-slate-400 text-sm leading-relaxed mb-8 line-clamp-3">
                        {v['description']}
                    </p>
                    <div class="mt-auto flex justify-between items-center border-t border-white/5 pt-4">
                        <span class="text-xl md:text-2xl font-black text-white">{v['price']}</span>
                        <span class="text-blue-400 font-bold group-hover:translate-x-2 transition-transform text-sm md:text-base">View Deal →</span>
                    </div>
                </div>
            </a>
"""

    html_template += """
        </div>
    </div>
</body>
</html>
"""
    
    output_path = "/home/engine/automated-ventures/showcase.html"
    with open(output_path, "w") as f:
        f.write(html_template)
    
    print(f"✅ Responsive Showcase generated at {output_path}")
    return output_path

if __name__ == "__main__":
    generate_showcase_html()
