import os
import re
import json
from typing import Dict, List, Any, Optional, Set

# =============================================================================
# HTML, CSS, AND JAVASCRIPT TEMPLATE
# =============================================================================

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

        /* Sidebar & Search */
        #sidebar {
            width: 350px;
            background: var(--sidebar-bg);
            border-right: 1px solid var(--border);
            display: flex;
            flex-direction: column;
        }

        #search-box { padding: 15px; border-bottom: 1px solid var(--border); }
        #search-input {
            width: 100%; padding: 8px; border-radius: 4px; border: 1px solid var(--border);
            background: var(--bg); color: var(--text); box-sizing: border-box;
        }

        #view-toggle { display: flex; padding: 5px 15px; background: #333; gap: 10px; }
        .toggle-btn {
            flex: 1; padding: 5px; text-align: center; font-size: 0.8em; cursor: pointer;
            border-radius: 3px; background: #444; transition: background 0.2s;
        }
        .toggle-btn.active { background: var(--accent); color: #000; font-weight: bold; }

        #categories { flex: 1; overflow-y: auto; padding: 10px; }
        .category { margin-bottom: 10px; }
        .category-name {
            font-weight: bold; color: var(--accent); cursor: pointer; padding: 5px;
            display: block; border-bottom: 1px solid #444;
        }

        .symbol-list { list-style: none; padding-left: 15px; display: none; }
        .symbol-list.active { display: block; }
        .symbol-item {
            padding: 4px 0; cursor: pointer; font-size: 0.9em; color: #bbb;
            white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
        }
        .symbol-item:hover { color: var(--text); }
        .symbol-type { font-size: 0.7em; opacity: 0.5; margin-right: 8px; text-transform: uppercase; width: 12px; display: inline-block; }

        /* Main Content */
        #content { flex: 1; overflow-y: auto; padding: 40px; scroll-behavior: smooth; }
        .symbol-detail { max-width: 1000px; margin: 0 auto; }
        h1 { color: var(--accent); margin-top: 0; }

        .tag { margin-bottom: 25px; }
        .tag-name {
            font-weight: bold; color: #81d4fa; text-transform: uppercase;
            font-size: 0.85em; margin-bottom: 8px; letter-spacing: 0.05em;
        }

        .code-block {
            background: var(--code-bg); padding: 15px; border-radius: 6px;
            border: 1px solid var(--border); position: relative; overflow-x: auto; margin-bottom: 25px;
        }
        .code-lang { position: absolute; top: 5px; right: 10px; font-size: 0.7em; color: #666; font-weight: bold; }
        pre { margin: 0; }

        .description { line-height: 1.7; margin-bottom: 35px; font-size: 1.1em; }
        .description h1, .description h2 { color: var(--accent); border-bottom: 1px solid #444; padding-bottom: 5px; }

        /* Data Tables */
        .member-table, .param-table { width: 100%; border-collapse: collapse; margin-top: 10px; margin-bottom: 25px; }
        .member-table td, .param-table td { padding: 12px 10px; border-bottom: 1px solid #333; vertical-align: top; }
        .member-name, .param-name { font-family: monospace; color: var(--accent); font-weight: bold; width: 25%; }

        /* Special Sections */
        .synth-info {
            background: var(--synth-bg); padding: 20px; border-radius: 8px;
            margin-bottom: 30px; border-left: 5px solid var(--accent);
        }
        .related-section {
            background: rgba(255,255,255,0.03); padding: 20px; border-radius: 8px;
            margin-top: 25px; border: 1px solid var(--border);
        }
        .related-list { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 10px; list-style: none; padding: 0; margin-top: 12px; }
        .api-link { color: var(--accent); text-decoration: none; cursor: pointer; }
        .api-link:hover { text-decoration: underline; }

        /* UI Elements */
        blockquote { background: rgba(255,255,255,0.05); padding: 15px 25px; margin: 20px 0; border-left: 4px solid var(--accent); font-style: italic; }
        code:not([class*="language-"]) { background: rgba(255,255,255,0.1); padding: 2px 6px; border-radius: 4px; font-family: monospace; font-size: 0.9em; }
        .mermaid { background: white; padding: 15px; border-radius: 6px; margin: 25px 0; box-shadow: 0 4px 15px rgba(0,0,0,0.5); }
    </style>
</head>
<body>
    <div id="sidebar">
        <div id="search-box">
            <input type="text" id="search-input" placeholder="Fuzzy search (e.g. 'CreateWin')...">
        </div>
        <div id="view-toggle">
            <div id="btn-subs" class="toggle-btn active" onclick="setView('subs')">Subsystems</div>
            <div id="btn-az" class="toggle-btn" onclick="setView('az')">A-Z List</div>
        </div>
        <div id="categories"></div>
    </div>
    <div id="content">
        <div id="welcome"></div>
        <div id="detail" style="display:none"></div>
    </div>

    <!-- External Dependencies -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/plugins/autoloader/prism-autoloader.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/marked/4.3.0/marked.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>

    <script>
        // --- PRISM CONFIGURATION ---
        Prism.plugins.autoloader.languages_path = 'https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/';
        Prism.languages.odin = {
            'comment': [{ pattern: /\\/\\/.*|\\/\\*[\\s\\S]*?\\*\\//, greedy: true }],
            'string': { pattern: /"(?:\\\\.|[^\\\\"\\r\\n])*"|`[\\s\\S]*?`/, greedy: true },
            'directive': { pattern: /#\\w+/, alias: 'keyword' },
            'attribute': { pattern: /@\\(\\w+\\)|@\\w+/, alias: 'variable' },
            'keyword': /\\b(?:asm|auto_cast|bit_set|break|case|cast|continue|defer|distinct|do|dynamic|else|enum|fallthrough|for|foreign|if|import|in|map|matrix|not_in|or_break|or_continue|or_else|or_return|package|proc|return|struct|switch|transmute|typeid|union|using|when|where)\\b/,
            'builtin': /\\b(?:len|cap|size_of|align_of|offset_of|type_of|context|nil|self|any|type|bool|b8|b16|b32|b64|int|i8|i16|i32|i64|i128|uint|u8|u16|u32|u64|u128|uintptr|uintptr_t|f16|f32|f64|complex32|complex64|complex128|quaternion64|quaternion128|quaternion256|string|cstring|rawptr)\\b/,
            'boolean': /\\b(?:true|false)\\b/,
            'function': /\\b\\w+(?=\\s*::\\s*(?:#\\w+\\s+)*proc)\\b/,
            'number': /\\b(?:0[xX][\\da-fA-F_]+|0[oO][0-7_]+|0[bB][01_]+|\\d[\\d_]*(?:\\.[\\d_]*)?(?:[eE][+-]?[\\d_]+)?)\\b/,
            'operator': /:=|::|->|\\.\\.\\.|\\+\\+|--|&&|\\|\\||[-+*/%&|^!<>]=?|~/,
            'punctuation': /[\\{\\}\\[\\]\\(\\),.;]/
        };

        // --- MARKED CONFIGURATION ---
        const renderer = new marked.Renderer();
        renderer.code = (code, lang) => lang === 'mermaid' ? `<div class="mermaid">${code}</div>` : `<pre><code class="language-${lang}">${code}</code></pre>`;
        renderer.text = (text) => text.replace(/\\b(SDL_\\w+)\\b/g, (m) => data.symbols[m] ? `<span class="api-link" onclick="showSymbol('${m}')">${m}</span>` : m);
        marked.setOptions({ renderer, gfm: true, breaks: true });

        // --- CORE DATA & STATE ---
        const data = DOC_DATA;
        let currentView = 'subs';

        // --- UI FUNCTIONS ---
        mermaid.initialize({ startOnLoad: false, theme: 'dark' });
        async function renderMermaid() { try { await mermaid.run(); } catch(e) {} }

        function setView(view) {
            currentView = view;
            document.getElementById('btn-subs').classList.toggle('active', view === 'subs');
            document.getElementById('btn-az').classList.toggle('active', view === 'az');
            renderSidebar();
        }

        function showWelcome() {
            const welcome = document.getElementById('welcome');
            document.getElementById('detail').style.display = 'none';
            welcome.style.display = 'block';
            if (data.extra_info['index']) {
                welcome.innerHTML = `<div class="symbol-detail">${marked.parse(data.extra_info['index'])}</div>`;
                setTimeout(renderMermaid, 50);
            }
            window.location.hash = '';
        }

        function renderSidebar() {
            const container = document.getElementById('categories');
            container.innerHTML = '';
            const query = document.getElementById('search-input').value.toLowerCase();

            if (currentView === 'subs') {
                Object.keys(data.categories).sort().forEach(cat => {
                    const symbols = data.categories[cat].filter(s => s.toLowerCase().includes(query)).sort();
                    if (symbols.length === 0 && query) return;
                    const div = document.createElement('div');
                    div.className = 'category';
                    div.innerHTML = `<span class="category-name">${cat}</span>
                        <ul class="symbol-list ${query ? 'active' : ''}">
                            ${symbols.map(s => `<li class="symbol-item" onclick="showSymbol('${s}')"><span class="symbol-type">${data.symbols[s].type[0]}</span>${s}</li>`).join('')}
                        </ul>`;
                    div.querySelector('.category-name').onclick = () => {
                        const list = div.querySelector('.symbol-list');
                        list.classList.toggle('active');
                        if (list.classList.contains('active')) showCategoryInfo(cat);
                    };
                    container.appendChild(div);
                });
            } else {
                const list = document.createElement('ul');
                list.className = 'symbol-list active';
                Object.keys(data.symbols).sort().filter(s => s.toLowerCase().includes(query)).forEach(s => {
                    const li = document.createElement('li');
                    li.className = 'symbol-item';
                    li.innerHTML = `<span class="symbol-type">${data.symbols[s].type[0]}</span>${s}`;
                    li.onclick = () => showSymbol(s);
                    list.appendChild(li);
                });
                container.appendChild(list);
            }
        }

        function showCategoryInfo(cat) {
            const detail = document.getElementById('detail');
            document.getElementById('welcome').style.display = 'none';
            detail.style.display = 'block';
            let synthHtml = data.extra_info[cat] ? `<div class="synth-info">${marked.parse(data.extra_info[cat])}</div>` : '';
            detail.innerHTML = `<div class="symbol-detail"><h1>Category: ${cat}</h1>${synthHtml}<p>Select a symbol from the sidebar to view details.</p></div>`;
            Prism.highlightAll();
            setTimeout(renderMermaid, 50);
        }

        function showSymbol(name) {
            const symbol = data.symbols[name];
            if (!symbol) return;
            const detail = document.getElementById('detail');
            document.getElementById('welcome').style.display = 'none';
            detail.style.display = 'block';

            let tagsHtml = symbol.tags.description ? `<div class="description">${marked.parse(symbol.tags.description[0])}</div>` : '';
            if (symbol.members && symbol.members.length > 0) {
                tagsHtml += `<div class="tag"><div class="tag-name">Members / Fields</div><table class="member-table">` + 
                    symbol.members.map(m => `<tr><td class="member-name">${m.name}</td><td>${marked.parse(m.desc || '')}</td></tr>`).join('') + `</table></div>`;
            }
            if (symbol.tags.param) {
                tagsHtml += `<div class="tag"><div class="tag-name">Parameters</div><table class="param-table">` + 
                    symbol.tags.param.map(p => {
                        const s = p.indexOf(' ');
                        return `<tr><td class="param-name">${s === -1 ? p : p.substring(0,s)}</td><td>${s === -1 ? '' : marked.parse(p.substring(s+1))}</td></tr>`;
                    }).join('') + `</table></div>`;
            }
            
            const standardTags = { 'returns': 'Returns', 'threadsafety': 'Thread Safety', 'notes': 'Notes', 'note': 'Note', 'warning': 'Warning', 'deprecated': 'Deprecated', 'since': 'Since' };
            Object.keys(standardTags).forEach(tag => {
                if (symbol.tags[tag]) {
                    const color = tag === 'warning' ? 'color: #ff8a65' : (tag === 'deprecated' ? 'color: #e57373; font-weight:bold' : '');
                    tagsHtml += `<div class="tag"><div class="tag-name">${standardTags[tag]}</div><div style="${color}">${marked.parse(symbol.tags[tag][0])}</div></div>`;
                }
            });

            if (symbol.tags.sa) {
                tagsHtml += `<div class="tag"><div class="tag-name">See Also</div><ul class="related-list">` + 
                    symbol.tags.sa.map(s => `<li class="api-link" onclick="showSymbol('${s.trim()}')">${s.trim()}</li>`).join('') + `</ul></div>`;
            }

            let hierarchyHtml = '';
            if (data.hierarchy[name]) {
                const h = data.hierarchy[name];
                if (h.creators.length || h.methods.length || h.destructors.length) {
                    hierarchyHtml = `<div class="related-section"><div class="tag-name">Functional API: ${name}</div>
                        ${h.creators.length ? `<div><b>Constructors:</b><ul class="related-list">${h.creators.map(c => `<li class="api-link" onclick="showSymbol('${c}')">${c}</li>`).join('')}</ul></div>` : ''}
                        ${h.methods.length ? `<div style="margin-top:15px"><b>Methods:</b><ul class="related-list">${h.methods.map(m => `<li class="api-link" onclick="showSymbol('${m}')">${m}</li>`).join('')}</ul></div>` : ''}
                        ${h.destructors.length ? `<div style="margin-top:15px"><b>Destructors:</b><ul class="related-list">${h.destructors.map(d => `<li class="api-link" onclick="showSymbol('${d}')">${d}</li>`).join('')}</ul></div>` : ''}
                    </div>`;
                }
            }

            let synthHtml = data.extra_info[name] ? `<div class="synth-info"><div class="tag-name">Synthesized Info</div>${marked.parse(data.extra_info[name])}</div>` : '';

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
                </div>`;
            window.location.hash = name;
            Prism.highlightAll();
            setTimeout(renderMermaid, 50);
            detail.scrollTop = 0;
        }

        document.getElementById('search-input').oninput = renderSidebar;
        renderSidebar();
        if (window.location.hash) {
            const n = window.location.hash.substring(1);
            if (data.symbols[n]) showSymbol(n); else showWelcome();
        } else showWelcome();
    </script>
</body>
</html>"""

# =============================================================================
# DOCUMENTATION GENERATOR ENGINE
# =============================================================================

class SDL3DocumentationGenerator:
    def __init__(self, headers_dir: str, extra_dir: str):
        self.headers_dir = headers_dir
        self.extra_dir = extra_dir
        
        # Internal Database
        self.symbols: Dict[str, Any] = {}
        self.categories: Dict[str, List[str]] = {}
        self.extra_info: Dict[str, str] = {}
        self.odin_bindings: Dict[str, str] = {}
        self.hierarchy: Dict[str, Dict[str, List[str]]] = {}

    def _normalize_type(self, type_str: str) -> str:
        """Strip C qualifiers to find the base SDL handle name."""
        return type_str.replace('const', '').replace('*', '').replace('struct', '').strip()

    def _parse_doxygen_block(self, block: str) -> Dict[str, List[str]]:
        """Parses a Doxygen block into a dictionary of tags."""
        if not block: return {}
        
        tags = {"description": []}
        current_tag = "description"
        buffer = []

        for line in block.split('\n'):
            line = line.strip().lstrip('*').strip()
            # Match @tag or \tag
            match = re.match(r'[\\@](\w+)\s*(.*)', line)
            if match:
                if buffer:
                    tags.setdefault(current_tag, []).append("\n".join(buffer).strip())
                current_tag, remainder = match.groups()
                buffer = [remainder] if remainder else []
            else:
                buffer.append(line)
        
        if buffer:
            tags.setdefault(current_tag, []).append("\n".join(buffer).strip())
        return tags

    def extract_odin_symbols(self, content: str):
        """Scans Odin bindings for symbol declarations and their attributes."""
        # Find 'Name ::' declarations
        for match in re.finditer(r'\b(\w+)\s*::\s*', content):
            name = match.group(1)
            if name in ['struct', 'enum', 'union', 'proc', 'foreign', 'import', 'package', 'if', 'when', 'else', 'for', 'switch', 'case', 'return', 'defer', 'using', 'cast', 'typeid']:
                continue
            
            # Extract declaration body (handles braces and simple lines)
            rest = content[match.end():]
            search_rest = rest.lstrip()
            if not search_rest: continue
            
            declaration = ""
            if search_rest.startswith('{') or any(search_rest.startswith(k) for k in ['struct', 'enum', 'union', 'proc']):
                # Find matching braces
                brace_pos = rest.find('{')
                if brace_pos != -1 and (rest.find('---') == -1 or brace_pos < rest.find('---')):
                    count, end_idx = 0, 0
                    for i in range(brace_pos, len(rest)):
                        if rest[i] == '{': count += 1
                        elif rest[i] == '}':
                            count -= 1
                            if count == 0:
                                end_idx = i + 1
                                break
                    declaration = rest[:end_idx]
                else:
                    # Simple single-line or no-brace block (like 'proc ---')
                    declaration = rest[:rest.find('\n')] if '\n' in rest else rest
            else:
                declaration = rest[:rest.find('\n')] if '\n' in rest else rest
            
            # Look for attributes above the declaration
            prefix = ""
            search_back = content[:match.start()].split('\n')
            attributes = []
            for line in reversed(search_back[:-1]):
                if not line.strip(): continue
                if '@' in line: attributes.append(line)
                else: break
            
            if attributes:
                prefix = "\n".join(reversed(attributes)).strip() + "\n"

            self.odin_bindings[name] = (prefix + name + " :: " + declaration).strip()

    def _parse_c_members(self, body: str) -> List[Dict[str, str]]:
        """Extracts trailing Doxygen comments for struct/enum members."""
        members = []
        for m in re.finditer(r'(\w+)\s*[=,;]\s*/\*\*< (.*?) \*/', body):
            members.append({"name": m.group(1), "desc": m.group(2).strip()})
        return members

    def extract_c_symbols(self, content: str, filename: str):
        """Primary parser for C headers using Doxygen blocks as anchors."""
        cat_match = re.search(r'# Category(\w+)', content)
        category = cat_match.group(1) if cat_match else filename.replace("SDL_", "").split('.')[0]
        
        # 1. Main Symbol Extraction (Doxygen-anchored)
        blocks = re.finditer(r'/\*\*(.*?)\*/\s*([^\n;{][^{;]*[;{])', content, re.DOTALL)
        for m in blocks:
            doc, decl_head = m.groups()
            tags = self._parse_doxygen_block(doc)
            name, type_str, full_decl, members = None, "unknown", decl_head, []
            
            # --- Function Detection ---
            if "extern SDL_DECLSPEC" in decl_head:
                fn_match = re.search(r'SDLCALL\s+(SDL_\w+)\s*\(', decl_head)
                if fn_match:
                    name, type_str = fn_match.group(1), "function"
                    if not decl_head.endswith(';'):
                        rem = content[m.end():]
                        end_semi = rem.find(';')
                        if end_semi != -1: full_decl += rem[:end_semi+1]
            
            # --- Typedef Detection (Struct/Enum) ---
            elif "typedef" in decl_head:
                type_match = re.search(r'typedef\s+(struct|enum)\s+(\w+)', decl_head)
                if type_match:
                    name, type_str = type_match.group(2), type_match.group(1)
                    if '{' in decl_head or not decl_head.endswith(';'):
                        rem = content[m.end():]
                        end_semi = rem.find(';')
                        if end_semi != -1: 
                            body = rem[:end_semi+1]
                            full_decl += body
                            members = self._parse_c_members(body)
                else:
                    # Simple Typedef
                    td_match = re.search(r'typedef\s+.*?\s+(SDL_\w+)\s*;', decl_head)
                    if td_match: name, type_str = td_match.group(1), "typedef"

            # --- Macro Detection ---
            elif "#define" in decl_head:
                macro_match = re.search(r'#define\s+(SDL_\w+)', decl_head)
                if macro_match: name, type_str = macro_match.group(1), "macro"
            
            if name:
                full_decl = re.sub(r'\s+', ' ', full_decl).strip()
                
                # Metadata for hierarchy analysis
                ret_type, arg_list = None, []
                if type_str == "function":
                    ret_match = re.match(r'extern\s+SDL_DECLSPEC\s+(.*?)\s+SDLCALL', full_decl)
                    if ret_match: ret_type = self._normalize_type(ret_match.group(1))
                    arg_match = re.search(r'\((.*?)\)', full_decl)
                    if arg_match:
                        for arg in arg_match.group(1).split(','):
                            arg = arg.strip()
                            if arg and arg != 'void':
                                parts = arg.split(' ')
                                arg_list.append(self._normalize_type(" ".join(parts[:-1]) if len(parts)>1 else parts[0]))

                self.symbols[name] = {
                    "name": name, "type": type_str, "c_decl": full_decl, 
                    "tags": tags, "category": category, "members": members,
                    "ret_type": ret_type, "args": arg_list
                }
                self.categories.setdefault(category, []).append(name)

        # 2. Grouped Macro Extraction (No leading Doxygen)
        for m in re.finditer(r'#define\s+(SDL_\w+)\s+.*?(?:/\*\*< (.*?) \*/)?', content):
            name, desc = m.groups()
            if name not in self.symbols:
                self.symbols[name] = {"name": name, "type": "macro", "c_decl": m.group(0), "tags": {"description": [desc]} if desc else {}, "category": category}
                self.categories.setdefault(category, []).append(name)

    def correlate_and_analyze(self):
        """Matches C symbols to Odin bindings and builds object hierarchy."""
        # --- 1. Correlation ---
        for name, data in self.symbols.items():
            stripped = name.replace("SDL_", "")
            # Direct match or stripped match
            if stripped in self.odin_bindings:
                data["odin_decl"] = self.odin_bindings[stripped]
            elif name in self.odin_bindings:
                data["odin_decl"] = self.odin_bindings[name]
            else:
                # Sub-prefix stripping (e.g. SDL_PIXELFORMAT_X -> PIXELFORMAT_X)
                parts = name.split('_')
                for i in range(1, len(parts)):
                    shorter = "_".join(parts[i:])
                    if shorter in self.odin_bindings:
                        data["odin_decl"] = self.odin_bindings[shorter]
                        break
        
        # --- 2. Functional Hierarchy ---
        # Initialize buckets for all "objects" (structs/typedefs)
        for name, data in self.symbols.items():
            if data['type'] in ['struct', 'typedef', 'enum']:
                self.hierarchy[name] = {"creators": [], "methods": [], "destructors": []}
        
        # Populate buckets
        for name, data in self.symbols.items():
            if data['type'] != 'function': continue
            
            ret, args = data.get('ret_type'), data.get('args', [])
            
            # If it returns an object -> Creator
            if ret in self.hierarchy:
                self.hierarchy[ret]["creators"].append(name)
            # If 1st arg is an object -> Method or Destructor
            elif args and args[0] in self.hierarchy:
                handle = args[0]
                if any(kw in name for kw in ["Destroy", "Free", "Close", "Release"]):
                    self.hierarchy[handle]["destructors"].append(name)
                else:
                    self.hierarchy[handle]["methods"].append(name)

    def run(self):
        """Orchestrates the full generation process."""
        print("Parsing Odin bindings...")
        for f in [x for x in os.listdir(self.headers_dir) if x.endswith('.odin')]:
            with open(os.path.join(self.headers_dir, f), 'r', encoding='utf-8') as file:
                self.extract_odin_symbols(file.read())
        
        print("Parsing C headers...")
        for f in [x for x in os.listdir(self.headers_dir) if x.endswith('.h')]:
            with open(os.path.join(self.headers_dir, f), 'r', encoding='utf-8') as file:
                self.extract_c_symbols(file.read(), f)
        
        print("Analyzing relationships and extra content...")
        self.correlate_and_analyze()
        
        if os.path.exists(self.extra_dir):
            for f in [x for x in os.listdir(self.extra_dir) if x.endswith('.md')]:
                with open(os.path.join(self.extra_dir, f), 'r', encoding='utf-8') as file:
                    self.extra_info[f.replace('.md', '')] = file.read()
        
        print(f"Bundling into single-file HTML...")
        output_data = {
            "categories": {k: sorted(list(set(v))) for k, v in self.categories.items()},
            "symbols": self.symbols,
            "extra_info": self.extra_info,
            "hierarchy": self.hierarchy
        }
        
        with open("docs/index.html", "w", encoding="utf-8") as f:
            # We replace exactly once to avoid accidental nested replacements
            f.write(HTML_TEMPLATE.replace("DOC_DATA", json.dumps(output_data)))
            
        print(f"Success! Generated sdl3_docs.html with {len(self.symbols)} symbols.")

if __name__ == "__main__":
    generator = SDL3DocumentationGenerator(headers_dir="Headers", extra_dir="extra")
    generator.run()
