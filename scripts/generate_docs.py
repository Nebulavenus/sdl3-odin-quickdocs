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
            max-width: 900px;
            margin: 0 auto;
        }
        h1 { color: var(--accent); }
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
            margin-bottom: 20px;
            border: 1px solid var(--border);
            position: relative;
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
            padding: 8px;
            border-bottom: 1px solid var(--border);
        }
        .param-name { font-family: monospace; color: var(--accent); }
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
    </style>
</head>
<body>
    <div id="sidebar">
        <div id="search-box">
            <input type="text" id="search-input" placeholder="Search symbols...">
        </div>
        <div id="categories">
            <!-- Categories injected here -->
        </div>
    </div>
    <div id="content">
        <div id="welcome">
            <h1>SDL3 Documentation</h1>
            <p>Select a category or symbol to view details.</p>
        </div>
        <div id="detail" style="display:none">
            <!-- Details injected here -->
        </div>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-c.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/marked/4.3.0/marked.min.js"></script>
    <script>
        // Odin prism component
        Prism.languages.odin = {
            'comment': [
                { pattern: /\\/\\/.*|\\/\\*[\\s\\S]*?\\*\\//, greedy: true },
            ],
            'string': { pattern: /"(?:\\\\.|[^\\\\"\\r\\n])*"/, greedy: true },
            'keyword': /\\b(?:package|import|foreign|where|when|if|else|for|switch|case|break|continue|return|defer|using|cast|typeid|struct|union|enum|proc|map|distinct)\\b/,
            'boolean': /\\b(?:true|false|nil)\\b/,
            'function': /\\b\\w+(?=\\s*::\\s*proc)/,
            'number': /\\b(?:0[xX][\\da-fA-F]+(?:_[\\da-fA-F]+)*|0[oO][0-7]+(?:_[0-7]+)*|0[bB][01]+(?:_[01]+)*|\\d+(?:_\\d+)*(?:\\.\\d+(?:_\\d+)*)?(?:[eE][+-]?\\d+(?:_\\d+)*)?)\\b/,
            'operator': /:=|::|->|\\.\\.\\.|\\+\\+|--|&&|\\|\\||[-+*/%&|^!<>]=?|~/,
            'punctuation': /[\\{\\}\\[\\]\\(\\),.;]/
        };

        const data = DOC_DATA;

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
                    if (list.classList.contains('active')) {
                        showCategoryInfo(cat);
                    }
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
                tagsHtml += `<div class="description">${symbol.tags.description[0].replace(/\\n/g, '<br>')}</div>`;
            }

            if (symbol.tags.param) {
                tagsHtml += `<div class="tag"><div class="tag-name">Parameters</div>
                    <table class="param-table">
                        ${symbol.tags.param.map(p => {
                            const [pname, ...desc] = p.split(' ');
                            return `<tr><td class="param-name">${pname}</td><td>${desc.join(' ')}</td></tr>`;
                        }).join('')}
                    </table>
                </div>`;
            }

            if (symbol.tags.returns) {
                tagsHtml += `<div class="tag"><div class="tag-name">Returns</div><div>${symbol.tags.returns[0]}</div></div>`;
            }

            if (symbol.tags.since) {
                tagsHtml += `<div class="tag"><div class="tag-name">Since</div><div>${symbol.tags.since[0]}</div></div>`;
            }

            detail.innerHTML = `
                <div class="symbol-detail">
                    <h1>${name}</h1>
                    ${synthHtml}
                    ${tagsHtml}
                    
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
                </div>
            `;
            window.location.hash = name;
            Prism.highlightAll();
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
            if (data.symbols[name]) showSymbol(name);
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
        odin_map = {}
        matches = re.finditer(r'^\s*(\w+)\s*::\s*', content, re.MULTILINE)
        for m in matches:
            name = m.group(1)
            start_pos = m.end()
            rest = content[start_pos:]
            if rest.strip().startswith('{'):
                count = 0
                end_idx = 0
                for i, char in enumerate(rest):
                    if char == '{': count += 1
                    elif char == '}':
                        count -= 1
                        if count == 0:
                            end_idx = i + 1
                            break
                decl = rest[:end_idx]
            else:
                end_line = rest.find('\\n')
                if end_line == -1: end_line = len(rest)
                decl = rest[:end_line]
            odin_map[name] = decl.strip()
        return odin_map

    def correlate(self):
        for filename in os.listdir(self.headers_dir):
            if filename.endswith('.odin'):
                path = os.path.join(self.headers_dir, filename)
                with open(path, 'r', encoding='utf-8') as f:
                    odin_symbols = self.extract_odin_symbols(f.read())
                    for sdl_name, data in self.symbols.items():
                        odin_name = sdl_name.replace("SDL_", "")
                        if odin_name in odin_symbols:
                            data["odin_decl"] = f"{odin_name} :: {odin_symbols[odin_name]}"
                        elif sdl_name in odin_symbols:
                            data["odin_decl"] = f"{sdl_name} :: {odin_symbols[sdl_name]}"

    def load_extra(self):
        if not os.path.exists(self.extra_dir): return
        for filename in os.listdir(self.extra_dir):
            if filename.endswith('.md'):
                name = os.path.splitext(filename)[0]
                with open(os.path.join(self.extra_dir, filename), 'r', encoding='utf-8') as f:
                    self.extra_info[name] = f.read()

    def run(self):
        for filename in os.listdir(self.headers_dir):
            if filename.endswith('.h'):
                path = os.path.join(self.headers_dir, filename)
                with open(path, 'r', encoding='utf-8') as f:
                    self.extract_c_symbols(f.read(), filename)
        self.correlate()
        self.load_extra()
        output_data = {
            "categories": self.categories,
            "symbols": self.symbols,
            "extra_info": self.extra_info
        }
        html = HTML_TEMPLATE.replace("DOC_DATA", json.dumps(output_data))
        with open("sdl3_docs.html", "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Generated sdl3_docs.html with {len(self.symbols)} symbols and {len(self.extra_info)} extra notes.")

if __name__ == "__main__":
    gen = SDL3DocGen("Headers", "extra")
    gen.run()
