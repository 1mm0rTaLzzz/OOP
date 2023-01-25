import math


class Vector3D:
    __slots__ = ['x', 'y', 'z']

    def __init__(self, ix=0, iy=0, iz=0):
        self.x = ix
        self.y = iy
        self.z = iz

    def as_tuple(self): 
        return self.x, self.y, self.z

    def __iter__(self): 
        return iter(self.as_tuple())

    def __mul__(self, other): 
        return __class__(self.x * other, self.y * other, self.z * other)

    def __abs__(self): 
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def __add__(self, other): 
        return __class__(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other): 
        return __class__(self.x - other.x, self.y - other.y, self.z - other.z)

    def __truediv__(self, other): 
        return __class__(self.x / float(other), self.y / float(other), self.z / float(other))

    def vector_mul(self, other): 
        return __class__(self.y * other.z - self.z * other.y, self.z * other.x - self.x * other.z, self.x * other.y - self.y * other.x)

    def ABC(self, other): 
        return self.x * other.x + self.y * other.y + self.z * other.z


a, b = map(int, input().split())
v0 = Vector3D(0, 0, 0)
x, y, z = map(float, input().split())
v1 = Vector3D(x, y, z)
x, y, z = map(float, input().split())
v2 = Vector3D(x, y, z)

v = v0 - v1
w = v2 - v1
p = v1 + w * (Vector3D.ABC(v, w) / (abs(w) ** 2))
r = p - v0
d = abs((v0 - p))

try:
    s = math.acos((d * d - a * a - b * b) / (-2 * a * b))
except:
    s = 0

if d > a + b or s < math.pi / 2 - 1e-9:
    print("No solution.")
else:
    t = math.acos((b * b - a * a - d * d) / (-2 * a * d))
    q = Vector3D.vector_mul(w, r) / abs(Vector3D.vector_mul(w, r))
    W = r / abs(r) * a * math.cos(t) + q * a * math.sin(t)
    x, y, z = map(float, W)
    print(x, y, z, s)
