# SDL3 Odin Quick Docs Generator

A "vibecoded" single-file documentation generator for SDL3, bridging C headers and Odin bindings.

## Features
- **Dual Signatures:** View both C and Odin declarations for every symbol in one place.
- **Object-Oriented View:** Automatically categorizes procedural functions into "Creators", "Methods", and "Destructors" for every handle/struct.
- **Deep Trace:** Extracts over 3,000 symbols including nested enum members and grouped macros.
- **Interactive Browsing:** Fast fuzzy search, subsystem vs A-Z views, and automatic symbol linking in descriptions.
- **Technical Overviews:** Integrated **Mermaid.js** support for architectural diagrams.
- **Offline Ready:** Generates a single self-contained HTML file with all documentation data embedded.

## Project Structure
- `Headers/`: The source directory containing `.h` (SDL3) and `.odin` (bindings) files.
- `extra/`: Markdown files used to inject "Human" explanations or overviews.
    - `index.md`: The home/overview page.
    - `{Subsystem}.md`: Subsystem-specific overviews (e.g., `Video.md`).
    - `{SDL_Symbol}.md`: Extra tips for specific functions/structs.
- `scripts/generate_docs.py`: The core Python engine that parses, correlates, and generates the HTML.
- `sdl3_docs.html`: The final generated documentation.

## How it Works
1. **Extraction:** The script uses regex to scan all `.h` and `.odin` files. It looks for Doxygen blocks and the declarations following them.
2. **Correlation:** It maps C symbols (e.g., `SDL_CreateWindow`) to Odin symbols (`CreateWindow`) by heuristic prefix stripping.
3. **Analysis:** It traces function parameters and return types to build a logical hierarchy (e.g., seeing that `SDL_SetWindowTitle` is a "method" of `SDL_Window`).
4. **Synthesis:** It merges automated extraction data with manual Markdown content from the `extra/` folder.
5. **Bundling:** Everything is packed into a single HTML template using `marked.js` for Markdown, `Prism.js` for code highlighting, and `Mermaid.js` for diagrams.

## Extending & Modifying
### Adding Explanations
Simply create a `.md` file in the `extra/` folder. If the filename matches an SDL symbol or a Category name, it will be injected as a "Synthesized Info" block on that page.

### Modifying the Layout
The `HTML_TEMPLATE` variable at the top of `scripts/generate_docs.py` contains all CSS and JS. You can modify the `style` tags or the navigation logic there.

### Fixing Extraction
If a symbol is missing or broken, check the regex patterns in `extract_c_symbols` or `extract_odin_symbols`. The C parser is generic (looking for `/** ... */` + code), while the Odin parser specifically looks for `::` declarations.

## License
This project is released into the public domain under the [Unlicense](LICENSE).

### Vendored Content Licenses
- **SDL3 Headers:** Located in `Headers/`, licensed under the [Zlib License](Headers/SDL_copying.h).
- **Odin Bindings:** Usually follow the Odin compiler's license (BSD-2-Clause or Zlib depending on the source).

### Third-Party Libraries (Embedded via CDN)
The generated `sdl3_docs.html` uses the following libraries:
- **Prism.js:** MIT License
- **marked.js:** MIT License
- **Mermaid.js:** MIT License

## Warranty & Disclaimer
This tool was built quickly for high-level overview purposes. **It is not an official SDL project.** No warranty is provided; use at your own risk. Always consult the [Official SDL Wiki](https://wiki.libsdl.org/SDL3) for the most accurate information.
