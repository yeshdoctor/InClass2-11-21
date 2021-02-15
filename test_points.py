import pytest
@pytest.mark.parametrize("p1,p2,x_new,y",[((1,1),(2,2),3,3),((1,-1),(2,-2),3,-3),((5,7),(6,14),4,0),((12,6),(7,3.5),22,11)])

def test_plane(p1,p2,x_new,y):
    from points import plane
    assert y == plane(p1,p2,x_new)

@pytest.mark.parametrize("point1,point2,point3,online",[((1,2),(3,4),(22,-12),False),((1,1),(2,2),(3,3),True),((2,2),(4,192),(-11,-67),False),((5,21),(10,42),(15,63),True)])

def test_on_line(point1,point2,point3,online):
    from points import on_line
    assert online == on_line(point1,point2,point3)
