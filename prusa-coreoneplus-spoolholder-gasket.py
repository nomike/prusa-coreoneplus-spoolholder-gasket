from pythonscad import *

params = Customizer()

params.add_parameter("inner_diameter", 26.5)
params.add_parameter("outer_diameter", 32.6)
params.add_parameter("height", 3.6)
params.add_parameter("epsilon", 0.001)
params.add_parameter("fn", 256)

fn = params["fn"]

gasket = cylinder(d=params["outer_diameter"], h=params["height"]) - cylinder(
    d=params["inner_diameter"], h=params["height"] + 2 * params["epsilon"]
).down(params["epsilon"])

show(gasket)
