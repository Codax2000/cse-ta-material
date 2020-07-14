'''
Alex Knowlton
Infrastructure, CSE 163 Summer 2020
7/10/2020

This module contains a SuitJacket class that tracks information about
a men's suit jacket.
'''


class SuitJacket:
    '''
    This class contains the number of buttons of a men's jacket, the
    number of vents, and the type of the jacket as a String.
    It has functions for getting the type of the jacket and the
    overall style score, which is the number of buttons added to the number
    of vents.
    '''
    def __init__(self, type, num_vents, num_buttons=3):
        '''
        Takes in the type of the jacket as a String, the number of vents
        of this jacket as an int, and the number of buttons as an int.
        If no value is specified for the number of buttons, defaults to 3.
        '''
        self._type = type
        self._num_vents = num_vents
        self._num_buttons = num_buttons

    def get_style_score(self):
        '''
        returns the style score of this jacket, which is the sum of the
        number of buttons and the number of vents, as an int.
        '''
        return self._num_buttons + self._num_vents

    def get_type(self):
        '''
        returns the type of this jacket as a String
        '''
        return self._type
