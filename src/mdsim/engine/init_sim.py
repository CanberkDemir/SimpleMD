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
    return None

def main():
    cfg = load_config('configs/lf_nvt.toml')
    system = createAseSystem(cfg)
    print(system)
    print(cfg)
