"""Semplici operazioni aritmetiche tra due numeri."""


def calculate(first_number: float, second_number: float, operation: str) -> float:
    """Esegue un'operazione aritmetica tra due numeri.

    Le operazioni accettate sono ``+``, ``-``, ``*`` e ``/``.
    Solleva ``ZeroDivisionError`` se il divisore è zero.
    """
    if operation == "+":
        return first_number + second_number
    if operation == "-":
        return first_number - second_number
    if operation == "*":
        return first_number * second_number
    if operation == "/":
        # Controlliamo il divisore prima di eseguire l'operazione, così chi usa
        # la funzione riceve un messaggio comprensibile.
        if second_number == 0:
            raise ZeroDivisionError("Non è possibile dividere per zero.")
        return first_number / second_number

    raise ValueError(f"Operazione non supportata: {operation}")
