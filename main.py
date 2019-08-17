# -:R, ():series, []:parallel
from fractions import Fraction


def unique(l: list) -> list:
    ret: list = []
    for i in l:
        if len(ret) == 0 or ret[-1] != i:
            ret.append(i)
    return ret


def flat(s: str, pre: str) -> str:
    return s[1:-1] if s.startswith(pre) else s


def igsplit(s: str) -> list:
    opb = 0
    ret = ['']
    for i in s:
        if i == ',' and opb == 0:
            ret.append('')
        else:
            ret[-1] += i
        if i in ('(', '['):
            opb += 1
        if i in (')', ']'):
            opb -= 1

    while len(ret[-1]) == 0:
        ret.pop()

    return ret


connections = [[]]
connections.append([('-', Fraction(1, 1))])
connections.append([('(-,-)', Fraction(2, 1)), ('[-,-]', Fraction(1, 2))])

toCalc = int(input())
for i in range(1, toCalc+1):
    if len(connections) <= i:
        toAppend = []
        for j in range(1, i//2+1):
            for circuit1 in connections[j]:
                for circuit2 in connections[i-j]:
                    series = ','.join(sorted(
                        igsplit(flat(circuit1[0], '(')+','+flat(circuit2[0], '('))))
                    toAppend.append(
                        (f'({series})', circuit1[1]+circuit2[1]))

                    parallel = ','.join(
                        sorted(igsplit(flat(circuit1[0], '[')+','+flat(circuit2[0], '['))))
                    toAppend.append(
                        (f'[{parallel}]', circuit1[1]*circuit2[1]/(circuit1[1]+circuit2[1])))

        toAppend.sort()
        print(f'{i} before unique: {len(toAppend)}')
        toAppend = unique(toAppend)
        connections.append(toAppend)

    toPrint = []
    for j in range(len(connections[i])):
        toPrint.append((connections[i][j][0], (
            connections[i][j][1].numerator, connections[i][j][1].denominator)))

    open(f'data_{i}', mode='wt', encoding='utf-8').write(str(toPrint))
    print(f'{i} done. The number of the circuit is {len(toPrint)}')
