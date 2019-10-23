from django.test import TestCase
from .utils import get_complex_roots


class ComplexTestCase(TestCase):
    def setUp(self):
        self.cmplx1 = complex(1, 0)
        self.cmplx2 = complex(1, 1)
        self.cmplx3 = complex(2, 2)
        self.cmplx4 = complex(0, 0)

    def test_complex_roots_results(self):
        c1 = get_complex_roots(self.cmplx1, 2)
        c1_expected = [(1+0j), (-1+0j)]

        c2 = get_complex_roots(self.cmplx2, 2)
        c2_expected = [(1.1+0.46j), (-1.1-0.46j)]

        c3 = get_complex_roots(self.cmplx3, 3)
        c3_expected = [(1.37+0.37j), (-1+1j), (-0.37-1.37j)]

        self.assertEqual(c1, c1_expected)
        self.assertEqual(c2, c2_expected)
        self.assertEqual(c3, c3_expected)


