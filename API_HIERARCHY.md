# SDL3 API Functional Hierarchy

This report categorizes the SDL3 API by the 'Objects' (handles) they operate on.

## Global
### ⚙️ Methods
- `SDL_AddEventWatch`
- `SDL_AddGamepadMapping`
- `SDL_AddGamepadMappingsFromFile`
- `SDL_AddHintCallback`
- `SDL_AddTimer`
- `SDL_AddTimerNS`
- `SDL_AudioDevicePaused`
- `SDL_BindAudioStream`
- `SDL_BindAudioStreams`
- `SDL_CalculateGPUTextureFormatSize`
- `SDL_CaptureMouse`
- `SDL_CleanupTLS`
- `SDL_ClearClipboardData`
- `SDL_ClearError`
- `SDL_ClearProperty`
- `SDL_CloseAudioDevice`
- `SDL_CompareAndSwapAtomicPointer`
- `SDL_ComposeCustomBlendMode`
- `SDL_ConvertPixels`
- `SDL_ConvertPixelsAndColorspace`
- `SDL_CopyFile`
- `SDL_CopyProperties`
- `SDL_CreateDirectory`
- `SDL_CreateProperties`
- `SDL_CreateSystemCursor`
- `SDL_CreateWindowAndRenderer`
- `SDL_CursorVisible`
- `SDL_Delay`
- `SDL_DelayNS`
- `SDL_DelayPrecise`
- `SDL_DestroyProperties`
- `SDL_DetachVirtualJoystick`
- `SDL_DisableScreenSaver`
- `SDL_EGL_GetCurrentConfig`
- `SDL_EGL_GetCurrentDisplay`
- `SDL_EGL_GetProcAddress`
- `SDL_EGL_SetAttributeCallbacks`
- `SDL_EnableScreenSaver`
- `SDL_EnterAppMainCallbacks`
- `SDL_EnumerateDirectory`
- `SDL_EnumerateProperties`
- `SDL_EventEnabled`
- `SDL_FilterEvents`
- `SDL_FlushEvent`
- `SDL_FlushEvents`
- `SDL_GDKSuspendComplete`
- `SDL_GL_DestroyContext`
- `SDL_GL_ExtensionSupported`
- `SDL_GL_GetAttribute`
- `SDL_GL_GetCurrentContext`
- `SDL_GL_GetProcAddress`
- `SDL_GL_GetSwapInterval`
- `SDL_GL_LoadLibrary`
- `SDL_GL_ResetAttributes`
- `SDL_GL_SetAttribute`
- `SDL_GL_SetSwapInterval`
- `SDL_GL_UnloadLibrary`
- `SDL_GPUSupportsProperties`
- `SDL_GPUSupportsShaderFormats`
- `SDL_GPUTextureFormatTexelBlockSize`
- `SDL_GamepadEventsEnabled`
- `SDL_GetAndroidActivity`
- `SDL_GetAndroidCachePath`
- `SDL_GetAndroidExternalStoragePath`
- `SDL_GetAndroidExternalStorageState`
- `SDL_GetAndroidInternalStoragePath`
- `SDL_GetAndroidJNIEnv`
- `SDL_GetAndroidSDKVersion`
- `SDL_GetAppMetadataProperty`
- `SDL_GetAssertionHandler`
- `SDL_GetAtomicPointer`
- `SDL_GetAudioDeviceChannelMap`
- `SDL_GetAudioDeviceFormat`
- `SDL_GetAudioDeviceGain`
- `SDL_GetAudioDeviceName`
- `SDL_GetAudioDriver`
- `SDL_GetAudioFormatName`
- `SDL_GetAudioPlaybackDevices`
- `SDL_GetAudioRecordingDevices`
- `SDL_GetBasePath`
- `SDL_GetBooleanProperty`
- `SDL_GetCPUCacheLineSize`
- `SDL_GetCameraDriver`
- `SDL_GetCameraName`
- `SDL_GetCameraPosition`
- `SDL_GetCameras`
- `SDL_GetClipboardData`
- `SDL_GetClipboardMimeTypes`
- `SDL_GetClipboardText`
- `SDL_GetClosestFullscreenDisplayMode`
- `SDL_GetCurrentAudioDriver`
- `SDL_GetCurrentCameraDriver`
- `SDL_GetCurrentDirectory`
- `SDL_GetCurrentDisplayOrientation`
- `SDL_GetCurrentThreadID`
- `SDL_GetCurrentTime`
- `SDL_GetCurrentVideoDriver`
- `SDL_GetDXGIOutputInfo`
- `SDL_GetDateTimeLocalePreferences`
- `SDL_GetDayOfWeek`
- `SDL_GetDayOfYear`
- `SDL_GetDaysInMonth`
- `SDL_GetDefaultAssertionHandler`
- `SDL_GetDefaultLogOutputFunction`
- `SDL_GetDirect3D9AdapterIndex`
- `SDL_GetDisplayBounds`
- `SDL_GetDisplayContentScale`
- `SDL_GetDisplayName`
- `SDL_GetDisplayProperties`
- `SDL_GetDisplayUsableBounds`
- `SDL_GetDisplays`
- `SDL_GetError`
- `SDL_GetEventDescription`
- `SDL_GetEventFilter`
- `SDL_GetFloatProperty`
- `SDL_GetGDKDefaultUser`
- `SDL_GetGDKTaskQueue`
- `SDL_GetGPUDriver`
- `SDL_GetGPUTextureFormatFromPixelFormat`
- `SDL_GetGamepadAxisFromString`
- `SDL_GetGamepadButtonFromString`
- `SDL_GetGamepadButtonLabelForType`
- `SDL_GetGamepadMappingForID`
- `SDL_GetGamepadMappings`
- `SDL_GetGamepadNameForID`
- `SDL_GetGamepadPathForID`
- `SDL_GetGamepadPlayerIndexForID`
- `SDL_GetGamepadProductForID`
- `SDL_GetGamepadProductVersionForID`
- `SDL_GetGamepadStringForAxis`
- `SDL_GetGamepadStringForButton`
- `SDL_GetGamepadStringForType`
- `SDL_GetGamepadTypeForID`
- `SDL_GetGamepadTypeFromString`
- `SDL_GetGamepadVendorForID`
- `SDL_GetGamepads`
- `SDL_GetGlobalMouseState`
- `SDL_GetGlobalProperties`
- `SDL_GetHapticNameForID`
- `SDL_GetHaptics`
- `SDL_GetHintBoolean`
- `SDL_GetJoystickNameForID`
- `SDL_GetJoystickPathForID`
- `SDL_GetJoystickPlayerIndexForID`
- `SDL_GetJoystickProductForID`
- `SDL_GetJoystickProductVersionForID`
- `SDL_GetJoystickTypeForID`
- `SDL_GetJoystickVendorForID`
- `SDL_GetJoysticks`
- `SDL_GetKeyFromName`
- `SDL_GetKeyFromScancode`
- `SDL_GetKeyName`
- `SDL_GetKeyboardNameForID`
- `SDL_GetKeyboardState`
- `SDL_GetKeyboards`
- `SDL_GetLogOutputFunction`
- `SDL_GetLogPriority`
- `SDL_GetMasksForPixelFormat`
- `SDL_GetMemoryFunctions`
- `SDL_GetMice`
- `SDL_GetModState`
- `SDL_GetMouseNameForID`
- `SDL_GetMouseState`
- `SDL_GetNaturalDisplayOrientation`
- `SDL_GetNumAllocations`
- `SDL_GetNumAudioDrivers`
- `SDL_GetNumCameraDrivers`
- `SDL_GetNumGPUDrivers`
- `SDL_GetNumLogicalCPUCores`
- `SDL_GetNumRenderDrivers`
- `SDL_GetNumVideoDrivers`
- `SDL_GetNumberProperty`
- `SDL_GetOriginalMemoryFunctions`
- `SDL_GetPathInfo`
- `SDL_GetPenDeviceType`
- `SDL_GetPerformanceCounter`
- `SDL_GetPerformanceFrequency`
- `SDL_GetPixelFormatForMasks`
- `SDL_GetPixelFormatFromGPUTextureFormat`
- `SDL_GetPixelFormatName`
- `SDL_GetPlatform`
- `SDL_GetPointerProperty`
- `SDL_GetPowerInfo`
- `SDL_GetPrefPath`
- `SDL_GetPrimaryDisplay`
- `SDL_GetPrimarySelectionText`
- `SDL_GetPropertyType`
- `SDL_GetRGB`
- `SDL_GetRGBA`
- `SDL_GetRealGamepadTypeForID`
- `SDL_GetRelativeMouseState`
- `SDL_GetRenderDriver`
- `SDL_GetRevision`
- `SDL_GetSIMDAlignment`
- `SDL_GetSandbox`
- `SDL_GetScancodeFromKey`
- `SDL_GetScancodeFromName`
- `SDL_GetScancodeName`
- `SDL_GetSensorNameForID`
- `SDL_GetSensorNonPortableTypeForID`
- `SDL_GetSensorTypeForID`
- `SDL_GetSensors`
- `SDL_GetSilenceValueForFormat`
- `SDL_GetStringProperty`
- `SDL_GetSystemPageSize`
- `SDL_GetSystemRAM`
- `SDL_GetSystemTheme`
- `SDL_GetTLS`
- `SDL_GetTicks`
- `SDL_GetTicksNS`
- `SDL_GetTouchDeviceName`
- `SDL_GetTouchDeviceType`
- `SDL_GetTouchDevices`
- `SDL_GetUserFolder`
- `SDL_GetVersion`
- `SDL_GetVideoDriver`
- `SDL_GlobDirectory`
- `SDL_HasARMSIMD`
- `SDL_HasAVX`
- `SDL_HasAVX2`
- `SDL_HasAVX512F`
- `SDL_HasAltiVec`
- `SDL_HasClipboardData`
- `SDL_HasClipboardText`
- `SDL_HasEvent`
- `SDL_HasEvents`
- `SDL_HasGamepad`
- `SDL_HasJoystick`
- `SDL_HasKeyboard`
- `SDL_HasLASX`
- `SDL_HasLSX`
- `SDL_HasMMX`
- `SDL_HasMouse`
- `SDL_HasNEON`
- `SDL_HasPrimarySelectionText`
- `SDL_HasProperty`
- `SDL_HasSSE`
- `SDL_HasSSE2`
- `SDL_HasSSE3`
- `SDL_HasSSE41`
- `SDL_HasSSE42`
- `SDL_HasScreenKeyboardSupport`
- `SDL_HideCursor`
- `SDL_Init`
- `SDL_InitSubSystem`
- `SDL_IsAudioDevicePhysical`
- `SDL_IsAudioDevicePlayback`
- `SDL_IsChromebook`
- `SDL_IsDeXMode`
- `SDL_IsGamepad`
- `SDL_IsJoystickVirtual`
- `SDL_IsMainThread`
- `SDL_IsMouseHaptic`
- `SDL_IsTV`
- `SDL_IsTablet`
- `SDL_JoystickEventsEnabled`
- `SDL_LoadFile`
- `SDL_LoadFileAsync`
- `SDL_LoadWAV`
- `SDL_LockJoysticks`
- `SDL_LockMutex`
- `SDL_LockProperties`
- `SDL_LockRWLockForReading`
- `SDL_LockRWLockForWriting`
- `SDL_LockSpinlock`
- `SDL_Log`
- `SDL_LogCritical`
- `SDL_LogDebug`
- `SDL_LogError`
- `SDL_LogInfo`
- `SDL_LogMessage`
- `SDL_LogMessageV`
- `SDL_LogTrace`
- `SDL_LogVerbose`
- `SDL_LogWarn`
- `SDL_MemoryBarrierAcquireFunction`
- `SDL_MemoryBarrierReleaseFunction`
- `SDL_Metal_DestroyView`
- `SDL_Metal_GetLayer`
- `SDL_MixAudio`
- `SDL_OnApplicationDidChangeStatusBarOrientation`
- `SDL_OnApplicationDidEnterBackground`
- `SDL_OnApplicationDidEnterForeground`
- `SDL_OnApplicationDidReceiveMemoryWarning`
- `SDL_OnApplicationWillEnterBackground`
- `SDL_OnApplicationWillEnterForeground`
- `SDL_OnApplicationWillTerminate`
- `SDL_OpenAudioDevice`
- `SDL_OpenURL`
- `SDL_OutOfMemory`
- `SDL_PauseAudioDevice`
- `SDL_PeepEvents`
- `SDL_PollEvent`
- `SDL_PremultiplyAlpha`
- `SDL_PumpEvents`
- `SDL_PushEvent`
- `SDL_Quit`
- `SDL_QuitSubSystem`
- `SDL_RegisterApp`
- `SDL_RegisterEvents`
- `SDL_ReloadGamepadMappings`
- `SDL_RemoveEventWatch`
- `SDL_RemoveHintCallback`
- `SDL_RemovePath`
- `SDL_RemoveTimer`
- `SDL_RenamePath`
- `SDL_RequestAndroidPermission`
- `SDL_ResetAssertionReport`
- `SDL_ResetHint`
- `SDL_ResetHints`
- `SDL_ResetKeyboard`
- `SDL_ResetLogPriorities`
- `SDL_ResumeAudioDevice`
- `SDL_RunApp`
- `SDL_RunOnMainThread`
- `SDL_SaveFile`
- `SDL_ScreenSaverEnabled`
- `SDL_SendAndroidBackButton`
- `SDL_SendAndroidMessage`
- `SDL_SetAppMetadata`
- `SDL_SetAppMetadataProperty`
- `SDL_SetAssertionHandler`
- `SDL_SetAtomicPointer`
- `SDL_SetAudioDeviceGain`
- `SDL_SetAudioPostmixCallback`
- `SDL_SetBooleanProperty`
- `SDL_SetClipboardData`
- `SDL_SetClipboardText`
- `SDL_SetCurrentThreadPriority`
- `SDL_SetError`
- `SDL_SetErrorV`
- `SDL_SetEventEnabled`
- `SDL_SetEventFilter`
- `SDL_SetFloatProperty`
- `SDL_SetGamepadEventsEnabled`
- `SDL_SetGamepadMapping`
- `SDL_SetHint`
- `SDL_SetHintWithPriority`
- `SDL_SetJoystickEventsEnabled`
- `SDL_SetLinuxThreadPriority`
- `SDL_SetLinuxThreadPriorityAndPolicy`
- `SDL_SetLogOutputFunction`
- `SDL_SetLogPriorities`
- `SDL_SetLogPriority`
- `SDL_SetLogPriorityPrefix`
- `SDL_SetMainReady`
- `SDL_SetMemoryFunctions`
- `SDL_SetModState`
- `SDL_SetNumberProperty`
- `SDL_SetPointerProperty`
- `SDL_SetPointerPropertyWithCleanup`
- `SDL_SetPrimarySelectionText`
- `SDL_SetRelativeMouseTransform`
- `SDL_SetScancodeName`
- `SDL_SetStringProperty`
- `SDL_SetTLS`
- `SDL_SetWindowsMessageHook`
- `SDL_SetX11EventHook`
- `SDL_SetiOSEventPump`
- `SDL_ShowAndroidToast`
- `SDL_ShowCursor`
- `SDL_ShowFileDialogWithProperties`
- `SDL_ShowOpenFileDialog`
- `SDL_ShowOpenFolderDialog`
- `SDL_ShowSaveFileDialog`
- `SDL_ShowSimpleMessageBox`
- `SDL_StepBackUTF8`
- `SDL_StepUTF8`
- `SDL_TimeFromWindows`
- `SDL_TimeToDateTime`
- `SDL_TimeToWindows`
- `SDL_TryLockMutex`
- `SDL_TryLockRWLockForReading`
- `SDL_TryLockRWLockForWriting`
- `SDL_TryLockSpinlock`
- `SDL_UCS4ToUTF8`
- `SDL_UnlockJoysticks`
- `SDL_UnlockMutex`
- `SDL_UnlockProperties`
- `SDL_UnlockRWLock`
- `SDL_UnlockSpinlock`
- `SDL_UnregisterApp`
- `SDL_UpdateGamepads`
- `SDL_UpdateJoysticks`
- `SDL_UpdateSensors`
- `SDL_UpdateTrays`
- `SDL_Vulkan_DestroySurface`
- `SDL_Vulkan_GetInstanceExtensions`
- `SDL_Vulkan_GetPresentationSupport`
- `SDL_Vulkan_GetVkGetInstanceProcAddr`
- `SDL_Vulkan_LoadLibrary`
- `SDL_Vulkan_UnloadLibrary`
- `SDL_WaitEvent`
- `SDL_WaitEventTimeout`
- `SDL_WarpMouseGlobal`
- `SDL_WasInit`
- `SDL_abs`
- `SDL_acos`
- `SDL_acosf`
- `SDL_aligned_alloc`
- `SDL_aligned_free`
- `SDL_asin`
- `SDL_asinf`
- `SDL_asprintf`
- `SDL_atan`
- `SDL_atan2`
- `SDL_atan2f`
- `SDL_atanf`
- `SDL_atof`
- `SDL_atoi`
- `SDL_bsearch`
- `SDL_bsearch_r`
- `SDL_calloc`
- `SDL_ceil`
- `SDL_ceilf`
- `SDL_copysign`
- `SDL_copysignf`
- `SDL_cos`
- `SDL_cosf`
- `SDL_crc16`
- `SDL_crc32`
- `SDL_exp`
- `SDL_expf`
- `SDL_fabs`
- `SDL_fabsf`
- `SDL_floor`
- `SDL_floorf`
- `SDL_fmod`
- `SDL_fmodf`
- `SDL_free`
- `SDL_getenv`
- `SDL_getenv_unsafe`
- `SDL_hid_ble_scan`
- `SDL_hid_device_change_count`
- `SDL_hid_exit`
- `SDL_hid_init`
- `SDL_iconv`
- `SDL_iconv_close`
- `SDL_iconv_open`
- `SDL_iconv_string`
- `SDL_isalnum`
- `SDL_isalpha`
- `SDL_isblank`
- `SDL_iscntrl`
- `SDL_isdigit`
- `SDL_isgraph`
- `SDL_isinf`
- `SDL_isinff`
- `SDL_islower`
- `SDL_isnan`
- `SDL_isnanf`
- `SDL_isprint`
- `SDL_ispunct`
- `SDL_isspace`
- `SDL_isupper`
- `SDL_isxdigit`
- `SDL_itoa`
- `SDL_lltoa`
- `SDL_log`
- `SDL_log10`
- `SDL_log10f`
- `SDL_logf`
- `SDL_lround`
- `SDL_lroundf`
- `SDL_ltoa`
- `SDL_malloc`
- `SDL_memcmp`
- `SDL_memcpy`
- `SDL_memmove`
- `SDL_memset`
- `SDL_memset4`
- `SDL_modf`
- `SDL_modff`
- `SDL_murmur3_32`
- `SDL_pow`
- `SDL_powf`
- `SDL_qsort`
- `SDL_qsort_r`
- `SDL_rand`
- `SDL_rand_bits`
- `SDL_rand_bits_r`
- `SDL_rand_r`
- `SDL_randf`
- `SDL_randf_r`
- `SDL_realloc`
- `SDL_round`
- `SDL_roundf`
- `SDL_scalbn`
- `SDL_scalbnf`
- `SDL_setenv_unsafe`
- `SDL_sin`
- `SDL_sinf`
- `SDL_snprintf`
- `SDL_sqrt`
- `SDL_sqrtf`
- `SDL_srand`
- `SDL_sscanf`
- `SDL_strcasecmp`
- `SDL_strcasestr`
- `SDL_strchr`
- `SDL_strcmp`
- `SDL_strdup`
- `SDL_strlcat`
- `SDL_strlcpy`
- `SDL_strlen`
- `SDL_strlwr`
- `SDL_strncasecmp`
- `SDL_strncmp`
- `SDL_strndup`
- `SDL_strnlen`
- `SDL_strnstr`
- `SDL_strpbrk`
- `SDL_strrchr`
- `SDL_strrev`
- `SDL_strstr`
- `SDL_strtod`
- `SDL_strtok_r`
- `SDL_strtol`
- `SDL_strtoll`
- `SDL_strtoul`
- `SDL_strtoull`
- `SDL_strupr`
- `SDL_swprintf`
- `SDL_tan`
- `SDL_tanf`
- `SDL_tolower`
- `SDL_toupper`
- `SDL_trunc`
- `SDL_truncf`
- `SDL_uitoa`
- `SDL_ulltoa`
- `SDL_ultoa`
- `SDL_unsetenv_unsafe`
- `SDL_utf8strlcpy`
- `SDL_utf8strlen`
- `SDL_utf8strnlen`
- `SDL_vasprintf`
- `SDL_vsnprintf`
- `SDL_vsscanf`
- `SDL_vswprintf`
- `SDL_wcscasecmp`
- `SDL_wcscmp`
- `SDL_wcsdup`
- `SDL_wcslcat`
- `SDL_wcslcpy`
- `SDL_wcslen`
- `SDL_wcsncasecmp`
- `SDL_wcsncmp`
- `SDL_wcsnlen`
- `SDL_wcsnstr`
- `SDL_wcsstr`
- `SDL_wcstol`

