import pytest
from functions.level_2.two_square_equation import solve_square_equation


@pytest.mark.parametrize('square_coefficient, linear_coefficient,'
                         'const_coefficient, expected',
                         [(5.0, -8.0, 3.0, (0.6, 1.0)),
                          (8.0, 2.0, -1.0, (-0.5, 0.25)),
                          (0.0, 1.0, -4.0, (4.0, None)),
                          (4.0, 4.0, 1.0, (-0.5, -0.5))])
def test__two_square_equation__success(square_coefficient,
                                       linear_coefficient,
                                       const_coefficient,
                                       expected):
    assert solve_square_equation(square_coefficient,
                                 linear_coefficient,
                                 const_coefficient) == expected


@pytest.mark.parametrize('square_coefficient, linear_coefficient,'
                         'const_coefficient, expected',
                         [(1.0, 2.0, 3.0, (None, None))])
def test__two_square_equation__fail(square_coefficient,
                                    linear_coefficient,
                                    const_coefficient,
                                    expected):
    assert solve_square_equation(square_coefficient,
                                 linear_coefficient,
                                 const_coefficient) == expected


# @pytest.mark.parametrize('square_coefficient, linear_coefficient,'
#                          'const_coefficient, expected',
#                          [('abc', -8.0, 3.0, TypeError),
#                           (8.0, 'abc', -1.0, TypeError),
#                           (0.0, 1.0, 'abc', TypeError),
#                           (None, None, None, TypeError)])
# def test__two_square_equation__error(square_coefficient,
#                                      linear_coefficient,
#                                      const_coefficient,
#                                      expected):
#     with pytest.raises(expected):
#         solve_square_equation(square_coefficient,
#                               linear_coefficient,
#                               const_coefficient)
