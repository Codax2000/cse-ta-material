'''
Alex Knowlton
Infrastructure, CSE 163 Summer 2020
7/10/2020

This module contains a Closet class that holds SuitJackets and can be
queried for information on the best jackets to wear.
'''


class Closet:
    '''
    This class defines a Closet class that holds SuitJackets. It has methods
    to return jackets that are of a particular type or jackets in order
    of overall style.
    '''

    def __init__(self, jackets):
        '''
        takes in a List of SuitJackets to track in this closet.
        '''
        self._jackets = dict()
        for jacket in jackets:
            type = jacket.get_type()
            if type not in self._jackets:
                self._jackets[type] = list()
            self._jackets[type].append(jacket)

    def get_jackets_of_type(self, type):
        '''
        returns a List of all SuitJackets that have the same type as the
        given type, in the same order that they were added to this Closet.
        If there are no SuitJackets of the given type, returns an empty List
        '''
        return self._jackets[type] if type in self._jackets else list()

    def add_jacket(self, jacket):
        '''
        adds the given SuitJacket to the Closet, so it will now appear
        when the Closet is queried
        '''
        type = jacket.get_type()
        if type in self._jackets:
            self._jackets[type].append(jacket)
        else:
            self._jackets[type] = [jacket]

    def get_jackets_by_style(self):
        '''
        returns a List of all SuitJackets in this Closet, ordered by their
        overall style, which is the sum of their buttons and vents, divided
        by the number of jackets of their type. The jacket with the
        highest ranked style is at the 'front' of the list, or at index 0.
        If there are no SuitJackets in this Closet, returns an empty List
        '''
        if len(self._jackets) == 0:
            return list()
        jackets = []
        for jacket in self._jackets.values():
            jackets += jacket  # this works because you can add lists together
        sorted_jackets = sorted(jackets, key=lambda s: s.get_style_score() /
                                len(self._jackets[s.get_type()]),
                                reverse=True)
        return sorted_jackets