---
## SDL_Window
### 🏗️ Constructors / Factories
- `SDL_CreatePopupWindow`
- `SDL_CreateWindow`
- `SDL_CreateWindowWithProperties`
- `SDL_GL_GetCurrentWindow`
- `SDL_GetGrabbedWindow`
- `SDL_GetKeyboardFocus`
- `SDL_GetMouseFocus`
- `SDL_GetRenderWindow`
- `SDL_GetWindowFromEvent`
- `SDL_GetWindowFromID`
- `SDL_GetWindowParent`
- `SDL_GetWindows`
### ⚙️ Methods
- `SDL_ClearComposition`
- `SDL_EGL_GetWindowSurface`
- `SDL_FlashWindow`
- `SDL_GL_CreateContext`
- `SDL_GL_MakeCurrent`
- `SDL_GL_SwapWindow`
- `SDL_GetDisplayForWindow`
- `SDL_GetTextInputArea`
- `SDL_GetWindowAspectRatio`
- `SDL_GetWindowBordersSize`
- `SDL_GetWindowDisplayScale`
- `SDL_GetWindowFlags`
- `SDL_GetWindowICCProfile`
- `SDL_GetWindowID`
- `SDL_GetWindowKeyboardGrab`
- `SDL_GetWindowMaximumSize`
- `SDL_GetWindowMinimumSize`
- `SDL_GetWindowMouseGrab`
- `SDL_GetWindowOpacity`
- `SDL_GetWindowPixelDensity`
- `SDL_GetWindowPixelFormat`
- `SDL_GetWindowPosition`
- `SDL_GetWindowProgressState`
- `SDL_GetWindowProgressValue`
- `SDL_GetWindowProperties`
- `SDL_GetWindowRelativeMouseMode`
- `SDL_GetWindowSafeArea`
- `SDL_GetWindowSize`
- `SDL_GetWindowSizeInPixels`
- `SDL_GetWindowSurfaceVSync`
- `SDL_GetWindowTitle`
- `SDL_HideWindow`
- `SDL_MaximizeWindow`
- `SDL_Metal_CreateView`
- `SDL_MinimizeWindow`
- `SDL_RaiseWindow`
- `SDL_RestoreWindow`
- `SDL_ScreenKeyboardShown`
- `SDL_SetTextInputArea`
- `SDL_SetWindowAlwaysOnTop`
- `SDL_SetWindowAspectRatio`
- `SDL_SetWindowBordered`
- `SDL_SetWindowFillDocument`
- `SDL_SetWindowFocusable`
- `SDL_SetWindowFullscreen`
- `SDL_SetWindowFullscreenMode`
- `SDL_SetWindowHitTest`
- `SDL_SetWindowIcon`
- `SDL_SetWindowKeyboardGrab`
- `SDL_SetWindowMaximumSize`
- `SDL_SetWindowMinimumSize`
- `SDL_SetWindowModal`
- `SDL_SetWindowMouseGrab`
- `SDL_SetWindowMouseRect`
- `SDL_SetWindowOpacity`
- `SDL_SetWindowParent`
- `SDL_SetWindowPosition`
- `SDL_SetWindowProgressState`
- `SDL_SetWindowProgressValue`
- `SDL_SetWindowRelativeMouseMode`
- `SDL_SetWindowResizable`
- `SDL_SetWindowShape`
- `SDL_SetWindowSize`
- `SDL_SetWindowSurfaceVSync`
- `SDL_SetWindowTitle`
- `SDL_SetiOSAnimationCallback`
- `SDL_ShowWindow`
- `SDL_ShowWindowSystemMenu`
- `SDL_StartTextInput`
- `SDL_StartTextInputWithProperties`
- `SDL_StopTextInput`
- `SDL_SyncWindow`
- `SDL_TextInputActive`
- `SDL_UpdateWindowSurface`
- `SDL_UpdateWindowSurfaceRects`
- `SDL_Vulkan_CreateSurface`
- `SDL_WarpMouseInWindow`
- `SDL_WindowHasSurface`
### ♻️ Destructors
- `SDL_DestroyWindow`
- `SDL_DestroyWindowSurface`

