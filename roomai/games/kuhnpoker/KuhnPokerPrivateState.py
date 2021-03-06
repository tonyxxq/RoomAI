#!/bin/python
import roomai.games.common

class KuhnPokerPrivateState(roomai.games.common.AbstractPrivateState):
    '''
    The private state class of KuhnPoker
    '''

    def __deepcopy__(self, memodict={}, newinstance = None):
        return AKuhnPokerPrivateState
AKuhnPokerPrivateState = KuhnPokerPrivateState()