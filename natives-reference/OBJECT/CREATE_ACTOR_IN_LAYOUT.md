---
description: >-
  Create an actor (npc, animal, vehicle, horse, ...) with a model, position &
  rotation.
---

# CREATE\_ACTOR\_IN\_LAYOUT

```cpp
Actor CREATE_ACTOR_IN_LAYOUT(Layout _Layout, const char* _ActorName, ActorModel _Model, Vector2 _PositionXY, float _PositionZ, Vector2 _RotationXY, float _RotationZ);
```

How to spawn an actor:

```cpp
void SpawnActor(ActorModel _Model, Vector3 _Position, Vector3 _Rotation)
{
    // Request the model.
    STREAM::STREAMING_REQUEST_ACTOR(_Model, true, false);

    // Wait for the model to be loaded in memory...
    while (!STREAM::STREAMING_IS_ACTOR_LOADED(_Model, -1))
    {
        ScriptWait(0);
    }

    // Get the player layout.
    Layout layout = OBJECT::FIND_NAMED_LAYOUT("PlayerLayout");

    // Create the actor with a specific model at specific position and rotation.
    Actor actor = OBJECT::CREATE_ACTOR_IN_LAYOUT(layout, "", _Model, PACK_VECTOR3(_Position), PACK_VECTOR3(_Rotation));

    // Make sure the newly created actor is valid
    if (ENTITY::IS_ACTOR_VALID(actor))
    {
        // Do something on the actor... (Godmode, give weapons to him or stuff like that etc...)

        // Make the actor as no longer needed, it will be deleted if you go away or actors pool is full.
        OBJECT::RELEASE_ACTOR(actor);
    }
}
```
