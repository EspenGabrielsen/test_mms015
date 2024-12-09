from enum import Enum

unitTypes = Enum("UnitTypes", [("quantity", 1), ("price", 2)])


def makeUnit(factor, unit, basicUnit, salesPriceUnit, procurmentUnit):

    conversionForm = 1

    if unit == basicUnit:
        if factor != 1:
            raise ValueError("ERROR IN FACTOR NEEDS TO BE 1")
        AUS1 = 1
    else:
        AUS1 = 0

    if unit == procurmentUnit: # legger inn enhets flagg
        AUS2 = 1
    else:
        AUS2 = 0

    if unit == salesPriceUnit: # legger inn pris flagg
        AUS5 = 1
        AUS9 = 1
        if factor != 1:
            factor = round(1/factor,3) # endrer faktor slik at salgsenhet kan deles (round slik at det ikke bli float feil)
            conversionForm = 2 # settere converterings type flagg
    else:
        AUS5 = 0
        AUS9 = 0
    
    for type in unitTypes:
        type = type.value
        if type == 1:
            print(
                f"Type:{type}\nFactor: {factor:5} Unit:{unit:3} Aus1:{AUS1} Aus2:{AUS2} Conversion_Form:{conversionForm}"
            )
        else:
            print(
                f"Type:{type}\nFactor: {factor:5} Unit:{unit:3} Aus5:{AUS5} Aus9:{AUS9} Conversion_Form:{conversionForm}\n"
            )


basicUnit: str = "PAK"
salesPriceUnit: str = "LM"
procurmentUnit = "PAK"

makeUnit(
    factor=1,
    unit="PAK",
    basicUnit=basicUnit,
    salesPriceUnit=salesPriceUnit,
    procurmentUnit=procurmentUnit,
)

makeUnit(
    factor=0.277777778,
    unit="LM",
    basicUnit=basicUnit,
    salesPriceUnit=salesPriceUnit,
    procurmentUnit=procurmentUnit,
)

makeUnit(
    factor=165,
    unit="PAL",
    basicUnit=basicUnit,
    salesPriceUnit=salesPriceUnit,
    procurmentUnit=procurmentUnit,
)
