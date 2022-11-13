def e_distro(electrons):
    all_electrons = electrons
    distribution = []
    counter = 1

    while all_electrons > 0:
        max_shell_qty = 2 * (counter ** 2)
        if max_shell_qty <= all_electrons:
            distribution.append(max_shell_qty)
            all_electrons -= max_shell_qty
            counter += 1
        else:
            distribution.append(all_electrons)
            all_electrons = 0
    return distribution


electron_qty = int(input())
print(e_distro((electron_qty)))
