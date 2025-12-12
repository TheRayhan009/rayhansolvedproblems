the_numbers_of_polyhedrons=int(input())
ans=0
for i in range(the_numbers_of_polyhedrons):
    check_polyhedrons=input()
    if check_polyhedrons=="Tetrahedron":
        ans = ans + 4
    elif check_polyhedrons=="Cube":
        ans = ans + 6
    elif check_polyhedrons=="Octahedron":
        ans = ans + 8
    elif check_polyhedrons=="Dodecahedron":
        ans = ans + 12
    else:
        ans = ans + 20
print(ans)