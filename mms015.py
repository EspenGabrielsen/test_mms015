from enum import Enum

unitTypes = Enum("UnitTypes", [("quantity", 1), ("price", 2)])


def makeUnit(factor, unit, basicUnit, salesPriceUnit, procurmentUnit):

    conversionForm = 1  # 1 = multiplied
    AUS1 = 0
    AUS2 = 0
    AUS5 = 0
    AUS9 = 0
    if (
        unit == basicUnit
    ):  # adding the flag this is the basic unit, and checking that it is 1. Else ValueError is raised
        if factor != 1:
            raise ValueError("ERROR IN BASICUNIT FACTOR NEEDS TO BE 1")
        AUS1 = 1

    if unit == procurmentUnit:  # add the flag this is the procurment unit
        AUS2 = 1

    if unit == salesPriceUnit:  # adding the flag this is the salesprice unit
        AUS5 = 1
        AUS9 = 1
        if factor != 1:
            factor = round(
                1 / factor, 5
            )  # converting factor for the salesprice unit so it can be devided instead of multiplied
            conversionForm = 2  # swaping conversion form to 2 = divide

    for type in unitTypes:  # Printing each type as they would be sent to the API
        type = type.value
        if type == 1:
            print(
                f"Type:{type}\nFactor: {factor:5} Unit:{unit:3} Aus1:{AUS1} Aus2:{AUS2} Conversion_Form:{conversionForm}"
            )
        else:
            print(
                f"Type:{type}\nFactor: {factor:5} Unit:{unit:3} Aus5:{AUS5} Aus9:{AUS9} Conversion_Form:{conversionForm}\n"
            )


basicUnit: str = "STK"
salesPriceUnit: str = "STK"
procurmentUnit = "STK"

makeUnit(
    factor=1,
    unit="STK",
    basicUnit=basicUnit,
    salesPriceUnit=salesPriceUnit,
    procurmentUnit=procurmentUnit,
)

makeUnit(
    factor=4,
    unit="KRT",
    basicUnit=basicUnit,
    salesPriceUnit=salesPriceUnit,
    procurmentUnit=procurmentUnit,
)

makeUnit(
    factor=12,
    unit="PAL",
    basicUnit=basicUnit,
    salesPriceUnit=salesPriceUnit,
    procurmentUnit=procurmentUnit,
)
