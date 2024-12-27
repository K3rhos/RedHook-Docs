---
description: >-
  Allow the gameplay camera FOV to be overridden, bcs the game by default is
  resetting the value every frame.
---

# ALLOW\_GAMEPLAY\_CAMERA\_FOV\_OVERRIDE

{% hint style="info" %}
This function doesn't need to be ran every frame, just set it to **true**, when you need to override the FOV, and restore it to **false** when no longer needed.
{% endhint %}

```cpp
void ALLOW_GAMEPLAY_CAMERA_FOV_OVERRIDE(bool _Toggle);
```

#### Example

<pre class="language-cpp"><code class="lang-cpp">REDHOOK::ALLOW_GAMEPLAY_CAMERA_FOV_OVERRIDE(true);

<strong>Camera gameplayCamera = CAM::GET_GAME_CAMERA();
</strong>
CAMERA::SET_CAMERA_FOV(gameplayCamera, 100.0f); // Set the Gameplay FOV to 100.0
</code></pre>
