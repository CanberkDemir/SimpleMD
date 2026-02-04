from ase import Atoms
from ase.calculators.lj import LennardJones
from mdsim.io.read_config import load_config
import numpy as np

def createAseSystem(config):
    system = Atoms(config['system']['atoms'], 
                 cell=config['system']['box'], 
                 pbc=[1, 1, 1]
                 )
    if 'lennard' or 'jones' in config['forces']['type']:
        # You can also add cutoff here think about it
        lj_instance = LennardJones(
                sigma=config['forces']['sigma'],
                epsilon=config['forces']['epsilon'],
                )
        system.calc = lj_instance
    return system

def initializeMd(system, config):
    kb = 1
    kinEnergy = 1.5*kb*config["system"]["temperature"]*config["system"]["n_particles"]
    masses = system.get_masses()
    min_distance = 0
    while min_distance < 1:
    # First make the distances between particles at least 'sigma'
    # Then make their velocities equilibriated
    return None

def main():
    cfg = load_config('configs/lf_nvt.toml')
    system = createAseSystem(cfg)
    print(system)
    print(cfg)
    print(system.get_masses())
    print(system.get_positions())
    print(system.get_distances("))
