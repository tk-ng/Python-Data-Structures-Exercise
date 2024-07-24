def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    result = ""
    for ltr in phrase:
        if ltr.lower() == to_swap.lower():
            # ltr = ltr.upper() if ltr.islower() else ltr.lower()
            ltr = ltr.swapcase()

        result+=ltr

    return result
