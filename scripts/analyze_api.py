import os
import re
import json

class APIAnalyzer:
    def __init__(self, headers_dir):
        self.headers_dir = headers_dir
        self.functions = []
        self.structs = set()
        # Handle -> { "required_by": [OtherHandles], "depends_on": [OtherHandles], "interactions": [OtherHandles] }
        self.relations = {} 

    def clean_type(self, type_str):
        t = type_str.replace('const', '').replace('*', '').strip()
        if t.startswith('SDL_'):
            return t
        return None

    def extract_data(self):
        struct_pattern = r'typedef\s+struct\s+(SDL_\w+)'
        for filename in os.listdir(self.headers_dir):
            if filename.endswith('.h'):
                with open(os.path.join(self.headers_dir, filename), 'r', encoding='utf-8') as f:
                    content = f.read()
                    for m in re.finditer(struct_pattern, content):
                        self.structs.add(m.group(1))

        func_pattern = r'extern\s+SDL_DECLSPEC\s+(.*?)\s+SDLCALL\s+(SDL_\w+)\s*\((.*?)\);'
        for filename in os.listdir(self.headers_dir):
            if filename.endswith('.h'):
                with open(os.path.join(self.headers_dir, filename), 'r', encoding='utf-8') as f:
                    content = f.read()
                    for m in re.finditer(func_pattern, content, re.DOTALL):
                        ret_type, name, args_str = m.groups()
                        
                        args = []
                        for arg in args_str.split(','):
                            arg = arg.strip()
                            if not arg or arg == 'void': continue
                            parts = arg.split(' ')
                            if len(parts) > 1:
                                arg_type = " ".join(parts[:-1]).strip()
                                args.append(self.clean_type(arg_type))
                            else:
                                args.append(self.clean_type(arg))

                        self.functions.append({
                            "name": name,
                            "ret": self.clean_type(ret_type),
                            "args": [a for a in args if a]
                        })

    def build_relations(self):
        for s in self.structs:
            self.relations[s] = {"creates": set(), "required_for": set(), "uses": set()}

        for fn in self.functions:
            ret = fn['ret']
            args = fn['args']

            if not args:
                continue

            # 1. Dependency: First arg creates Return type
            # e.g. SDL_Window -> SDL_Renderer
            if ret and ret in self.structs:
                main_arg = args[0]
                if main_arg in self.structs and main_arg != ret:
                    self.relations[main_arg]["creates"].add(ret)
                    self.relations[ret]["required_for"].add(main_arg)

            # 2. Interaction: Function takes multiple handles
            # e.g. SDL_RenderTexture(Renderer, Texture)
            if len(args) > 1:
                for i in range(len(args)):
                    for j in range(i + 1, len(args)):
                        a, b = args[i], args[j]
                        if a in self.structs and b in self.structs and a != b:
                            self.relations[a]["uses"].add(b)
                            self.relations[b]["uses"].add(a)

    def generate_report(self):
        with open("API_INTERACTIONS.md", "w", encoding="utf-8") as f:
            f.write("# SDL3 API Interaction Graph\n\n")
            f.write("This diagram shows how core SDL3 handles depend on and interact with each other.\n\n")
            
            f.write("```mermaid\ngraph LR\n")
            
            # Focus on most important core handles to keep diagram readable
            core_handles = [
                "SDL_Window", "SDL_Renderer", "SDL_Texture", "SDL_Surface", 
                "SDL_GPUDevice", "SDL_GPUCommandBuffer", "SDL_GPURenderPass",
                "SDL_AudioStream", "SDL_IOStream", "SDL_PropertiesID"
            ]

            added_edges = set()

            for h in core_handles:
                if h not in self.relations: continue
                
                # Draw creation links
                for other in self.relations[h]["creates"]:
                    if other in core_handles:
                        edge = tuple(sorted((h, other)))
                        if edge not in added_edges:
                            f.write(f"    {h} -- \"creates\" --> {other}\n")
                            added_edges.add(edge)

                # Draw usage links
                for other in self.relations[h]["uses"]:
                    if other in core_handles:
                        edge = tuple(sorted((h, other)))
                        if edge not in added_edges:
                            f.write(f"    {h} <--> {other}\n")
                            added_edges.add(edge)

            f.write("```\n\n")
            
            f.write("## Subsystem Connectivity Details\n\n")
            for h in sorted(self.relations.keys()):
                rel = self.relations[h]
                if not rel["creates"] and not rel["uses"]: continue
                
                f.write(f"### {h}\n")
                if rel["creates"]:
                    f.write("- **Produces:** " + ", ".join([f"`{x}`" for x in sorted(rel["creates"])]) + "\n")
                if rel["uses"]:
                    f.write("- **Interacts with:** " + ", ".join([f"`{x}`" for x in sorted(rel["uses"])]) + "\n")
                f.write("\n")

        print(f"Generated API_INTERACTIONS.md mapping interactions between {len(self.structs)} handles.")

if __name__ == "__main__":
    analyzer = APIAnalyzer("Headers")
    analyzer.extract_data()
    analyzer.build_relations()
    analyzer.generate_report()
