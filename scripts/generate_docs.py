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
            width: 300px;
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
        <div id="welcome">
            <!-- index.md injected here -->
        </div>
        <div id="detail" style="display:none">
            <!-- Details injected here -->
        </div>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-c.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/marked/4.3.0/marked.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
    <script>
        mermaid.initialize({ startOnLoad: false, theme: 'dark' });
        
        // Custom renderer for marked
        const renderer = new marked.Renderer();
        const oldCode = renderer.code.bind(renderer);
        renderer.code = function(code, lang, escaped) {
            if (lang === 'mermaid') {
                return `<div class="mermaid">${code}</div>`;
            }
            return oldCode(code, lang, escaped);
        };
        marked.setOptions({ renderer: renderer, gfm: true, breaks: true });

        const data = DOC_DATA;

        async function renderMermaid() {
            try {
                await mermaid.run();
            } catch (e) {
                console.error("Mermaid error:", e);
            }
        }

        function showWelcome() {
            const welcome = document.getElementById('welcome');
            const detail = document.getElementById('detail');
            welcome.style.display = 'block';
            detail.style.display = 'none';
            
            if (data.extra_info['index']) {
                welcome.innerHTML = `<div class="symbol-detail">${marked.parse(data.extra_info['index'])}</div>`;
                setTimeout(renderMermaid, 50); // Small delay to ensure DOM is ready
            } else {
                welcome.innerHTML = `<div class="symbol-detail"><h1>SDL3 Documentation</h1><p>Select a category or symbol to view details.</p></div>`;
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
            
            let synthHtml = '';
            if (data.extra_info[cat]) {
                synthHtml = `<div class="synth-info">${marked.parse(data.extra_info[cat])}</div>`;
            }

            detail.innerHTML = `
                <div class="symbol-detail">
                    <h1>Category: ${cat}</h1>
                    ${synthHtml}
                    <p>Select a symbol from the sidebar to view its details.</p>
                </div>
            `;
            Prism.highlightAll();
            setTimeout(renderMermaid, 50);
        }

        function showSymbol(name) {
            const symbol = data.symbols[name];
            const welcome = document.getElementById('welcome');
            const detail = document.getElementById('detail');
            welcome.style.display = 'none';
            detail.style.display = 'block';

            let synthHtml = '';
            if (data.extra_info[name]) {
                synthHtml = `<div class="synth-info">
                    <div class="tag-name">Synthesized Info</div>
                    ${marked.parse(data.extra_info[name])}
                </div>`;
            }

            let tagsHtml = '';
            if (symbol.tags.description) {
                const desc = symbol.tags.description[0].replace(/\\\\n/g, '\\n');
                tagsHtml += `<div class="description">${marked.parse(desc)}</div>`;
            }

            if (symbol.tags.param) {
                tagsHtml += `<div class="tag"><div class="tag-name">Parameters</div>
                    <table class="param-table">
                        ${symbol.tags.param.map(p => {
                            const firstSpace = p.indexOf(' ');
                            if (firstSpace === -1) return `<tr><td class="param-name">${p}</td><td></td></tr>`;
                            const pname = p.substring(0, firstSpace);
                            const pdesc = p.substring(firstSpace + 1);
                            return `<tr><td class="param-name">${pname}</td><td>${marked.parse(pdesc)}</td></tr>`;
                        }).join('')}
                    </table>
                </div>`;
            }

            if (symbol.tags.returns) {
                tagsHtml += `<div class="tag"><div class="tag-name">Returns</div><div>${marked.parse(symbol.tags.returns[0])}</div></div>`;
            }

            if (symbol.tags.since) {
                tagsHtml += `<div class="tag"><div class="tag-name">Since</div><div>${symbol.tags.since[0]}</div></div>`;
            }

            detail.innerHTML = `
                <div class="symbol-detail">
                    <h1>${name}</h1>
                    ${synthHtml}
                    
                    <div class="tag-name">Odin Declaration</div>
                    <div class="code-block">
                        <span class="code-lang">Odin</span>
                        <pre><code class="language-odin">${symbol.odin_decl || 'Not bound in Odin'}</code></pre>
                    </div>

                    <div class="tag-name">C Declaration</div>
                    <div class="code-block">
                        <span class="code-lang">C</span>
                        <pre><code class="language-c">${symbol.c_decl}</code></pre>
                    </div>

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
                if (item.innerText.toLowerCase().includes(query)) {
                    item.style.display = 'block';
                    item.closest('.symbol-list').classList.add('active');
                } else {
                    item.style.display = 'none';
                }
            });
        };

        renderSidebar();
        if (window.location.hash) {
            const name = window.location.hash.substring(1);
            if (data.symbols[name]) {
                showSymbol(name);
            } else if (data.categories[name]) {
                showCategoryInfo(name);
            } else {
                showWelcome();
            }
        } else {
            showWelcome();
        }
    </script>
</body>
</html>"""

class SDL3DocGen:
    def __init__(self, headers_dir, extra_dir):
        self.headers_dir = headers_dir
        self.extra_dir = extra_dir
        self.symbols = {} # name -> data
        self.categories = {} # cat_name -> list of symbols
        self.extra_info = {} # name/cat -> md content
        self.odin_symbols = {} # name -> decl

    def parse_doxygen(self, block):
        if not block: return {}
        lines = block.split('\n')
        tags = {}
        current_tag = "description"
        tag_content = []
        for line in lines:
            line = line.strip().lstrip('*').strip()
            match = re.match(r'\\(\w+)\s*(.*)', line)
            if match:
                if tag_content:
                    tags[current_tag] = tags.get(current_tag, []) + ["\\n".join(tag_content).strip()]
                current_tag = match.group(1)
                remainder = match.group(2).strip()
                tag_content = [remainder] if remainder else []
            else:
                tag_content.append(line)
        if tag_content:
            tags[current_tag] = tags.get(current_tag, []) + ["\\n".join(tag_content).strip()]
        return tags

    def extract_c_symbols(self, content, filename):
        cat_match = re.search(r'# Category(\w+)', content)
        category = cat_match.group(1) if cat_match else os.path.splitext(filename)[0].replace("SDL_", "")
        
        func_pattern = r'/\*\*(.*?)\*/\s*extern\s+SDL_DECLSPEC\s+(.*?)\s+SDLCALL\s+(SDL_\w+)\s*\((.*?)\);'
        for m in re.finditer(func_pattern, content, re.DOTALL):
            doc, ret, name, args = m.groups()
            self.add_symbol(name, "function", doc, f"{ret} {name}({args});", category)

        enum_pattern = r'/\*\*(.*?)\*/\s*typedef\s+enum\s+(SDL_\w+)\s*\{(.*?)\}\s*\2;'
        for m in re.finditer(enum_pattern, content, re.DOTALL):
            doc, name, body = m.groups()
            self.add_symbol(name, "enum", doc, f"typedef enum {name} {{ {body.strip()} }} {name};", category)

        struct_pattern = r'/\*\*(.*?)\*/\s*typedef\s+struct\s+(SDL_\w+)\s*(?:\{(.*?)\})?\s*\2;'
        for m in re.finditer(struct_pattern, content, re.DOTALL):
            doc, name, body = m.groups()
            decl = f"typedef struct {name} {{ {body.strip() if body else ''} }} {name};"
            self.add_symbol(name, "struct", doc, decl, category)

        define_pattern = r'/\*\*(.*?)\*/\s*#define\s+(SDL_\w+)\s+(.*)'
        for m in re.finditer(define_pattern, content):
            doc, name, val = m.groups()
            self.add_symbol(name, "macro", doc, f"#define {name} {val.strip()}", category)

    def add_symbol(self, name, type, doc, decl, category):
        tags = self.parse_doxygen(doc)
        data = {
            "name": name, "type": type, "c_decl": decl.strip(),
            "tags": tags, "category": category, "odin_decl": None
        }
        self.symbols[name] = data
        if category not in self.categories: self.categories[category] = []
        self.categories[category].append(name)

    def extract_odin_symbols(self, content):
        matches = re.finditer(r'\b(\w+)\s*::\s*', content)
        for m in matches:
            name = m.group(1)
            if name in ['struct', 'enum', 'union', 'proc', 'foreign', 'import', 'package', 'if', 'when', 'else', 'for', 'switch', 'case', 'return', 'defer', 'using', 'cast', 'typeid']:
                continue
            
            start_pos = m.end()
            rest = content[start_pos:]
            search_rest = rest.lstrip()
            if not search_rest: continue
            
            decl = ""
            if search_rest.startswith('{') or any(search_rest.startswith(k) for k in ['struct', 'enum', 'union', 'proc']):
                first_brace = rest.find('{')
                first_dash = rest.find('---')
                if first_brace != -1 and (first_dash == -1 or first_brace < first_dash):
                    count, end_idx = 0, 0
                    for i in range(first_brace, len(rest)):
                        if rest[i] == '{': count += 1
                        elif rest[i] == '}':
                            count -= 1
                            if count == 0:
                                end_idx = i + 1
                                break
                    decl = rest[:end_idx]
                else:
                    end_line = rest.find('\n')
                    decl = rest[:end_line] if end_line != -1 else rest
            else:
                end_line = rest.find('\n')
                decl = rest[:end_line] if end_line != -1 else rest
            
            prefix = ""
            search_back = content[:m.start()].split('\n')
            attr_lines = []
            for line in reversed(search_back[:-1]):
                if not line.strip(): continue
                if '@' in line: attr_lines.append(line)
                else: break
            if attr_lines: prefix = "\n".join(reversed(attr_lines)).strip() + "\n"

            self.odin_symbols[name] = (prefix + name + " :: " + decl).strip()
            
            if "enum" in decl:
                enum_body = re.search(r'\{(.*?)\}', decl, re.DOTALL)
                if enum_body:
                    for member in re.findall(r'(\w+)\s*[=,]', enum_body.group(1)):
                        if member not in self.odin_symbols: self.odin_symbols[member] = f"(Member of enum {name})"

    def correlate(self):
        for sdl_name, data in self.symbols.items():
            stripped = sdl_name.replace("SDL_", "")
            if stripped in self.odin_symbols: data["odin_decl"] = self.odin_symbols[stripped]
            elif sdl_name in self.odin_symbols: data["odin_decl"] = self.odin_symbols[sdl_name]
            else:
                parts = sdl_name.split('_')
                for i in range(1, len(parts)):
                    short_name = "_".join(parts[i:])
                    if short_name in self.odin_symbols:
                        data["odin_decl"] = self.odin_symbols[short_name]
                        break

    def load_extra(self):
        if not os.path.exists(self.extra_dir): return
        for filename in os.listdir(self.extra_dir):
            if filename.endswith('.md'):
                name = os.path.splitext(filename)[0]
                with open(os.path.join(self.extra_dir, filename), 'r', encoding='utf-8') as f:
                    self.extra_info[name] = f.read()

    def run(self):
        for filename in os.listdir(self.headers_dir):
            if filename.endswith('.odin'):
                with open(os.path.join(self.headers_dir, filename), 'r', encoding='utf-8') as f:
                    self.extract_odin_symbols(f.read())
        for filename in os.listdir(self.headers_dir):
            if filename.endswith('.h'):
                with open(os.path.join(self.headers_dir, filename), 'r', encoding='utf-8') as f:
                    self.extract_c_symbols(f.read(), filename)
        self.correlate()
        self.load_extra()
        output_data = {
            "categories": self.categories, "symbols": self.symbols, "extra_info": self.extra_info
        }
        html = HTML_TEMPLATE.replace("DOC_DATA", json.dumps(output_data))
        with open("sdl3_docs.html", "w", encoding="utf-8") as f: f.write(html)
        print(f"Generated sdl3_docs.html with {len(self.symbols)} symbols.")

if __name__ == "__main__":
    gen = SDL3DocGen("Headers", "extra")
    gen.run()
