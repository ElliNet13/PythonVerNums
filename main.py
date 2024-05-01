class vn:
    def __init__(self, value):
        self._major, self._minor, self._patch = map(int, value.split('.'))
    
    @property
    def major(self):
        return self._major
    
    @major.setter
    def major(self, value):
        self._major = value

    @property
    def minor(self):
        return self._minor
    
    @minor.setter
    def minor(self, value):
        if value > 9:
            self._major += value // 10
            self._minor = value % 10
        else:
            self._minor = value
    
    @property
    def patch(self):
        return self._patch
    
    @patch.setter
    def patch(self, value):
        if value > 9:
            self._minor += value // 10
            self._patch = value % 10
        else:
            self._patch = value
    
    def __str__(self):
        return f"{self._major}.{self._minor}.{self._patch}"
    
    def __repr__(self):
        return f'vn("{self}")'

new = vn("1.0.0")
print(new)
new.patch = 10
print(new)
new.patch = 7744652
print(new)