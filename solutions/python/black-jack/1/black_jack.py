"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):

    
    """Determine the scoring value of a card.
    

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    if card == 'J' or  card == 'Q' or card == 'K':
        value = 10
    elif card == 'A':
        value = 1
    else:
        value = int(card);

    return value;

    
    

    

    

def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    if card_one == 'J' or  card_one == 'Q' or card_one == 'K':
        value1 = 10
    elif card_one == 'A':
        value1 = 1
    else:
        value1 = int(card_one);

    if card_two == 'J' or  card_two == 'Q' or card_two == 'K':
        value2 = 10
    elif card_two == 'A':
        value2 = 1
    else:
        value2 = int(card_two);

    value1 = int(value1)
    value2 = int(value2)

    if value1 > value2:
        return card_one
    elif value2 > value1:
        return card_two
    elif value1 == value2:
        return (card_one,card_two)

    


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for an upcoming ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    
    if card_one == 'J' or  card_one == 'Q' or card_one == 'K' or card_one == 'A':
        return 1
    elif card_two == 'J' or  card_two == 'Q' or card_two == 'K' or card_two == 'A':
        return 1
    else:
        sum = int(card_one) + int(card_two)
        if sum + 11 <= 21 :
            return 11;
        else:
            return 1;
            
            
        
    


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    if card_one == 'A':
        if card_two == 'J' or  card_two == 'Q' or card_two == 'K' or card_two == '10':
            return True;
        else:
            return False;
    elif card_two == 'A':
        if card_one == 'J' or  card_one == 'Q' or card_one == 'K' or card_one == '10':
            return True;
        else:
            return False;
    else:
        return False


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """
    if card_one == '6' and card_two == '6':
        return True;
    elif card_one == card_two:
        return True;
    elif card_one == 'K' and card_two == 'Q':
        return True;
    elif card_one == 'Q' and card_two == 'K':
        return True
    else:
        return False
    


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """
    if card_one == 'J' or  card_one == 'Q' or card_one == 'K':
        value1 = 10
    elif card_one == 'A':
        value1 = 1
    else:
        value1 = int(card_one);

    if card_two == 'J' or  card_two == 'Q' or card_two == 'K':
        value2 = 10
    elif card_two == 'A':
        value2 = 1
    else:
        value2 = int(card_two);

    sum = int(value1) + int(value2);
    if sum == 9 or sum==10 or sum==11:
        return True;
    else:
        return False
