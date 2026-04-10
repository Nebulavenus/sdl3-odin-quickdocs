import os
import re
import json

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SDL3 Documentation (Odin & C)</title>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-tomorrow.min.css" rel="stylesheet" />
    <style>
        :root {
            --bg: #1a1a1a;
            --sidebar-bg: #2d2d2d;
            --text: #e0e0e0;
            --accent: #4fc3f7;
            --border: #444;
            --code-bg: #252525;
            --synth-bg: #1e3a5f;
        }
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            background: var(--bg);
            color: var(--text);
            margin: 0;
            display: flex;
            height: 100vh;
            overflow: hidden;
        }
        #sidebar {
            width: 350px;
            background: var(--sidebar-bg);
            border-right: 1px solid var(--border);
            display: flex;
            flex-direction: column;
        }
        #search-box {
            padding: 15px;
            background: var(--sidebar-bg);
            border-bottom: 1px solid var(--border);
        }
        #search-input {
            width: 100%;
            padding: 8px;
            border-radius: 4px;
            border: 1px solid var(--border);
            background: var(--bg);
            color: var(--text);
            box-sizing: border-box;
        }
        #categories {
            flex: 1;
            overflow-y: auto;
            padding: 10px;
        }
        .category {
            margin-bottom: 10px;
        }
        .category-name {
            font-weight: bold;
            color: var(--accent);
            cursor: pointer;
            padding: 5px;
            display: block;
        }
        .symbol-list {
            list-style: none;
            padding-left: 15px;
            display: none;
        }
        .symbol-list.active {
            display: block;
        }
        .symbol-item {
            padding: 3px 0;
            cursor: pointer;
            font-size: 0.9em;
            color: #bbb;
        }
        .symbol-item:hover {
            color: var(--text);
        }
        #content {
            flex: 1;
            overflow-y: auto;
            padding: 40px;
        }
        .symbol-detail {
            max-width: 1000px;
            margin: 0 auto;
        }
        h1 { color: var(--accent); margin-top: 0; }
        .tag {
            margin-bottom: 20px;
        }
        .tag-name {
            font-weight: bold;
            color: #81d4fa;
            text-transform: uppercase;
            font-size: 0.8em;
            margin-bottom: 5px;
        }
        .code-block {
            background: var(--code-bg);
            padding: 15px;
            border-radius: 6px;
            border: 1px solid var(--border);
            position: relative;
            overflow-x: auto;
            margin-bottom: 20px;
        }
        .code-lang {
            position: absolute;
            top: 5px;
            right: 10px;
            font-size: 0.7em;
            color: #666;
        }
        pre { margin: 0; }
        .description {
            line-height: 1.6;
            margin-bottom: 30px;
            font-size: 1.1em;
        }
        .param-table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 10px;
        }
        .param-table td {
            padding: 12px 8px;
            border-bottom: 1px solid var(--border);
            vertical-align: top;
        }
        .param-name { font-family: monospace; color: var(--accent); white-space: nowrap; width: 150px; }
        .synth-info {
            background: var(--synth-bg);
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 30px;
            border-left: 5px solid var(--accent);
        }
        .synth-info h1, .synth-info h2, .synth-info h3 { margin-top: 0; color: #fff; }
        blockquote {
            background: rgba(255,255,255,0.1);
            padding: 10px 20px;
            margin: 0;
            border-left: 3px solid #fff;
        }
        code:not([class*="language-"]) {
            background: rgba(255,255,255,0.1);
            padding: 2px 4px;
            border-radius: 3px;
            font-family: monospace;
        }
        .mermaid {
            background: white;
            padding: 10px;
            border-radius: 4px;
            margin: 20px 0;
        }
        .related-section {
            background: rgba(255,255,255,0.05);
            padding: 15px;
            border-radius: 6px;
            margin-top: 20px;
            border: 1px solid var(--border);
        }
        .related-list {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 8px;
            list-style: none;
            padding: 0;
            margin-top: 10px;
        }
        .api-link {
            color: var(--accent);
            text-decoration: none;
            cursor: pointer;
            font-size: 0.9em;
        }
        .api-link:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <div id="sidebar">
        <div id="search-box">
            <input type="text" id="search-input" placeholder="Search symbols...">
        </div>
        <div id="categories">
            <div class="category">
                <span class="category-name" onclick="showWelcome()">🏠 Overview</span>
            </div>
            <!-- Categories injected here -->
        </div>
    </div>
    <div id="content">
        <div id="welcome"></div>
        <div id="detail" style="display:none"></div>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-c.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/marked/4.3.0/marked.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
    <script>
        mermaid.initialize({ startOnLoad: false, theme: 'dark' });
        
        const renderer = new marked.Renderer();
        const oldCode = renderer.code.bind(renderer);
        renderer.code = function(code, lang, escaped) {
            if (lang === 'mermaid') return `<div class="mermaid">${code}</div>`;
            return oldCode(code, lang, escaped);
        };
        marked.setOptions({ renderer: renderer, gfm: true, breaks: true });

        const data = DOC_DATA;

        async function renderMermaid() {
            try { await mermaid.run(); } catch (e) { console.error(e); }
        }

        function showWelcome() {
            const welcome = document.getElementById('welcome');
            const detail = document.getElementById('detail');
            welcome.style.display = 'block';
            detail.style.display = 'none';
            if (data.extra_info['index']) {
                welcome.innerHTML = `<div class="symbol-detail">${marked.parse(data.extra_info['index'])}</div>`;
                setTimeout(renderMermaid, 50);
            }
            window.location.hash = '';
        }

        function renderSidebar() {
            const container = document.getElementById('categories');
            Object.keys(data.categories).sort().forEach(cat => {
                const div = document.createElement('div');
                div.className = 'category';
                div.innerHTML = `<span class="category-name">${cat}</span>
                    <ul class="symbol-list">
                        ${data.categories[cat].sort().map(s => `<li class="symbol-item" onclick="showSymbol('${s}')">${s}</li>`).join('')}
                    </ul>`;
                div.querySelector('.category-name').onclick = () => {
                    const list = div.querySelector('.symbol-list');
                    list.classList.toggle('active');
                    if (list.classList.contains('active')) showCategoryInfo(cat);
                };
                container.appendChild(div);
            });
        }

        function showCategoryInfo(cat) {
            const welcome = document.getElementById('welcome');
            const detail = document.getElementById('detail');
            welcome.style.display = 'none';
            detail.style.display = 'block';
            let synthHtml = data.extra_info[cat] ? `<div class="synth-info">${marked.parse(data.extra_info[cat])}</div>` : '';
            detail.innerHTML = `<div class="symbol-detail"><h1>Category: ${cat}</h1>${synthHtml}<p>Select a symbol from the sidebar to view details.</p></div>`;
            Prism.highlightAll();
            setTimeout(renderMermaid, 50);
        }

        function showSymbol(name) {
            const symbol = data.symbols[name];
            if (!symbol) return;
            document.getElementById('welcome').style.display = 'none';
            const detail = document.getElementById('detail');
            detail.style.display = 'block';

            let synthHtml = data.extra_info[name] ? `<div class="synth-info"><div class="tag-name">Synthesized Info</div>${marked.parse(data.extra_info[name])}</div>` : '';
            let tagsHtml = symbol.tags.description ? `<div class="description">${marked.parse(symbol.tags.description[0].replace(/\\\\n/g, '\\\\n'))}</div>` : '';
            
            if (symbol.tags.param) {
                tagsHtml += `<div class="tag"><div class="tag-name">Parameters</div><table class="param-table">` + 
                    symbol.tags.param.map(p => {
                        const s = p.indexOf(' ');
                        return `<tr><td class="param-name">${s === -1 ? p : p.substring(0,s)}</td><td>${s === -1 ? '' : marked.parse(p.substring(s+1))}</td></tr>`;
                    }).join('') + `</table></div>`;
            }

            let hierarchyHtml = '';
            if (symbol.type === 'struct' && data.hierarchy[name]) {
                const h = data.hierarchy[name];
                hierarchyHtml = `<div class="related-section">
                    <div class="tag-name">Functional API: ${name}</div>
                    ${h.creators.length ? `<div><b>Constructors:</b><ul class="related-list">${h.creators.map(c => `<li class="api-link" onclick="showSymbol('${c}')">${c}</li>`).join('')}</ul></div>` : ''}
                    ${h.methods.length ? `<div style="margin-top:15px"><b>Methods:</b><ul class="related-list">${h.methods.map(m => `<li class="api-link" onclick="showSymbol('${m}')">${m}</li>`).join('')}</ul></div>` : ''}
                    ${h.destructors.length ? `<div style="margin-top:15px"><b>Destructors:</b><ul class="related-list">${h.destructors.map(d => `<li class="api-link" onclick="showSymbol('${d}')">${d}</li>`).join('')}</ul></div>` : ''}
                </div>`;
            }

            detail.innerHTML = `
                <div class="symbol-detail">
                    <h1>${name}</h1>
                    ${synthHtml}
                    <div class="tag-name">Odin Declaration</div>
                    <div class="code-block"><span class="code-lang">Odin</span><pre><code class="language-odin">${symbol.odin_decl || 'Not bound'}</code></pre></div>
                    <div class="tag-name">C Declaration</div>
                    <div class="code-block"><span class="code-lang">C</span><pre><code class="language-c">${symbol.c_decl}</code></pre></div>
                    ${hierarchyHtml}
                    ${tagsHtml}
                </div>
            `;
            window.location.hash = name;
            Prism.highlightAll();
            setTimeout(renderMermaid, 50);
        }

        document.getElementById('search-input').oninput = (e) => {
            const query = e.target.value.toLowerCase();
            document.querySelectorAll('.symbol-item').forEach(item => {
                item.style.display = item.innerText.toLowerCase().includes(query) ? 'block' : 'none';
            });
        };

        renderSidebar();
        if (window.location.hash) {
            const n = window.location.hash.substring(1);
            if (data.symbols[n]) showSymbol(n); else showWelcome();
        } else showWelcome();
    </script>
</body>
</html>"""

class SDL3DocGen:
    def __init__(self, headers_dir, extra_dir):
        self.headers_dir = headers_dir
        self.extra_dir = extra_dir
        self.symbols = {}
        self.categories = {}
        self.extra_info = {}
        self.odin_symbols = {}
        self.hierarchy = {}

    def clean_type(self, t):
        return t.replace('const', '').replace('*', '').strip()

    def parse_doxygen(self, block):
        if not block: return {}
        tags = {"description": []}
        cur = "description"
        content = []
        for line in block.split('\n'):
            line = line.strip().lstrip('*').strip()
            m = re.match(r'\\(\w+)\s*(.*)', line)
            if m:
                if content:
                    if cur not in tags: tags[cur] = []
                    tags[cur].append("\\n".join(content).strip())
                cur, rem = m.groups()
                if cur not in tags: tags[cur] = []
                content = [rem] if rem else []
            else: content.append(line)
        if content:
            if cur not in tags: tags[cur] = []
            tags[cur].append("\\n".join(content).strip())
        return tags

    def extract_odin_symbols(self, content):
        for m in re.finditer(r'\b(\w+)\s*::\s*', content):
            name = m.group(1)
            if name in ['struct', 'enum', 'proc', 'if', 'for', 'switch']: continue
            rest = content[m.end():]
            search_rest = rest.lstrip()
            if not search_rest: continue
            decl = ""
            if search_rest.startswith('{') or any(search_rest.startswith(k) for k in ['struct', 'enum', 'proc']):
                brace, count, end = rest.find('{'), 0, 0
                if brace != -1 and (rest.find('---') == -1 or brace < rest.find('---')):
                    for i in range(brace, len(rest)):
                        if rest[i] == '{': count += 1
                        elif rest[i] == '}':
                            count -= 1
                            if count == 0:
                                end = i + 1
                                break
                    decl = rest[:end]
                else: decl = rest[:rest.find('\n')] if rest.find('\n') != -1 else rest
            else: decl = rest[:rest.find('\n')] if rest.find('\n') != -1 else rest
            prefix = ""
            back = content[:m.start()].split('\n')
            attrs = []
            for l in reversed(back[:-1]):
                if not l.strip(): continue
                if '@' in l: attrs.append(l)
                else: break
            if attrs: prefix = "\n".join(reversed(attrs)).strip() + "\n"
            self.odin_symbols[name] = (prefix + name + " :: " + decl).strip()

    def extract_c_symbols(self, content, filename):
        cat = re.search(r'# Category(\w+)', content)
        category = cat.group(1) if cat else filename.replace("SDL_", "").split('.')[0]
        for m in re.finditer(r'/\*\*(.*?)\*/\s*extern\s+SDL_DECLSPEC\s+(.*?)\s+SDLCALL\s+(SDL_\w+)\s*\((.*?)\);', content, re.DOTALL):
            doc, ret, name, args = m.groups()
            al = [self.clean_type(a.strip().split(' ')[0]) for a in args.split(',') if a.strip() and a.strip() != 'void']
            self.symbols[name] = {"name": name, "type": "function", "c_decl": f"{ret} {name}({args});", "tags": self.parse_doxygen(doc), "category": category, "ret_type": self.clean_type(ret), "args": al}
            if category not in self.categories: self.categories[category] = []
            self.categories[category].append(name)
        for m in re.finditer(r'/\*\*(.*?)\*/\s*typedef\s+struct\s+(SDL_\w+)\s*(?:\{(.*?)\})?\s*\2;', content, re.DOTALL):
            doc, name, body = m.groups()
            self.symbols[name] = {"name": name, "type": "struct", "c_decl": f"typedef struct {name} {{ ... }} {name};", "tags": self.parse_doxygen(doc), "category": category}
            if category not in self.categories: self.categories[category] = []
            self.categories[category].append(name)

    def run(self):
        for f in os.listdir(self.headers_dir):
            path = os.path.join(self.headers_dir, f)
            with open(path, 'r', encoding='utf-8') as file:
                if f.endswith('.odin'): self.extract_odin_symbols(file.read())
                elif f.endswith('.h'): self.extract_c_symbols(file.read(), f)
        for n, d in self.symbols.items():
            s = n.replace("SDL_", "")
            if s in self.odin_symbols: d["odin_decl"] = self.odin_symbols[s]
            elif n in self.odin_symbols: d["odin_decl"] = self.odin_symbols[n]
            else:
                for i in range(1, len(n.split('_'))):
                    sh = "_".join(n.split('_')[i:])
                    if sh in self.odin_symbols:
                        d["odin_decl"] = self.odin_symbols[sh]
                        break
        for n, d in self.symbols.items():
            if d['type'] == 'struct': self.hierarchy[n] = {"creators": [], "methods": [], "destructors": []}
        for n, d in self.symbols.items():
            if d['type'] == 'function':
                r, a = d.get('ret_type'), d.get('args', [])
                if r in self.hierarchy: self.hierarchy[r]["creators"].append(n)
                elif a and a[0] in self.hierarchy:
                    h = a[0]
                    if any(x in n for x in ["Destroy", "Free", "Close"]): self.hierarchy[h]["destructors"].append(n)
                    else: self.hierarchy[h]["methods"].append(n)
        if os.path.exists(self.extra_dir):
            for f in os.listdir(self.extra_dir):
                if f.endswith('.md'):
                    with open(os.path.join(self.extra_dir, f), 'r', encoding='utf-8') as file:
                        self.extra_info[f.replace('.md', '')] = file.read()
        out = {"categories": self.categories, "symbols": self.symbols, "extra_info": self.extra_info, "hierarchy": self.hierarchy}
        with open("sdl3_docs.html", "w", encoding="utf-8") as f:
            f.write(HTML_TEMPLATE.replace("DOC_DATA", json.dumps(out)))
        print(f"Generated sdl3_docs.html with {len(self.symbols)} symbols.")

if __name__ == "__main__":
    SDL3DocGen("Headers", "extra").run()