---
## SDL_Renderer
### 🏗️ Constructors / Factories
- `SDL_CreateGPURenderer`
- `SDL_CreateRenderer`
- `SDL_CreateRendererWithProperties`
- `SDL_CreateSoftwareRenderer`
- `SDL_GetRenderer`
- `SDL_GetRendererFromTexture`
### ⚙️ Methods
- `SDL_AddVulkanRenderSemaphores`
- `SDL_ConvertEventToRenderCoordinates`
- `SDL_FlushRenderer`
- `SDL_GetCurrentRenderOutputSize`
- `SDL_GetDefaultTextureScaleMode`
- `SDL_GetRenderClipRect`
- `SDL_GetRenderColorScale`
- `SDL_GetRenderDrawBlendMode`
- `SDL_GetRenderDrawColor`
- `SDL_GetRenderDrawColorFloat`
- `SDL_GetRenderLogicalPresentation`
- `SDL_GetRenderLogicalPresentationRect`
- `SDL_GetRenderMetalCommandEncoder`
- `SDL_GetRenderMetalLayer`
- `SDL_GetRenderOutputSize`
- `SDL_GetRenderSafeArea`
- `SDL_GetRenderScale`
- `SDL_GetRenderTextureAddressMode`
- `SDL_GetRenderVSync`
- `SDL_GetRenderViewport`
- `SDL_GetRendererName`
- `SDL_GetRendererProperties`
- `SDL_RenderClear`
- `SDL_RenderClipEnabled`
- `SDL_RenderCoordinatesFromWindow`
- `SDL_RenderCoordinatesToWindow`
- `SDL_RenderDebugText`
- `SDL_RenderDebugTextFormat`
- `SDL_RenderFillRect`
- `SDL_RenderFillRects`
- `SDL_RenderGeometry`
- `SDL_RenderGeometryRaw`
- `SDL_RenderLine`
- `SDL_RenderLines`
- `SDL_RenderPoint`
- `SDL_RenderPoints`
- `SDL_RenderPresent`
- `SDL_RenderRect`
- `SDL_RenderRects`
- `SDL_RenderTexture`
- `SDL_RenderTexture9Grid`
- `SDL_RenderTexture9GridTiled`
- `SDL_RenderTextureAffine`
- `SDL_RenderTextureRotated`
- `SDL_RenderTextureTiled`
- `SDL_RenderViewportSet`
- `SDL_SetDefaultTextureScaleMode`
- `SDL_SetGPURenderState`
- `SDL_SetRenderClipRect`
- `SDL_SetRenderColorScale`
- `SDL_SetRenderDrawBlendMode`
- `SDL_SetRenderDrawColor`
- `SDL_SetRenderDrawColorFloat`
- `SDL_SetRenderLogicalPresentation`
- `SDL_SetRenderScale`
- `SDL_SetRenderTarget`
- `SDL_SetRenderTextureAddressMode`
- `SDL_SetRenderVSync`
- `SDL_SetRenderViewport`
### ♻️ Destructors
- `SDL_DestroyRenderer`

