def royxatda_uchrashuvlar(sonlar):
    royxat = {}
    for son in sonlar:
        if son in royxat:
            royxat[son] += 1
        else:
            royxat[son] = 1
    return royxat

def uchrashuvlar_soni(sonlar):
    royxat = royxatda_uchrashuvlar(sonlar)
    return {son: uchrashuv for son, uchrashuv in royxat.items() if uchrashuv > 1}

sonlar = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(uchrashuvlar_soni(sonlar))
```

```python
def royxatda_uchrashuvlar(sonlar):
    royxat = {}
    for son in sonlar:
        if son in royxat:
            royxat[son] += 1
        else:
            royxat[son] = 1
    return royxat

def uchrashuvlar_soni(sonlar):
    royxat = royxatda_uchrashuvlar(sonlar)
    return {son: uchrashuv for son, uchrashuv in royxat.items() if uchrashuv > 1}

sonlar = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(uchrashuvlar_soni(sonlar))
```

```python
def royxatda_uchrashuvlar(sonlar):
    royxat = {}
    for son in sonlar:
        if son in royxat:
            royxat[son] += 1
        else:
            royxat[son] = 1
    return royxat

def uchrashuvlar_soni(sonlar):
    royxat = royxatda_uchrashuvlar(sonlar)
    return {son: uchrashuv for son, uchrashuv in royxat.items() if uchrashuv > 1}

sonlar = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(uchrashuvlar_soni(sonlar))
