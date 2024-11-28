---
description: Convert world position to 2D screen position.
---

# WORLD\_TO\_SCREEN

{% hint style="warning" %}
**`_X`** **& `_Y`** are in 0.0 to 1.0 based coordinates.\
That mean 0.0, 0.0 represent the top left corner of your screen, and 1.0, 1.0 the bottom right.
{% endhint %}

```cpp
bool WORLD_TO_SCREEN(Vector3* _WorldPosition, float* _X, float* _Y);
```

```cpp
Actor localPlayerActor = UNSORTED::GET_PLAYER_ACTOR(-1);

Vector3 playerPosition = UNSORTED::GET_POSITION(localPlayerActor);

float x, y;
if (REDHOOK::WORLD_TO_SCREEN(&playerPosition, &x, &y))
{
    Print(Log_Info, "%f %f", x, y); // Output the screen coordinates.
}
```
