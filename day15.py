def hash(inpt):
    value = 0
    for alphabet in inpt:
        value += ord(alphabet)
        value *= 17
        value %= 256

    return value

def main(input_sequence):
    total = 0
    steps = input_sequence.split(',')
    for step in steps:
        step_result = hash(step.replace('\n', ''))
        total += step_result
    return total


sequence = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"

result = main(sequence)
print(result)
