import re

class ParolValidatsiya:
    def __init__(self, uzunlik, belgilar):
        self.uzunlik = uzunlik
        self.belgilar = belgilar

    def validatsiya(self, parol):
        if len(parol) < self.uzunlik:
            return False
        if not re.search(r"[a-z]", parol):
            return False
        if not re.search(r"[A-Z]", parol):
            return False
        if not re.search(r"[0-9]", parol):
            return False
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", parol):
            return False
        return True

uzunlik = 8
belgilar = ["katta harf", "kichik harf", "son", "maxsus belgi"]

parol_validatsiya = ParolValidatsiya(uzunlik, belgilar)

parollar = ["Parol123!", "PAROL123", "parol123", "parol123!"]

for parol in parollar:
    if parol_validatsiya.validatsiya(parol):
        print(f"Parol {parol} validatsiya qilingan")
    else:
        print(f"Parol {parol} validatsiya qilinmadi")
```

```python
import re

class ParolValidatsiya:
    def __init__(self, uzunlik, belgilar):
        self.uzunlik = uzunlik
        self.belgilar = belgilar

    def validatsiya(self, parol):
        if len(parol) < self.uzunlik:
            return False
        if not re.search(r"[a-z]", parol):
            return False
        if not re.search(r"[A-Z]", parol):
            return False
        if not re.search(r"[0-9]", parol):
            return False
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", parol):
            return False
        return True

uzunlik = 8
belgilar = ["katta harf", "kichik harf", "son", "maxsus belgi"]

parol_validatsiya = ParolValidatsiya(uzunlik, belgilar)

parollar = ["Parol123!", "PAROL123", "parol123", "parol123!"]

for parol in parollar:
    if parol_validatsiya.validatsiya(parol):
        print(f"Parol {parol} validatsiya qilingan")
    else:
        print(f"Parol {parol} validatsiya qilinmadi")
