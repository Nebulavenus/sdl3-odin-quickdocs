# Audio Overview in SDL3

SDL3 simplifies audio by using **Audio Streams** as the primary interface. 

### Key Concepts:
- **Logical Devices:** Multiple applications can share a single physical device.
- **Automatic Migration:** SDL3 can seamlessly move audio between devices (e.g., when plugging in headphones).
- **Simplified API:** Use `SDL_OpenAudioDeviceStream` for quick setup.

> [!NOTE]
> In Odin, ensure you handle `AudioDeviceID` as a distinct type.
