from pythonscad import *

inner_diameter = 26.5
outer_diameter = 32.6
height = 3.6
epsilon = 0.001
fn = 256

show(cylinder(d=outer_diameter, h=height) - cylinder(d=inner_diameter, h=height + 2 * epsilon).down(epsilon))