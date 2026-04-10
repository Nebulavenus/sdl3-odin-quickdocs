# SDL3 Architecture Overview

SDL3 is organized into several semi-independent subsystems. Most applications follow a standard lifecycle of initialization, window creation, event polling, and rendering.

## General Lifecycle & Subsystems

```mermaid
graph TD
    subgraph Initialization
        Start[App Start] --> Init[SDL_Init: flags]
    end

    subgraph Video_System
        Init --> Win[SDL_CreateWindow: title, w, h, flags]
        Win --> Props[SDL_GetWindowProperties: window]
    end

    subgraph Event_Loop
        Win --> Poll[SDL_PollEvent: SDL_Event*]
        Poll -- has event --> Handle[Handle Input/Quit]
        Handle --> Poll
        Poll -- empty --> Update[Update Game State]
    end

    subgraph Rendering
        Update --> Render[Draw Frame]
        Render --> Win
    end

    Handle -- Quit Event --> Quit[SDL_Quit]
```

### Structs & Dependencies
- **SDL_InitFlags**: Bit-set passed to `SDL_Init` (e.g., `SDL_INIT_VIDEO`, `SDL_INIT_AUDIO`).
- **SDL_Window**: Created by `SDL_CreateWindow`, owned by the Video subsystem.
- **SDL_Event**: Union struct populated by `SDL_PollEvent` or `SDL_WaitEvent`.
