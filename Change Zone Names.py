
from archicad import ACConnection
import archicad
import sys
conn = ACConnection.connect()

assert conn

acc = conn.commands
act = conn.types
acu = conn.utilities

elements = acc.GetElementsByType('Zone')
zoneNameId = acu.GetBuiltInPropertyId('Zone_ZoneName')
appliId = acu.GetUserDefinedPropertyId('Phases','Application')
value =acc.GetPropertyValuesOfElements(elements,[appliId])
EPVArray = []
for index,element in enumerate(elements):
    element = element.elementId
    buffer = str(value[index].propertyValues[0].propertyValue.value.displayValue)
    buffer = buffer.split(':')[0]
    normalString = act.NormalStringPropertyValue(buffer,type='string',status = 'normal')
    EPV =act.ElementPropertyValue(element,zoneNameId, normalString)
    EPVArray.append(EPV)
    result = acc.SetPropertyValuesOfElements(EPVArray)
   
