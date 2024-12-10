from enum import Enum

unitTypes = Enum("UnitTypes", [("quantity", 1), ("price", 2)])
pricecomparisonType = Enum("PriceComparison",[("pricecomparison",7)])

def makeUnit(factor, unit, basicUnit, salesPriceUnit, procurmentUnit, packageType="",altFactor=1):

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
    
    if packageType == "PSE-PAK":
        type = pricecomparisonType.pricecomparison.value
        factor = altFactor
        conversionForm = 1
        print(
                f"Type:{type}\nFactor: {factor:5} Unit:{unit:3} Conversion_Form: {conversionForm}\n"
            )
    else:
        for type in unitTypes:  # Printing each type as they would be sent to the API
            type = type.value
            if type == 1:
                print(
                    f"Type:{type}\nFactor: {factor:5} Unit:{unit:3} AUS1:{AUS1} AUS2:{AUS2} Conversion_Form: {conversionForm}"
                )
            else:
                print(
                    f"Type:{type}\nFactor: {factor:5} Unit:{unit:3} AUS5:{AUS5} AUS9:{AUS9} Conversion_Form: {conversionForm}\n"
                )



#____ALT UNDER HER ER TEST DATA_____
basicUnit: str = "STK"
salesPriceUnit: str = "M2"
procurmentUnit = "STK"

makeUnit(
    factor=1,
    unit="STK",
    basicUnit=basicUnit,
    salesPriceUnit=salesPriceUnit,
    procurmentUnit=procurmentUnit,
    packageType="F-PAK",
    altFactor=3.57
)
makeUnit(
    factor=0.280112045,
    unit="M2",
    basicUnit=basicUnit,
    salesPriceUnit=salesPriceUnit,
    procurmentUnit=procurmentUnit,
    packageType="",
    altFactor=1
)

makeUnit(
    factor=12,
    unit="PAL",
    basicUnit=basicUnit,
    salesPriceUnit=salesPriceUnit,
    procurmentUnit=procurmentUnit,
    packageType="D-PAK",
    altFactor=42.84
)
makeUnit(
    factor=0.280112045,
    unit="M2",
    basicUnit=basicUnit,
    salesPriceUnit=salesPriceUnit,
    procurmentUnit=procurmentUnit,
    packageType="PSE-PAK",
    altFactor=1
)