Simulations #1
hl = 4500
hr = 480
x = (-150e3,0,150e3)
tf = 1600
pwlinear
Details:
* There is a right bank wave that causes the growing peak to stop growing and decay after the peak to the Riemann value
* Shape of the growing peak wavefront (before it reaches the right side) can be approximated by our special function but not exactly.

Simulations #2
hl = 4500
hr = 480
x = (-150e3,0,150e3)
tf = 1600
pwcubic
Details:
* Looks like it touches the peak value closer than the pwlinear case.
* lag between peak and Riemann value is smoothened out (a lot) by the right bank wave

Simulations #3
hl = 4500
hr = 480
x = (-50e3,0,100e3,300e3)
tf = 1600
pwlinear
Details:
* the curve between peak value and the reimann solution is not monotonic, the value in between goes below the riemann value but just barely.
* time lag of approx 5 purples

Simulations #4
hl = 4500
hr = 480
x = (-50e3,0,50e3,300e3)
tf = 1600
pwlinear
Details:
* again monotonic, with a tiny dip before riemann value
* time lag of approx 2.5 purples possibly implying that the time lag theory is right.