---
## SDL_Surface
### 🏗️ Constructors / Factories
- `SDL_AcquireCameraFrame`
- `SDL_ConvertSurface`
- `SDL_ConvertSurfaceAndColorspace`
- `SDL_CreateSurface`
- `SDL_CreateSurfaceFrom`
- `SDL_DuplicateSurface`
- `SDL_GetSurfaceImages`
- `SDL_GetWindowSurface`
- `SDL_LoadBMP`
- `SDL_LoadBMP_IO`
- `SDL_LoadPNG`
- `SDL_LoadPNG_IO`
- `SDL_LoadSurface`
- `SDL_LoadSurface_IO`
- `SDL_RenderReadPixels`
- `SDL_RotateSurface`
- `SDL_ScaleSurface`
### ⚙️ Methods
- `SDL_AddSurfaceAlternateImage`
- `SDL_BlitSurface`
- `SDL_BlitSurface9Grid`
- `SDL_BlitSurfaceScaled`
- `SDL_BlitSurfaceTiled`
- `SDL_BlitSurfaceTiledWithScale`
- `SDL_BlitSurfaceUnchecked`
- `SDL_BlitSurfaceUncheckedScaled`
- `SDL_ClearSurface`
- `SDL_FillSurfaceRect`
- `SDL_FillSurfaceRects`
- `SDL_FlipSurface`
- `SDL_GetSurfaceAlphaMod`
- `SDL_GetSurfaceBlendMode`
- `SDL_GetSurfaceClipRect`
- `SDL_GetSurfaceColorKey`
- `SDL_GetSurfaceColorMod`
- `SDL_GetSurfaceColorspace`
- `SDL_GetSurfaceProperties`
- `SDL_LockSurface`
- `SDL_MapSurfaceRGB`
- `SDL_MapSurfaceRGBA`
- `SDL_PremultiplySurfaceAlpha`
- `SDL_ReadSurfacePixel`
- `SDL_ReadSurfacePixelFloat`
- `SDL_RemoveSurfaceAlternateImages`
- `SDL_SaveBMP`
- `SDL_SaveBMP_IO`
- `SDL_SavePNG`
- `SDL_SavePNG_IO`
- `SDL_SetSurfaceAlphaMod`
- `SDL_SetSurfaceBlendMode`
- `SDL_SetSurfaceClipRect`
- `SDL_SetSurfaceColorKey`
- `SDL_SetSurfaceColorMod`
- `SDL_SetSurfaceColorspace`
- `SDL_SetSurfacePalette`
- `SDL_SetSurfaceRLE`
- `SDL_StretchSurface`
- `SDL_SurfaceHasAlternateImages`
- `SDL_SurfaceHasColorKey`
- `SDL_SurfaceHasRLE`
- `SDL_UnlockSurface`
- `SDL_WriteSurfacePixel`
- `SDL_WriteSurfacePixelFloat`
### ♻️ Destructors
- `SDL_DestroySurface`

