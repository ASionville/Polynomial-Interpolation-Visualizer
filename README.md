# Polynomial-Interpolation-Visualizer
A very quick visualisation of Lagrange interpolating polynomial

## What are Lagrange Interpolating Polynomials ?
The Lagrange Interpolating Polynomial (LIP) is (by Wikipedia) "the unique polynomial of lowest degree that interpolates a given set of data"\
For us, it will be the unique polynomial that goes throught a list of given points

## How does it work ?
Those are the Keybindings of the Canvas :\
 - `Left Click`: Add a point\
 - `Left Click + Drag`: Move a point\
 - `Right Click`: Delete a point\

Each time the Canvas is modified, the LIP the recalculated to fit the new positions of the points
It is calculated using the formula :\
$\displaystyle LIP(X) = \sum_{j=0}^n y_j\bigg(\prod_{i=0,i\neq j}^n \frac{X-x_i}{X_j-X_i}\bigg)$
