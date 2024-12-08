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

    if unit == procurmentUnit:
        AUS2 = 1
    else:
        AUS2 = 0

    if unit == salesPriceUnit:
        AUS5 = 1
        AUS9 = 1
        if factor != 1:
            conversionForm = 2
    else:
        AUS5 = 0
        AUS9 = 0

    for type in unitTypes:
        type = type.value
        if type == 1:
            print(
                f"Type:{type} Factor:{factor} Unit:{unit} Aus1:{AUS1} Aus2:{AUS2} Conversion_Form:{conversionForm}"
            )
        else:
            print(
                f"Type:{type} Factor:{factor} Unit:{unit} Aus5:{AUS5} Aus9:{AUS9} Conversion_Form:{conversionForm}\n"
            )


factor: float = 1
unit: str = "PAK"
basicUnit: str = "PAK"
salesPriceUnit: str = "STK"
procurmentUnit = "PAK"


makeUnit(
    factor=factor,
    unit=unit,
    basicUnit=basicUnit,
    salesPriceUnit=salesPriceUnit,
    procurmentUnit=procurmentUnit,
)
makeUnit(
    factor=0.1,
    unit="STK",
    basicUnit=basicUnit,
    salesPriceUnit=salesPriceUnit,
    procurmentUnit=procurmentUnit,
)
makeUnit(
    factor=10,
    unit="PAL",
    basicUnit=basicUnit,
    salesPriceUnit=salesPriceUnit,
    procurmentUnit=procurmentUnit,
)
makeUnit(
    factor=1,
    unit="ESK",
    basicUnit=basicUnit,
    salesPriceUnit=salesPriceUnit,
    procurmentUnit=procurmentUnit,
)
