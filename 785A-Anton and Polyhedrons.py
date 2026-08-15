import sys

faces = {
    'Tetrahedron': 4,
    'Cube': 6,
    'Octahedron': 8,
    'Dodecahedron': 12,
    'Icosahedron': 20
}

n = int(sys.stdin.readline())
total = sum(faces[sys.stdin.readline().strip()] for _ in range(n))
print(total)