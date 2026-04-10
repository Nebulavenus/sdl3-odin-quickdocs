### Tips for SDL_CreateWindow
When creating a window in SDL3, the flags are now 64-bit. 

In Odin, this is represented as a `bit_set`:
```odin
flags := sdl.WindowFlags{.RESIZABLE, .HIGH_PIXEL_DENSITY}
window := sdl.CreateWindow("My Game", 800, 600, flags)
```
