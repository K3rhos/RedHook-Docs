---
description: Return the height of a text by passing font id and font scale.
---

# RH\_GetTextHeight

{% hint style="warning" %}
Output value is in 0.0 to 1.0 based coordinates.\
That mean 0.0 represent no size and 1.0 is taking the whole screen height.
{% endhint %}

{% hint style="danger" %}
**\_Text** is what we call an "unsafe" variable bcs <mark style="color:yellow;">**DrawText**</mark> get called from a different thread, that mean if you pass a <mark style="color:blue;">**std::string**</mark> using <mark style="color:yellow;">**.c\_str()**</mark> the temporary value will not be retained.\
I suggest doing a wrapper using <mark style="color:yellow;">**strdup**</mark> so you get a safe copy of your ptr (See example below)
{% endhint %}

{% hint style="danger" %}
**\_OutputValue** result is slightly delayed, bcs the function need to do a "flip flop" to run in the rendering thread, get the value and give you back the value.

If you don't want to deal with that I suggest making a global/static variable somewhere storing the previous size and update it accordingly when needed.
{% endhint %}

```cpp
void RH_GetTextHeight(const char* _Text, int _FontId, float _FontScale, float* _OutputValue);
```

```cpp
// Safe wrapper so we don't lose the temporary conversion using .c_str()
void GetTextHeight(const std::string& _Text, int _FontId, float _FontScale, float* _OutputValue)
{
	const char* safeCStr = _strdup(_Text.c_str());

	return RH_GetTextHeight(safeCStr, _FontId, _FontScale, _OutputValue);
}
```