---
## SDL_IOStream
### 🏗️ Constructors / Factories
- `SDL_GetProcessInput`
- `SDL_GetProcessOutput`
- `SDL_IOFromConstMem`
- `SDL_IOFromDynamicMem`
- `SDL_IOFromFile`
- `SDL_IOFromMem`
- `SDL_OpenIO`
### ⚙️ Methods
- `SDL_AddGamepadMappingsFromIO`
- `SDL_FlushIO`
- `SDL_GetIOProperties`
- `SDL_GetIOSize`
- `SDL_GetIOStatus`
- `SDL_IOprintf`
- `SDL_IOvprintf`
- `SDL_LoadFile_IO`
- `SDL_LoadWAV_IO`
- `SDL_ReadIO`
- `SDL_ReadS16BE`
- `SDL_ReadS16LE`
- `SDL_ReadS32BE`
- `SDL_ReadS32LE`
- `SDL_ReadS64BE`
- `SDL_ReadS64LE`
- `SDL_ReadS8`
- `SDL_ReadU16BE`
- `SDL_ReadU16LE`
- `SDL_ReadU32BE`
- `SDL_ReadU32LE`
- `SDL_ReadU64BE`
- `SDL_ReadU64LE`
- `SDL_ReadU8`
- `SDL_SaveFile_IO`
- `SDL_SeekIO`
- `SDL_TellIO`
- `SDL_WriteIO`
- `SDL_WriteS16BE`
- `SDL_WriteS16LE`
- `SDL_WriteS32BE`
- `SDL_WriteS32LE`
- `SDL_WriteS64BE`
- `SDL_WriteS64LE`
- `SDL_WriteS8`
- `SDL_WriteU16BE`
- `SDL_WriteU16LE`
- `SDL_WriteU32BE`
- `SDL_WriteU32LE`
- `SDL_WriteU64BE`
- `SDL_WriteU64LE`
- `SDL_WriteU8`
### ♻️ Destructors
- `SDL_CloseIO`

---
## SDL_Gamepad
### 🏗️ Constructors / Factories
- `SDL_GetGamepadFromID`
- `SDL_GetGamepadFromPlayerIndex`
- `SDL_OpenGamepad`
### ⚙️ Methods
- `SDL_GamepadConnected`
- `SDL_GamepadHasAxis`
- `SDL_GamepadHasButton`
- `SDL_GamepadHasSensor`
- `SDL_GamepadSensorEnabled`
- `SDL_GetGamepadAppleSFSymbolsNameForAxis`
- `SDL_GetGamepadAppleSFSymbolsNameForButton`
- `SDL_GetGamepadAxis`
- `SDL_GetGamepadButton`
- `SDL_GetGamepadButtonLabel`
- `SDL_GetGamepadConnectionState`
- `SDL_GetGamepadFirmwareVersion`
- `SDL_GetGamepadID`
- `SDL_GetGamepadMapping`
- `SDL_GetGamepadName`
- `SDL_GetGamepadPath`
- `SDL_GetGamepadPlayerIndex`
- `SDL_GetGamepadPowerInfo`
- `SDL_GetGamepadProduct`
- `SDL_GetGamepadProductVersion`
- `SDL_GetGamepadProperties`
- `SDL_GetGamepadSensorData`
- `SDL_GetGamepadSensorDataRate`
- `SDL_GetGamepadSerial`
- `SDL_GetGamepadSteamHandle`
- `SDL_GetGamepadTouchpadFinger`
- `SDL_GetGamepadType`
- `SDL_GetGamepadVendor`
- `SDL_GetNumGamepadTouchpadFingers`
- `SDL_GetNumGamepadTouchpads`
- `SDL_GetRealGamepadType`
- `SDL_RumbleGamepad`
- `SDL_RumbleGamepadTriggers`
- `SDL_SendGamepadEffect`
- `SDL_SetGamepadLED`
- `SDL_SetGamepadPlayerIndex`
- `SDL_SetGamepadSensorEnabled`
### ♻️ Destructors
- `SDL_CloseGamepad`

---
## SDL_Joystick
### 🏗️ Constructors / Factories
- `SDL_GetGamepadJoystick`
- `SDL_GetJoystickFromID`
- `SDL_GetJoystickFromPlayerIndex`
- `SDL_OpenJoystick`
### ⚙️ Methods
- `SDL_GetJoystickAxis`
- `SDL_GetJoystickAxisInitialState`
- `SDL_GetJoystickBall`
- `SDL_GetJoystickButton`
- `SDL_GetJoystickConnectionState`
- `SDL_GetJoystickFirmwareVersion`
- `SDL_GetJoystickHat`
- `SDL_GetJoystickID`
- `SDL_GetJoystickName`
- `SDL_GetJoystickPath`
- `SDL_GetJoystickPlayerIndex`
- `SDL_GetJoystickPowerInfo`
- `SDL_GetJoystickProduct`
- `SDL_GetJoystickProductVersion`
- `SDL_GetJoystickProperties`
- `SDL_GetJoystickSerial`
- `SDL_GetJoystickType`
- `SDL_GetJoystickVendor`
- `SDL_GetNumJoystickAxes`
- `SDL_GetNumJoystickBalls`
- `SDL_GetNumJoystickButtons`
- `SDL_GetNumJoystickHats`
- `SDL_IsJoystickHaptic`
- `SDL_JoystickConnected`
- `SDL_RumbleJoystick`
- `SDL_RumbleJoystickTriggers`
- `SDL_SendJoystickEffect`
- `SDL_SendJoystickVirtualSensorData`
- `SDL_SetJoystickLED`
- `SDL_SetJoystickPlayerIndex`
- `SDL_SetJoystickVirtualAxis`
- `SDL_SetJoystickVirtualBall`
- `SDL_SetJoystickVirtualButton`
- `SDL_SetJoystickVirtualHat`
- `SDL_SetJoystickVirtualTouchpad`
### ♻️ Destructors
- `SDL_CloseJoystick`

