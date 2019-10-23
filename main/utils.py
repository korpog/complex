import math
import cmath
from bokeh.plotting import figure
from bokeh.embed import components


def get_complex_roots(cmplx_num, root_degree):
    ''' returns the list of roots of a complex number (rounded to two decimal places)
        Example:
        cmplx_num = complex(1, 0)
        roots = get_complex_roots(cmplx_num, 2)
        [(1+0j), (-1+0j)]
    '''
    roots_list = []
    modulus = math.sqrt(cmplx_num.real ** 2 + cmplx_num.imag ** 2)
    modulus_root = modulus ** (1/root_degree)
    phase = cmath.phase(cmplx_num)
    for i in range(root_degree):
        root = cmath.rect(modulus_root, (phase + 2 * i * math.pi)/root_degree)
        root_rounded = complex(round(root.real, 2), round(root.imag, 2))
        roots_list.append(root_rounded)
    return roots_list


def get_plot_components(x_vals, y_vals):
    plot = figure(title="Complex roots", x_axis_label='Real', y_axis_label='Imaginary',
                  plot_width=400, plot_height=400, toolbar_location="below")
    plot.circle(x=x_vals, y=y_vals, size=5, color="navy")
    comp = components(plot)
    return comp
