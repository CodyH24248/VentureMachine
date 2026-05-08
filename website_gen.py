import os
import json

def generate_showcase_html():
    ventures_dir = "/home/engine/automated-ventures/ventures"
    ventures_data = []
    
    image_map = {
        "localbiz-ai-voice-receptionist": "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?auto=format&fit=crop&q=80&w=1200",
        "ai-ugc-video-generator-for-ads": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&q=80&w=1200",
        "niche-discord": "https://images.unsplash.com/photo-1552664730-d307ca884978?auto=format&fit=crop&q=80&w=1200",
        "ai-real-estate-photo-enhancer": "https://images.unsplash.com/photo-1582408921715-18e7806367c1?auto=format&fit=crop&q=80&w=1200",
        "automated-ai-podcast-editor": "https://images.unsplash.com/photo-1478737270239-2f02b77fc618?auto=format&fit=crop&q=80&w=1200",
        "ai-legal-contract-reviewer-for-freelancers": "https://images.unsplash.com/photo-1450101499163-c8848c66ca85?auto=format&fit=crop&q=80&w=1200"
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
                        
                        img_url = image_map.get(slug, "https://images.unsplash.com/photo-1677442136019-21780ecad995?auto=format&fit=crop&q=80&w=1200")
                        
                        ventures_data.append({
                            "name": name,
                            "description": desc,
                            "price": price,
                            "slug": slug,
                            "image": img_url
                        })

    # Shared Styles & Head - Ultra Clean Elite
    shared_head = """
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        :root { --accent: #2563eb; }
        body { font-family: 'Plus Jakarta Sans', sans-serif; background-color: #ffffff; color: #0f172a; -webkit-font-smoothing: antialiased; }
        .hero-gradient { background: radial-gradient(circle at 50% 50%, rgba(37, 99, 235, 0.03) 0%, rgba(255, 255, 255, 1) 70%); }
        .animate-reveal { animation: reveal 1.2s cubic-bezier(0.16, 1, 0.3, 1) forwards; }
        @keyframes reveal { from { opacity: 0; transform: translateY(40px); } to { opacity: 1; transform: translateY(0); } }
        .venture-card { transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1); border: 1px solid #f1f5f9; }
        .venture-card:hover { transform: translateY(-8px); border-color: #2563eb; box-shadow: 0 30px 60px -12px rgba(15, 23, 42, 0.12); }
    </style>
    """

    # Logo Component
    logo_svg = """
    <svg width="48" height="48" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg" class="mx-auto">
        <path d="M50 10L90 32.5V67.5L50 90L10 67.5V32.5L50 10Z" stroke="#2563eb" stroke-width="10" stroke-linejoin="round"/>
        <path d="M30 45L50 70L70 45" stroke="#2563eb" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/>
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
    <title>{v['name']} | VentureMachine</title>
    {shared_head}
</head>
<body>
    <nav class="py-8 border-b border-slate-100 sticky top-0 bg-white/80 backdrop-blur-md z-50">
        <div class="max-w-7xl mx-auto px-6 flex justify-between items-center">
            <a href="index.html" class="flex items-center gap-3">
                <svg width="24" height="24" viewBox="0 0 100 100" fill="none"><path d="M50 10L90 32.5V67.5L50 90L10 67.5V32.5L50 10Z" stroke="#2563eb" stroke-width="12" stroke-linejoin="round"/></svg>
                <span class="text-sm font-extrabold uppercase tracking-widest text-slate-900">VentureMachine</span>
            </a>
            <a href="index.html" class="text-xs font-bold text-slate-400 hover:text-blue-600 uppercase tracking-widest transition-colors">Portfolio</a>
        </div>
    </nav>

    <main class="max-w-5xl mx-auto px-6 py-24">
        <div class="animate-reveal">
            <div class="mb-12">
                <span class="inline-block px-3 py-1 bg-blue-50 text-blue-600 text-[10px] font-black uppercase tracking-widest rounded-full mb-6">Autonomous Asset</span>
                <h1 class="text-5xl md:text-7xl font-extrabold tracking-tighter text-slate-900 mb-8">{v['name']}</h1>
                <p class="text-xl text-slate-500 max-w-2xl leading-relaxed mb-12">{v['description']}</p>
            </div>

            <div class="rounded-3xl overflow-hidden shadow-2xl mb-24 aspect-video">
                <img src="{v['image']}" class="w-full h-full object-cover">
            </div>

            <div class="grid grid-cols-1 md:grid-cols-3 gap-12 border-t border-slate-100 pt-24">
                <div class="md:col-span-2">
                    <h2 class="text-2xl font-bold mb-8">Acquisition Overview</h2>
                    <div class="prose prose-slate text-slate-600 leading-relaxed space-y-6">
                        <p>This venture represents a turnkey AI solution, meticulously engineered for scalability and autonomous operation. Every component, from the backend infrastructure to the market positioning, has been optimized by the VentureMachine engine.</p>
                        <p>Purchasing this asset includes full transfer of codebases, documentation, deployment scripts, and operational training modules.</p>
                    </div>
                </div>
                <div>
                    <div class="bg-slate-50 p-8 rounded-3xl border border-slate-100">
                        <p class="text-[10px] font-black text-slate-400 uppercase tracking-widest mb-2">Asking Valuation</p>
                        <p class="text-4xl font-black text-slate-900 mb-8">{v['price']}</p>
                        <a href="https://acquire.com" class="block w-full py-4 bg-blue-600 text-white text-center rounded-xl font-bold hover:bg-blue-700 transition-all">Acquire Venture</a>
                        <p class="text-[10px] text-center text-slate-400 mt-6 font-medium">Closing handled via Acquire.com Escrow</p>
                    </div>
                </div>
            </div>
        </div>
    </main>
</body>
</html>
"""
        with open(f"/home/engine/automated-ventures/{v['slug']}.html", "w") as f:
            f.write(detail_html)

    # 2. Main Portfolio - Centered Elite Branding
    html_template = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VentureMachine | Accredited AI Startup Studio</title>
    {shared_head}
</head>
<body class="hero-gradient">
    <header class="pt-32 pb-40 px-6">
        <div class="max-w-4xl mx-auto text-center animate-reveal">
            {logo_svg}
            <h1 class="text-sm font-black uppercase tracking-[0.4em] text-blue-600 mb-12 mt-6">VentureMachine</h1>
            <h2 class="text-6xl md:text-8xl font-extrabold tracking-tighter text-slate-900 leading-[0.95] mb-12">
                The institutional engine for AI ventures.
            </h2>
            <p class="text-xl md:text-2xl text-slate-500 max-w-2xl mx-auto font-medium leading-relaxed mb-16">
                An autonomous factory building, scaling, and exiting profitable AI enterprises at scale.
            </p>
            <div class="flex justify-center items-center gap-12 grayscale opacity-40">
                <span class="font-black tracking-widest text-xs">AUTONOMOUS</span>
                <span class="font-black tracking-widest text-xs">SCALABLE</span>
                <span class="font-black tracking-widest text-xs">ACCREDITED</span>
            </div>
        </div>
    </header>

    <section id="portfolio" class="bg-white py-32 border-t border-slate-50">
        <div class="max-w-7xl mx-auto px-6">
            <div class="mb-24 flex justify-between items-end">
                <div>
                    <h3 class="text-xs font-black uppercase tracking-widest text-blue-600 mb-4">Investment Portfolio</h3>
                    <h4 class="text-4xl font-extrabold text-slate-900 tracking-tight">Active Ventures</h4>
                </div>
                <div class="hidden md:block">
                    <p class="text-sm font-bold text-slate-400">Showing 6 High-Growth Assets</p>
                </div>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-12">
"""
    
    for v in ventures_data:
        html_template += f"""
                <a href="{v['slug']}.html" class="venture-card group bg-white p-4 rounded-[40px] flex flex-col">
                    <div class="relative rounded-[32px] overflow-hidden aspect-square mb-10">
                        <img src="{v['image']}" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110">
                    </div>
                    <div class="px-4 pb-4 flex-grow flex flex-col">
                        <h5 class="text-2xl font-bold text-slate-900 tracking-tight mb-4 group-hover:text-blue-600 transition-colors">{v['name']}</h5>
                        <p class="text-slate-500 text-sm leading-relaxed mb-10 line-clamp-2">{v['description']}</p>
                        <div class="mt-auto pt-6 border-t border-slate-50 flex justify-between items-center">
                            <span class="text-lg font-black text-slate-900">{v['price']}</span>
                            <span class="w-8 h-8 rounded-full bg-slate-50 flex items-center justify-center group-hover:bg-blue-600 group-hover:text-white transition-all">
                                <svg width="16" height="16" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M14 5l7 7m0 0l-7 7m7-7H3" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
                            </span>
                        </div>
                    </div>
                </a>
"""

    html_template += """
            </div>
        </div>
    </section>

    <footer class="py-32 bg-slate-50 border-t border-slate-100">
        <div class="max-w-7xl mx-auto px-6 text-center">
            <div class="mb-12">
                <svg width="32" height="32" viewBox="0 0 100 100" fill="none" class="mx-auto opacity-20"><path d="M50 10L90 32.5V67.5L50 90L10 67.5V32.5L50 10Z" stroke="#000" stroke-width="12"/></svg>
            </div>
            <p class="text-slate-400 text-xs font-bold uppercase tracking-[0.4em] mb-4">&copy; 2025 VentureMachine</p>
            <p class="text-slate-300 text-[10px] max-w-sm mx-auto leading-loose">
                Proprietary autonomous venture infrastructure. All assets performance-verified by internal audit protocols.
            </p>
        </div>
    </footer>
</body>
</html>
"""
    
    output_path = "/home/engine/automated-ventures/showcase.html"
    with open(output_path, "w") as f:
        f.write(html_template)
    
    return output_path

if __name__ == "__main__":
    generate_showcase_html()