---
## SDL_GPUDevice
### 🏗️ Constructors / Factories
- `SDL_CreateGPUDevice`
- `SDL_CreateGPUDeviceWithProperties`
- `SDL_GetGPURendererDevice`
### ⚙️ Methods
- `SDL_ClaimWindowForGPUDevice`
- `SDL_GDKResumeGPU`
- `SDL_GDKSuspendGPU`
- `SDL_GPUTextureSupportsFormat`
- `SDL_GPUTextureSupportsSampleCount`
- `SDL_GetGPUDeviceDriver`
- `SDL_GetGPUDeviceProperties`
- `SDL_GetGPUShaderFormats`
- `SDL_GetGPUSwapchainTextureFormat`
- `SDL_MapGPUTransferBuffer`
- `SDL_QueryGPUFence`
- `SDL_ReleaseGPUBuffer`
- `SDL_ReleaseGPUComputePipeline`
- `SDL_ReleaseGPUFence`
- `SDL_ReleaseGPUGraphicsPipeline`
- `SDL_ReleaseGPUSampler`
- `SDL_ReleaseGPUShader`
- `SDL_ReleaseGPUTexture`
- `SDL_ReleaseGPUTransferBuffer`
- `SDL_ReleaseWindowFromGPUDevice`
- `SDL_SetGPUAllowedFramesInFlight`
- `SDL_SetGPUBufferName`
- `SDL_SetGPUSwapchainParameters`
- `SDL_SetGPUTextureName`
- `SDL_UnmapGPUTransferBuffer`
- `SDL_WaitForGPUFences`
- `SDL_WaitForGPUIdle`
- `SDL_WaitForGPUSwapchain`
- `SDL_WindowSupportsGPUPresentMode`
- `SDL_WindowSupportsGPUSwapchainComposition`
### ♻️ Destructors
- `SDL_DestroyGPUDevice`

---
## SDL_AudioStream
### 🏗️ Constructors / Factories
- `SDL_CreateAudioStream`
- `SDL_OpenAudioDeviceStream`
### ⚙️ Methods
- `SDL_AudioStreamDevicePaused`
- `SDL_ClearAudioStream`
- `SDL_FlushAudioStream`
- `SDL_GetAudioStreamAvailable`
- `SDL_GetAudioStreamData`
- `SDL_GetAudioStreamDevice`
- `SDL_GetAudioStreamFormat`
- `SDL_GetAudioStreamFrequencyRatio`
- `SDL_GetAudioStreamGain`
- `SDL_GetAudioStreamInputChannelMap`
- `SDL_GetAudioStreamOutputChannelMap`
- `SDL_GetAudioStreamProperties`
- `SDL_GetAudioStreamQueued`
- `SDL_LockAudioStream`
- `SDL_PauseAudioStreamDevice`
- `SDL_PutAudioStreamData`
- `SDL_PutAudioStreamDataNoCopy`
- `SDL_PutAudioStreamPlanarData`
- `SDL_ResumeAudioStreamDevice`
- `SDL_SetAudioStreamFormat`
- `SDL_SetAudioStreamFrequencyRatio`
- `SDL_SetAudioStreamGain`
- `SDL_SetAudioStreamGetCallback`
- `SDL_SetAudioStreamInputChannelMap`
- `SDL_SetAudioStreamOutputChannelMap`
- `SDL_SetAudioStreamPutCallback`
- `SDL_UnbindAudioStream`
- `SDL_UnbindAudioStreams`
- `SDL_UnlockAudioStream`
### ♻️ Destructors
- `SDL_DestroyAudioStream`

---
## SDL_Texture
### 🏗️ Constructors / Factories
- `SDL_CreateTexture`
- `SDL_CreateTextureFromSurface`
- `SDL_CreateTextureWithProperties`
- `SDL_GetRenderTarget`
### ⚙️ Methods
- `SDL_GetTextureAlphaMod`
- `SDL_GetTextureAlphaModFloat`
- `SDL_GetTextureBlendMode`
- `SDL_GetTextureColorMod`
- `SDL_GetTextureColorModFloat`
- `SDL_GetTextureProperties`
- `SDL_GetTextureScaleMode`
- `SDL_GetTextureSize`
- `SDL_LockTexture`
- `SDL_LockTextureToSurface`
- `SDL_SetTextureAlphaMod`
- `SDL_SetTextureAlphaModFloat`
- `SDL_SetTextureBlendMode`
- `SDL_SetTextureColorMod`
- `SDL_SetTextureColorModFloat`
- `SDL_SetTexturePalette`
- `SDL_SetTextureScaleMode`
- `SDL_UnlockTexture`
- `SDL_UpdateNVTexture`
- `SDL_UpdateTexture`
- `SDL_UpdateYUVTexture`
### ♻️ Destructors
- `SDL_DestroyTexture`

---
## SDL_Haptic
### 🏗️ Constructors / Factories
- `SDL_GetHapticFromID`
- `SDL_OpenHaptic`
- `SDL_OpenHapticFromJoystick`
- `SDL_OpenHapticFromMouse`
### ⚙️ Methods
- `SDL_CreateHapticEffect`
- `SDL_GetHapticEffectStatus`
- `SDL_GetHapticFeatures`
- `SDL_GetHapticID`
- `SDL_GetHapticName`
- `SDL_GetMaxHapticEffects`
- `SDL_GetMaxHapticEffectsPlaying`
- `SDL_GetNumHapticAxes`
- `SDL_HapticEffectSupported`
- `SDL_HapticRumbleSupported`
- `SDL_InitHapticRumble`
- `SDL_PauseHaptic`
- `SDL_PlayHapticRumble`
- `SDL_ResumeHaptic`
- `SDL_RunHapticEffect`
- `SDL_SetHapticAutocenter`
- `SDL_SetHapticGain`
- `SDL_StopHapticEffect`
- `SDL_StopHapticEffects`
- `SDL_StopHapticRumble`
- `SDL_UpdateHapticEffect`
### ♻️ Destructors
- `SDL_CloseHaptic`
- `SDL_DestroyHapticEffect`

---
## SDL_GPURenderPass
### 🏗️ Constructors / Factories
- `SDL_BeginGPURenderPass`
### ⚙️ Methods
- `SDL_BindGPUFragmentSamplers`
- `SDL_BindGPUFragmentStorageBuffers`
- `SDL_BindGPUFragmentStorageTextures`
- `SDL_BindGPUGraphicsPipeline`
- `SDL_BindGPUIndexBuffer`
- `SDL_BindGPUVertexBuffers`
- `SDL_BindGPUVertexSamplers`
- `SDL_BindGPUVertexStorageBuffers`
- `SDL_BindGPUVertexStorageTextures`
- `SDL_DrawGPUIndexedPrimitives`
- `SDL_DrawGPUIndexedPrimitivesIndirect`
- `SDL_DrawGPUPrimitives`
- `SDL_DrawGPUPrimitivesIndirect`
- `SDL_EndGPURenderPass`
- `SDL_SetGPUBlendConstants`
- `SDL_SetGPUScissor`
- `SDL_SetGPUStencilReference`
- `SDL_SetGPUViewport`

