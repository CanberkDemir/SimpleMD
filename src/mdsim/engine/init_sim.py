from ase import Atoms
from mdsim.io.read_config import load_config

def create_atoms(config):
    return None

def initialize_md(Atoms, config):
    return None

def main():
    cfg = load_config('configs/lf_nvt.toml')
    print(cfg)
