---
description: Get all actors spawned in the world.
---

# WORLD\_GET\_ALL\_ACTORS

{% hint style="info" %}
Max world actors at once cannot exceed **70**.
{% endhint %}

```cpp
int WORLD_GET_ALL_ACTORS(Actor* _Array);
```

#### Example

```cpp
// A cool wrapper !
static const std::vector<Actor> GetWorldAllActors()
{
	std::vector<Actor> result = {};

	Actor actors[70];
	int actorsCount = REDHOOK::WORLD_GET_ALL_ACTORS(actors);

	for (int i = 0; i < actorsCount; i++)
	{
		Actor actor = actors[i];

		if (!ENTITY::IS_ACTOR_VALID(actor))
			continue;

		result.push_back(actor);
	}

	return result;
}
```