---
## SDL_hid_device
### 🏗️ Constructors / Factories
- `SDL_hid_open`
- `SDL_hid_open_path`
### ⚙️ Methods
- `SDL_hid_close`
- `SDL_hid_get_feature_report`
- `SDL_hid_get_indexed_string`
- `SDL_hid_get_input_report`
- `SDL_hid_get_manufacturer_string`
- `SDL_hid_get_product_string`
- `SDL_hid_get_properties`
- `SDL_hid_get_report_descriptor`
- `SDL_hid_get_serial_number_string`
- `SDL_hid_read`
- `SDL_hid_read_timeout`
- `SDL_hid_send_feature_report`
- `SDL_hid_set_nonblocking`
- `SDL_hid_write`

---
## SDL_Storage
### 🏗️ Constructors / Factories
- `SDL_OpenFileStorage`
- `SDL_OpenStorage`
- `SDL_OpenTitleStorage`
- `SDL_OpenUserStorage`
### ⚙️ Methods
- `SDL_CopyStorageFile`
- `SDL_CreateStorageDirectory`
- `SDL_EnumerateStorageDirectory`
- `SDL_GetStorageFileSize`
- `SDL_GetStoragePathInfo`
- `SDL_GetStorageSpaceRemaining`
- `SDL_GlobStorageDirectory`
- `SDL_ReadStorageFile`
- `SDL_RemoveStoragePath`
- `SDL_RenameStoragePath`
- `SDL_StorageReady`
- `SDL_WriteStorageFile`
### ♻️ Destructors
- `SDL_CloseStorage`

---
## SDL_GPUCommandBuffer
### 🏗️ Constructors / Factories
- `SDL_AcquireGPUCommandBuffer`
### ⚙️ Methods
- `SDL_AcquireGPUSwapchainTexture`
- `SDL_BlitGPUTexture`
- `SDL_CancelGPUCommandBuffer`
- `SDL_GenerateMipmapsForGPUTexture`
- `SDL_InsertGPUDebugLabel`
- `SDL_PopGPUDebugGroup`
- `SDL_PushGPUComputeUniformData`
- `SDL_PushGPUDebugGroup`
- `SDL_PushGPUFragmentUniformData`
- `SDL_PushGPUVertexUniformData`
- `SDL_SubmitGPUCommandBuffer`
- `SDL_WaitAndAcquireGPUSwapchainTexture`

---
## SDL_TrayEntry
### 🏗️ Constructors / Factories
- `SDL_GetTrayEntries`
- `SDL_GetTrayMenuParentEntry`
- `SDL_InsertTrayEntryAt`
### ⚙️ Methods
- `SDL_ClickTrayEntry`
- `SDL_GetTrayEntryChecked`
- `SDL_GetTrayEntryEnabled`
- `SDL_GetTrayEntryLabel`
- `SDL_RemoveTrayEntry`
- `SDL_SetTrayEntryCallback`
- `SDL_SetTrayEntryChecked`
- `SDL_SetTrayEntryEnabled`
- `SDL_SetTrayEntryLabel`

---
## SDL_GPUCopyPass
### 🏗️ Constructors / Factories
- `SDL_BeginGPUCopyPass`
### ⚙️ Methods
- `SDL_CopyGPUBufferToBuffer`
- `SDL_CopyGPUTextureToTexture`
- `SDL_DownloadFromGPUBuffer`
- `SDL_DownloadFromGPUTexture`
- `SDL_EndGPUCopyPass`
- `SDL_UploadToGPUBuffer`
- `SDL_UploadToGPUTexture`

---
## SDL_GPUComputePass
### 🏗️ Constructors / Factories
- `SDL_BeginGPUComputePass`
### ⚙️ Methods
- `SDL_BindGPUComputePipeline`
- `SDL_BindGPUComputeSamplers`
- `SDL_BindGPUComputeStorageBuffers`
- `SDL_BindGPUComputeStorageTextures`
- `SDL_DispatchGPUCompute`
- `SDL_DispatchGPUComputeIndirect`
- `SDL_EndGPUComputePass`

---
## SDL_Sensor
### 🏗️ Constructors / Factories
- `SDL_GetSensorFromID`
- `SDL_OpenSensor`
### ⚙️ Methods
- `SDL_GetSensorData`
- `SDL_GetSensorID`
- `SDL_GetSensorName`
- `SDL_GetSensorNonPortableType`
- `SDL_GetSensorProperties`
- `SDL_GetSensorType`
### ♻️ Destructors
- `SDL_CloseSensor`

---
## SDL_Camera
### 🏗️ Constructors / Factories
- `SDL_OpenCamera`
### ⚙️ Methods
- `SDL_GetCameraFormat`
- `SDL_GetCameraID`
- `SDL_GetCameraPermissionState`
- `SDL_GetCameraProperties`
- `SDL_ReleaseCameraFrame`
### ♻️ Destructors
- `SDL_CloseCamera`

---
## SDL_Rect
### 🏗️ Constructors / Factories
- `SDL_GetWindowMouseRect`
### ⚙️ Methods
- `SDL_GetDisplayForRect`
- `SDL_GetRectAndLineIntersection`
- `SDL_GetRectIntersection`
- `SDL_GetRectUnion`
- `SDL_HasRectIntersection`

---
## SDL_Semaphore
### 🏗️ Constructors / Factories
- `SDL_CreateSemaphore`
### ⚙️ Methods
- `SDL_GetSemaphoreValue`
- `SDL_SignalSemaphore`
- `SDL_TryWaitSemaphore`
- `SDL_WaitSemaphore`
- `SDL_WaitSemaphoreTimeout`
### ♻️ Destructors
- `SDL_DestroySemaphore`

---
## SDL_Thread
### 🏗️ Constructors / Factories
- `SDL_CreateThread`
- `SDL_CreateThreadRuntime`
- `SDL_CreateThreadWithProperties`
- `SDL_CreateThreadWithPropertiesRuntime`
### ⚙️ Methods
- `SDL_DetachThread`
- `SDL_GetThreadID`
- `SDL_GetThreadName`
- `SDL_GetThreadState`
- `SDL_WaitThread`

---
## SDL_AtomicU32
### ⚙️ Methods
- `SDL_AddAtomicU32`
- `SDL_CompareAndSwapAtomicU32`
- `SDL_GetAtomicU32`
- `SDL_SetAtomicU32`

---
## SDL_Environment
### 🏗️ Constructors / Factories
- `SDL_CreateEnvironment`
- `SDL_GetEnvironment`
### ⚙️ Methods
- `SDL_GetEnvironmentVariable`
- `SDL_GetEnvironmentVariables`
- `SDL_SetEnvironmentVariable`
- `SDL_UnsetEnvironmentVariable`
### ♻️ Destructors
- `SDL_DestroyEnvironment`

---
## SDL_Process
### 🏗️ Constructors / Factories
- `SDL_CreateProcess`
- `SDL_CreateProcessWithProperties`
### ⚙️ Methods
- `SDL_GetProcessProperties`
- `SDL_KillProcess`
- `SDL_ReadProcess`
- `SDL_WaitProcess`
### ♻️ Destructors
- `SDL_DestroyProcess`

