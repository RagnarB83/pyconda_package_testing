import subprocess as sp
from math import isclose


def pygrep(string, file):
    with open(file) as f:
        for line in f:
            if string in line:
                stringlist = line.split()
                return stringlist


def test_xtb():
    with open("file.xyz", "w") as xyzfile:
        xyzfile.write("2\n")
        xyzfile.write("title\n")
        xyzfile.write("H 0.0 0.0 0.0\n")
        xyzfile.write("F 0.0 0.0 1.0\n")
    command_list = ["xtb", "file.xyz"]
    with open("xtb.out", "w") as ofile:
        process = sp.run(
            command_list,
            check=True,
            stdout=ofile,
            stderr=ofile,
            universal_newlines=True,
        )
    if process.returncode == 0:
        print("xtb ran successfully")

    energy_list = pygrep("TOTAL ENERGY", "xtb.out")
    print(energy_list)
    energy = float(energy_list[3])
    print("energy:", energy)
    refenergy = -5.219468351901
    print("refenergy:", refenergy)
    assert isclose(energy, refenergy)


# test_xtb()
