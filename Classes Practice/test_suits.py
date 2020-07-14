'''
Alex Knowlton
Infrastructure, CSE 163 Summer 2020
7/10/2020

This module tests the SuitJacket and Closet classes for correctness.
'''

from suit_jacket import SuitJacket
from closet import Closet


def test_suit_jacket():
    '''
    tests the SuitJacket class
    '''
    test_get_style_score()
    test_get_type()


def test_get_style_score():
    '''
    tests the get_style_score of the SuitJacket class
    '''
    jacket_one = SuitJacket('Blazer', 1)
    jacket_two = SuitJacket('Blazer', 2, 2)
    jacket_three = SuitJacket('Tuxedo', 0, 0)
    assert jacket_one.get_style_score() == 4
    assert jacket_two.get_style_score() == 4
    assert jacket_three.get_style_score() == 0


def test_get_type():
    jacket_one = SuitJacket('Blazer', 1)
    jacket_two = SuitJacket('Tuxedo', 2, 2)
    assert jacket_one.get_type() == 'Blazer'
    assert jacket_two.get_type() == 'Tuxedo'


def test_closet():
    '''
    tests the Closet class
    '''
    closet_one = Closet([SuitJacket('Tweed', 1, 2),
                         SuitJacket('Tuxedo', 0),
                         SuitJacket('Tuxedo', 2, 2)])
    closet_two = Closet([SuitJacket('Blazer', 1),
                         SuitJacket('Pinstriped', 0, 3)])
    closet_three = Closet([])
    closets = [closet_one, closet_two, closet_three]
    test_get_jackets_of_type(closets)
    test_add_jacket()
    test_get_jackets_by_style(closets)


def test_get_jackets_of_type(closets):
    '''
    tests the get_jackets_of_type function of the Closet class
    '''
    assert len(closets[0].get_jackets_of_type('Tweed')) == 1
    assert len(closets[2].get_jackets_of_type('Blazer')) == 0
    assert len(closets[1].get_jackets_of_type('Sporting')) == 0


def test_add_jacket():
    '''
    tests the add_jacket function of the Closet class
    '''
    closet = Closet([SuitJacket('Blazer', 1),
                     SuitJacket('Pinstriped', 0, 3)])
    closet.add_jacket(SuitJacket('Sporting', 0, 2))
    assert len(closet.get_jackets_of_type('Sporting')) == 1
    assert closet.get_jackets_of_type('Sporting')[0].get_style_score() == 2


def test_get_jackets_by_style(closets):
    '''
    tests the get_jackets_by_style function of the Closet class
    '''
    assert [i.get_type() for i in closets[0].get_jackets_by_style()] == \
        ['Tweed', 'Tuxedo', 'Tuxedo']
    assert [i.get_type() for i in closets[1].get_jackets_by_style()] == \
        ['Blazer', 'Pinstriped']
    assert [i.get_type() for i in closets[2].get_jackets_by_style()] == []


def main():
    test_suit_jacket()
    test_closet()


if __name__ == '__main__':
    main()
