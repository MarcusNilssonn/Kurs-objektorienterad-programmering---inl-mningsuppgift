""" Skapa en egen exception class som heter:
EgenException
Klassen ska ärva utav 
Exception  """

class EgenException(Exception):
    pass

""" Skapa en funktion som heter:
Kasta
Metoden ska kasta/raise EgenException
"""
def Kasta():
    raise EgenException