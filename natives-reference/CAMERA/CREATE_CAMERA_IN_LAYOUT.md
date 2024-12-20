---
description: No description available
---

# CREATE\_CAMERA\_IN\_LAYOUT

```cpp
Camera CREATE_CAMERA_IN_LAYOUT(Layout _Layout, const char* _Unk1, int _Unk2);
```

### Examples

#### Create a camera

```cpp
Layout layout = OBJECT::GET_AMBIENT_LAYOUT();

Camera camera = CAMERA::CREATE_CAMERA_IN_LAYOUT(layout, "", 0);

CAMERA::INIT_CAMERA_FROM_GAME_CAMERA(camera);
CAMERA::SET_CURRENT_CAMERA_ON_CHANNEL(camera, 0, 0, 0, 0, 0, 0, 0, 0, 0);
```

#### Delete a camera

```cpp
CAMERA::REMOVE_CAMERA_FROM_CHANNEL(camera, 0);
OBJECT::DESTROY_CAMERA(camera);
CAM::CAMERA_RESET(0);
```
