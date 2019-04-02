import math
import cmath
from bokeh.plotting import figure
from bokeh.embed import components

def get_complex_roots(cmplx_num, root_degree):
    ''' returns the list of roots of a complex number
        Example:
        roots = get_complex_roots(-2j, 2)
        [(1.0000000000000002-1j), (-1+1.0000000000000002j)]
    '''
    roots_list = []
    modulus = math.sqrt(cmplx_num.real ** 2 + cmplx_num.imag ** 2)
    modulus_root = modulus ** (1/root_degree)
    phase = cmath.phase(cmplx_num)
    for i in range(root_degree):
        root = cmath.rect(modulus_root, (phase + 2 * i * math.pi)/root_degree)
        roots_list.append(root)
    return roots_list

def get_plot_components():
    plot = figure()
    plot.circle([1,2], [3,4])
    comp = components(plot)
    return comp