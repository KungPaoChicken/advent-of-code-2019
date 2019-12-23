from collections import Counter


def load(reactions):
    formulas = {}
    reactions = [r.split(" => ") for r in reactions.split("\n")]
    for inputs, output in reactions:
        inputs = [i.split() for i in inputs.split(", ")]
        inputs = [(name, int(num)) for num, name in inputs]
        num, name = output.split()
        output = (name, int(num))
        formulas[output] = inputs
    return formulas


reactions = load(
    """157 ORE => 5 NZVS
165 ORE => 6 DCFZ
44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL
12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ
179 ORE => 7 PSHF
177 ORE => 5 HKGWZ
7 DCFZ, 7 PSHF => 2 XJWVT
165 ORE => 2 GPVTF
3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT"""
)


from time import sleep


def get(materials):
    materials = materials
    while len(materials.keys()) != 1 or list(materials.keys())[0] != "ORE":
        inputs = Counter()
        for item, amount in materials.items():
            if item == "ORE":
                inputs.update({item: amount})
                continue
            for k in reactions.keys():
                output, output_amount = k
                if output == item:
                    if amount % output_amount == 0:
                        inputs.update(
                            {
                                input_item: amount // output_amount * input_amount
                                for input_item, input_amount in reactions[k]
                            }
                        )
                    else:
                        inputs.update({item: amount})
                    break
        if materials == inputs:
            print("EQUAL")
            for item, amount in inputs.items():
                if item == "ORE":
                    continue
                for output, output_amount in reactions.keys():
                    if item == output:
                        inputs[item] = (amount // output_amount + 1) * output_amount
        print(inputs)
        sleep(1)
        materials = inputs
    print(materials)


get({"FUEL": 1})
# print(get({"ORE": 1}))

