import json
from functools import reduce
from decimal import *
import xml.etree.cElementTree as ET

type = input()
# abc = '{"K":10,"Sums":[1.01,2.02],"Muls":[1,4]}'
if type == "Json":
    json_input = input()
    json_obj = json.loads(json_input)
    sums = list(map(lambda x: Decimal(str(x)), json_obj["Sums"]))
    muls = json_obj["Muls"]
    K = Decimal(str(json_obj["K"]))
    values = []
    values.extend(muls)
    values.extend(sums)
    sum_result = sum(sums) * K
    mul_result = reduce(lambda x, y: x * y, muls)
    sorted_vals = sorted(list(map(lambda x: float(x), values)))
    data = {}
    data['SumResult'] = float(sum_result)
    data['MulResult'] = float(mul_result)
    data['SortedInputs'] = sorted_vals
    json_data = json.dumps(data)
    print(type)
    print(json_data)
else:
    #i = "<Input><K>10</K><Sums><decimal>1.01</decimal><decimal>2.02</decimal></Sums><Muls><int>1</int><int>4</int></Muls></Input>"
    xml_obj = input()
    root = ET.fromstring(xml_obj)
    sums = []
    muls = []
    values = []
    K = Decimal(root.find("K").text)
    for dec in root.find("Sums"):
        sums.append(Decimal(dec.text))
    for int in root.find("Muls"):
        muls.append(Decimal(int.text))
    values.extend(muls)
    values.extend(sums)
    sum_result = sum(sums) * K
    mul_result = reduce(lambda x, y: x * y, muls)
    sorted_vals = sorted(list(map(lambda x: float(x), values)))
    output_xml = ET.Element('Output')
    SumResult = ET.Element('SumResult')
    SumResult.text = str(sum_result)
    output_xml.append(SumResult)
    MulResult = ET.Element('MulResult')
    MulResult.text = str(mul_result)
    output_xml.append(MulResult)
    SortedInputs = ET.Element('SortedInputs')
    for val in sorted_vals:
        el = ET.Element('decimal')
        el.text = str(val)
        SortedInputs.append(el)
    output_xml.append(SortedInputs)
    print(type)
    print(ET.tostring(output_xml, encoding='unicode'))