from sympy import symbols, solve, nonlinsolve


def parse_input_file(input_file: str) -> list[[list[int], list[int]]]:
    input_file = open(input_file, 'r')
    lines = input_file.readlines()

    stones = []
    for this_line in lines:
        position, velocity = this_line.strip().split(" @ ")

        stones.append([
            [int(x) for x in position.split(",")],
            [int(x) for x in velocity.split(",")]
        ])

    return stones


def make_equations_lines(stones: list[[list[int], list[int]]]) -> list:
    equations = []
    '''
    px, py, pz | vx, vy, vz:
    px(t) = px + vx*t
    py(t) = py + vy*t
    pz(t) = pz + vz*t
    
    x as f(y):
    py + vy*t = y ==> t = (y - py)/vy
    x = px + vx * (y - py)/vy
    '''
    y = symbols('y')
    t = symbols('t')
    for position, velocity in stones:
        px, py, pz = position
        vx, vy, vz = velocity

        equations.append([px + vx * (y - py) / vy,
                          px + vx * t])

    return equations


def find_crossings(equations: list, low: int, high: int) -> int:
    crossings = 0
    for i in range(len(equations)):
        print(i, 'of ', len(equations))
        for j in range(i + 1, len(equations)):
            sol = solve(equations[i][0] - equations[j][0])
            if len(sol) > 0:
                y = sol[0]
                x = eval(str(equations[i][0]))
                ta = solve(equations[i][1] - x)
                tb = solve(equations[j][1] - x)
                if low <= x <= high and low <= y <= high and ta[0] >= 0 and tb[0] >= 0:
                    crossings += 1

    return crossings


def make_equations_system(stones: list[[list[int], list[int]]]) -> [list, int]:
    equations = []
    '''
    px, py, pz | vx, vy, vz:
    pxi(t) = pxi + vxi*t
    pyi(t) = pyi + vyi*t
    pzi(t) = pzi + vzi*t

    want to prep to find:
    
    qx(t) = qpx + qvx*t
    qy(t) = qpy + qvy*t
    qz(t) = qpz + qvz*t
    
    such that:
    qx(t1) = pxi(t1)
    qy(t1) = pyi(t1)
    qz(t1) = pzi(t1)
    
    qx(t2) = pxi(t2)
    qy(t2) = pyi(t2)
    qz(t2) = pzi(t2)

    '''
    qx = symbols('qx')
    qy = symbols('qy')
    qz = symbols('qz')

    qvx = symbols('qvx')
    qvy = symbols('qvy')
    qvz = symbols('qvz')

    t = [symbols('t%d' % i) for i in range(len(stones))]

    counter = 0

    for position, velocity in stones:
        px, py, pz = position
        vx, vy, vz = velocity

        equations.append(qx + qvx * t[counter] - px - vx * t[counter])
        equations.append(qy + qvy * t[counter] - py - vy * t[counter])
        equations.append(qz + qvz * t[counter] - pz - vz * t[counter])

        counter += 1

    return equations, len(stones)


def find_magic(equations: list, len_stones: int) -> [int, int, int]:
    qx = symbols('qx')
    qy = symbols('qy')
    qz = symbols('qz')

    qvx = symbols('qvx')
    qvy = symbols('qvy')
    qvz = symbols('qvz')

    t = [symbols('t%d' % i) for i in range(len_stones)]

    results = nonlinsolve(equations[0:9], [qx, qy, qz, qvx, qvy, qvz, *t])

    return list(results)
