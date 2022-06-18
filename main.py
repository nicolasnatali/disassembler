def disassemble(instructions):
    """
    Performs a binary-to-MIPS disassembly.

    :param instructions: A list of binary instructions.
    :return: A list of MIPS instructions.
    """
    register = {
        '00000': '$zero',
        '00001': '$at',
        '00010': '$v0',
        '00011': '$v1',
        '00100': '$a0',
        '00101': '$a1',
        '00110': '$a2',
        '00111': '$a3',
        '01000': '$t0',
        '01001': '$t1',
        '01010': '$t2',
        '01011': '$t3',
        '01100': '$t4',
        '01101': '$t5',
        '01110': '$t6',
        '01111': '$t7',
        '10000': '$s0',
        '10001': '$s1',
        '10010': '$s2',
        '10011': '$s3',
        '10100': '$s4',
        '10101': '$s5',
        '10110': '$s6',
        '10111': '$s7',
        '11000': '$t8',
        '11001': '$t9',
        '11010': '$k0',
        '11011': '$k1',
        '11100': '$gp',
        '11101': '$sp',
        '11110': '$fp',
        '11111': '$ra'
    }
    operation = {
        '100011': 'lw',
        '001101': 'ori',
        '101011': 'sw',
        '100000': 'add',
        '100100': 'and',
        '001000': 'jr',
        '100010': 'sub',
        '000010': 'j'
    }
    category = {
        'lw': 'data_transfer',
        'ori': 'logical',
        'sw': 'data_transfer'
    }
    result = list()
    for i in instructions:
        if i[0:6] == '000000':
            result.append(f'{operation[i[26:32]]} {register[i[16:21]]}, {register[i[6:11]]}, {register[i[11:16]]}')
        elif i[0:6] == '000010' or i[0:6] == '000011':
            result.append(f'{operation[i[0:6]]} {i[6:32]}')
        else:
            if category[operation[i[0:6]]] == 'data_transfer':
                result.append(f'{operation[i[0:6]]} {register[i[11:16]]}, {i[16:32]}({register[i[6:11]]})')
            else:
                result.append(f'{operation[i[0:6]]} {register[i[11:16]]}, {register[i[6:11]]}, {i[16:32]}')
    return result


def main():
    """
    Runs the disassembler program.

    :return: Nothing.
    """
    instructions = [
        '00000001101011100101100000100100',
        '10001101010010010000000000001000',
        '00001000000000010010001101000101',
        '00000010101010010101100000100010',
        '00000011111000000000000000001000',
        '00110101111100001011111011101111',
        '10101110100011010000000000100000',
        '00000010110011010101000000100000'
    ]
    for instruction in disassemble(instructions):
        print(instruction)


if __name__ == '__main__':
    main()
