def f1_micro(y_true: list[int], y_pred: list[int]) -> float:
    """
    Returns the micro-averaged F1 score as a Python float rounded to four decimals.
    """
    # Write code here
    TP = sum(y_true == y_pred for y_true, y_pred in zip(y_true,y_pred))
    FN = sum(y_true != y_pred for y_true, y_pred in zip(y_true, y_pred))
    FP = sum(y_true != y_pred for y_true, y_pred in zip(y_true, y_pred))

    return 2*TP/(2*TP + FP + FN)