---
description: Set the current time of the day.
---

# SET\_TIME\_OF\_DAY

```cpp
void SET_TIME_OF_DAY(Time _UnixTime);
```

#### Example

```cpp
// Set the time to 12:00 AM
Time time = TIME::MAKE_TIME_OF_DAY(12, 0, 0);

TIME::SET_TIME_OF_DAY(time);
```
