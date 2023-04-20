Period = 0.2689
Radius = 0.225
mass = 0.0008


def main(Period, Radius, mass):
    Vc = (2 * 3.1415 * Radius)/Period
    print(Vc)

    Ac = (Vc * Vc)/Radius
    print(Ac)

    Ft = mass * Ac
    print(Ft)

main(Period, Radius, mass)