---
## SDL_FRect
### ⚙️ Methods
- `SDL_GetRectAndLineIntersectionFloat`
- `SDL_GetRectIntersectionFloat`
- `SDL_GetRectUnionFloat`
- `SDL_HasRectIntersectionFloat`

---
## SDL_AtomicInt
### ⚙️ Methods
- `SDL_AddAtomicInt`
- `SDL_CompareAndSwapAtomicInt`
- `SDL_GetAtomicInt`
- `SDL_SetAtomicInt`

---
## SDL_Condition
### 🏗️ Constructors / Factories
- `SDL_CreateCondition`
### ⚙️ Methods
- `SDL_BroadcastCondition`
- `SDL_SignalCondition`
- `SDL_WaitCondition`
- `SDL_WaitConditionTimeout`
### ♻️ Destructors
- `SDL_DestroyCondition`

---
## SDL_InitState
### ⚙️ Methods
- `SDL_SetInitialized`
- `SDL_ShouldInit`
- `SDL_ShouldQuit`

---
## SDL_GUID
### 🏗️ Constructors / Factories
- `SDL_GetGamepadGUIDForID`
- `SDL_GetJoystickGUID`
- `SDL_GetJoystickGUIDForID`
- `SDL_StringToGUID`
### ⚙️ Methods
- `SDL_GUIDToString`
- `SDL_GetGamepadMappingForGUID`
- `SDL_GetJoystickGUIDInfo`

---
## SDL_AsyncIO
### 🏗️ Constructors / Factories
- `SDL_AsyncIOFromFile`
### ⚙️ Methods
- `SDL_GetAsyncIOSize`
- `SDL_ReadAsyncIO`
- `SDL_WriteAsyncIO`
### ♻️ Destructors
- `SDL_CloseAsyncIO`

---
## SDL_AsyncIOQueue
### 🏗️ Constructors / Factories
- `SDL_CreateAsyncIOQueue`
### ⚙️ Methods
- `SDL_GetAsyncIOResult`
- `SDL_SignalAsyncIOQueue`
- `SDL_WaitAsyncIOResult`
### ♻️ Destructors
- `SDL_DestroyAsyncIOQueue`

---
## SDL_Point
### ⚙️ Methods
- `SDL_GetDisplayForPoint`
- `SDL_GetRectEnclosingPoints`

---
## SDL_PixelFormatDetails
### 🏗️ Constructors / Factories
- `SDL_GetPixelFormatDetails`
### ⚙️ Methods
- `SDL_MapRGB`
- `SDL_MapRGBA`

---
## SDL_SharedObject
### 🏗️ Constructors / Factories
- `SDL_LoadObject`
### ⚙️ Methods
- `SDL_LoadFunction`
- `SDL_UnloadObject`

---
## SDL_Tray
### 🏗️ Constructors / Factories
- `SDL_CreateTray`
- `SDL_GetTrayMenuParentTray`
### ⚙️ Methods
- `SDL_SetTrayIcon`
- `SDL_SetTrayTooltip`
### ♻️ Destructors
- `SDL_DestroyTray`

---
## SDL_VirtualJoystickDesc
### ⚙️ Methods
- `SDL_AttachVirtualJoystick`

---
## SDL_AssertData
### 🏗️ Constructors / Factories
- `SDL_GetAssertionReport`
### ⚙️ Methods
- `SDL_ReportAssertion`

---
## SDL_FPoint
### ⚙️ Methods
- `SDL_GetRectEnclosingPointsFloat`

---
## SDL_MessageBoxData
### ⚙️ Methods
- `SDL_ShowMessageBox`

---
## SDL_AudioSpec
### ⚙️ Methods
- `SDL_ConvertAudioSamples`

---
## SDL_hid_device_info
### 🏗️ Constructors / Factories
- `SDL_hid_enumerate`
- `SDL_hid_get_device_info`
### ⚙️ Methods
- `SDL_hid_free_enumeration`

---
## SDL_DateTime
### ⚙️ Methods
- `SDL_DateTimeToTime`

---
## SDL_Palette
### 🏗️ Constructors / Factories
- `SDL_CreatePalette`
- `SDL_CreateSurfacePalette`
- `SDL_GetSurfacePalette`
- `SDL_GetTexturePalette`
### ⚙️ Methods
- `SDL_SetPaletteColors`
### ♻️ Destructors
- `SDL_DestroyPalette`

---
## SDL_Cursor
### 🏗️ Constructors / Factories
- `SDL_CreateColorCursor`
- `SDL_CreateCursor`
- `SDL_GetCursor`
- `SDL_GetDefaultCursor`
### ⚙️ Methods
- `SDL_SetCursor`
### ♻️ Destructors
- `SDL_DestroyCursor`

---
## SDL_GPURenderState
### 🏗️ Constructors / Factories
- `SDL_CreateGPURenderState`
### ⚙️ Methods
- `SDL_SetGPURenderStateFragmentUniforms`
### ♻️ Destructors
- `SDL_DestroyGPURenderState`

---
## SDL_GPUGraphicsPipeline
### 🏗️ Constructors / Factories
- `SDL_CreateGPUGraphicsPipeline`

---
## SDL_GPUComputePipeline
### 🏗️ Constructors / Factories
- `SDL_CreateGPUComputePipeline`

---
## SDL_GPUBuffer
### 🏗️ Constructors / Factories
- `SDL_CreateGPUBuffer`

---
## SDL_RWLock
### 🏗️ Constructors / Factories
- `SDL_CreateRWLock`
### ♻️ Destructors
- `SDL_DestroyRWLock`

---
## SDL_GPUTransferBuffer
### 🏗️ Constructors / Factories
- `SDL_CreateGPUTransferBuffer`

---
## SDL_DisplayMode
### 🏗️ Constructors / Factories
- `SDL_GetCurrentDisplayMode`
- `SDL_GetDesktopDisplayMode`
- `SDL_GetFullscreenDisplayModes`
- `SDL_GetWindowFullscreenMode`

---
## SDL_Locale
### 🏗️ Constructors / Factories
- `SDL_GetPreferredLocales`

---
## SDL_GPUFence
### 🏗️ Constructors / Factories
- `SDL_SubmitGPUCommandBufferAndAcquireFence`

---
## SDL_GPUShader
### 🏗️ Constructors / Factories
- `SDL_CreateGPUShader`

---
## SDL_GamepadBinding
### 🏗️ Constructors / Factories
- `SDL_GetGamepadBindings`

---
## SDL_TrayMenu
### 🏗️ Constructors / Factories
- `SDL_CreateTrayMenu`
- `SDL_CreateTraySubmenu`
- `SDL_GetTrayEntryParent`
- `SDL_GetTrayMenu`
- `SDL_GetTraySubmenu`

---
## SDL_CameraSpec
### 🏗️ Constructors / Factories
- `SDL_GetCameraSupportedFormats`

---
## SDL_GPUTexture
### 🏗️ Constructors / Factories
- `SDL_CreateGPUTexture`

---
## SDL_GPUSampler
### 🏗️ Constructors / Factories
- `SDL_CreateGPUSampler`

---
## SDL_Mutex
### 🏗️ Constructors / Factories
- `SDL_CreateMutex`
### ♻️ Destructors
- `SDL_DestroyMutex`

---
## SDL_Finger
### 🏗️ Constructors / Factories
- `SDL_GetTouchFingers`

---
