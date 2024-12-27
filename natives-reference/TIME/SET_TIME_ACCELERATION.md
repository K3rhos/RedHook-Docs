---
description: Set the time of day cycle scaling. (30.0 is the default value)
---

# SET\_TIME\_ACCELERATION

```cpp
void SET_TIME_ACCELERATION(float _Value);
```

#### Example

```cpp
// Frozen time acceleration
TIME::SET_TIME_ACCELERATION(0.0f);

// Setting the TOD acceleration 10 times faster than normal speed
TIME::SET_TIME_ACCELERATION(300.0f);
```
