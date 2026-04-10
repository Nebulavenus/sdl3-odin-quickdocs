# SDL3 GPU API

The GPU API provides a modern, low-level interface for 3D graphics and compute. It is based on command recording and submission.

## GPU Workflow & Struct Dependencies

```mermaid
graph TD
    subgraph Device_Setup
        Init[SDL_Init] --> Dev[SDL_CreateGPUDevice: format, debug, name]
        Dev --> Claim[SDL_ClaimWindowForGPUDevice: device, window]
    end

    subgraph Pipeline_State
        Dev --> Pipe[SDL_CreateGPUGraphicsPipeline: device, SDL_GPUGraphicsPipelineCreateInfo]
    end

    subgraph Frame_Recording
        Dev --> CB[SDL_AcquireGPUCommandBuffer: device]
        CB -- SDL_AcquireGPUSwapchainTexture --> ST[Swapchain Texture]
        
        CB -- SDL_BeginGPURenderPass --> RP[SDL_GPURenderPass]
        RP -- SDL_BindGPUGraphicsPipeline --> Pipe
        RP -- SDL_DrawGPUPrimitives --> Work[Recorded Work]
        RP -- SDL_EndGPURenderPass --> CB
    end

    subgraph Submission
        CB -- SDL_SubmitGPUCommandBuffer --> Done[Hardware Execution]
    end
```

### Critical Structs
- **SDL_GPUGraphicsPipelineCreateInfo**: Huge struct defining shaders, vertex layout, blend modes, and depth testing.
- **SDL_GPUCommandBuffer**: Represents a "to-do list" for the GPU.
- **SDL_GPURenderPass**: Scoped object for drawing into specific textures.
- **SDL_GPUBuffer**: Created via `SDL_CreateGPUBuffer`, used for vertices, indices, or uniforms.
