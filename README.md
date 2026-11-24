# Prusa Core One+ spool holder gasket

The [original spool holder](https://www.printables.com/model/1167816-core-onegen-2-printable-parts/) (see file "spoolholder-static-r1.stl") requires a rubber gasket.

This is a printable version of it.

You can find STLs for this design on Thingiverse (see link below).

## Customizing

This design was done in PythonSCAD and can be customized.

Clone the repository with `git clone` using the Github URL mentioned below.

Create a Python virtual environmennt:

Unix:

```shell
$ python3 -m venv .venv
$ source .venv/bin/activate
(.venv) $ pip install --upgrade pip
(.venv) $ pip install -r requirements.txt
```

PowerShell:

```powershell
PS> python -m venv .venv
PS> .venv\Scripts\Activate.ps1
(.venv) PS> pip install --upgrade pip
(.venv) PS> pip install -r requirements.txt
```

Then simply run `make` or generate the STL with this command:

Unix:

```shell
(.venv) $ generate-pythonscad-stls --output-dir="output"
```

PowerShell:

```powershell
(.venv) PS> generate-pythonscad-stls --output-dir="output"
```

## Thingiverse

<https://thingiverse.com/thing:6528263>

## GitHub

<https://github.com/nomike/prusa-coreoneplus-spoolholder-gasket/>
