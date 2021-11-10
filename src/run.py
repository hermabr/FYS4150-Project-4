import argparse
import itertools
import numpy as np
from collections import defaultdict


def get_all_states(L):
    N = L ** 2

    spins = itertools.product([-1, 1], repeat=N)

    state_summary = []
    degeneracies = defaultdict(int)

    for spin in spins:
        spin = np.array(spin).reshape(L, L)

        positive_spins = np.sum(spin == 1)

        E_h = np.multiply(spin, np.roll(spin, 1, axis=0))
        E_v = np.multiply(spin, np.roll(spin, 1, axis=1))
        E_s = -(np.sum(E_h) + np.sum(E_v))

        M_s = np.sum(spin)

        degeneracies[E_s] += 1

        state_summary.append([positive_spins, E_s, M_s])

    for state in state_summary:
        state.append(degeneracies[state[1]])

    # write state summary to csv file with header
    np.savetxt(
        "output/state_summary.csv",
        state_summary,
        delimiter=",",
        fmt="%s",
        header="positive spins,E(s),M(s),degeneracy",
        comments="",
    )

    print("Successfully saved state summary to file")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="To run the python and julia scripts")
    parser.add_argument(
        "-s",
        "--states",
        help="To get information about different states",
        action="store_true",
    )
    parser.add_argument(
        "-a",
        "--all",
        help="To run everything",
        action="store_true",
    )

    args = parser.parse_args()

    if not any(vars(args).values()):
        parser.print_help()
    if args.states or args.all:
        get_all_states(2)