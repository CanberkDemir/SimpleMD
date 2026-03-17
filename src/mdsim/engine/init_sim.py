from ase import Atoms
from ase.calculators.lj import LennardJones
from mdsim.io.read_config import load_config
import numpy as np

def createAseSystem(config) -> Atoms:
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

def vectorSum(vectorArray) -> np.ndarray:
    # The vector should be in the shape array(n,3)
    newArray = np.array()
    for i in vectorArray:
        num = np.sqrt(np.sum(np.power(i,2)))
        np.concatenate((newArray, np.array(num)), axis=None)
    return newArray

def setInitialPosition(system, config) -> Atoms:
    minDist = 0
    while minDist < config["forces"]["sigma"]:
        system.rattle()
        for i in range(len(system)):
            distance = system.get_distances(i, range(len(system)), mic=True)
            if float(0) in distance:
                zeroarr = np.array([0])
                distance = np.setdiff1d(distance, zeroarr)
            if min(distance) > minDist:
                minDist = min(distance) 
    return system

def setInitialVelocity(system, config) -> Atoms:
    kb = 1
    kinEnergy = 1.5*kb*config["system"]["temperature"]*len(system)
    masses = system.get_masses()
    boolLogic = True
    while boolLogic:
        system.set_velocities(np.random.rand(len(system),3))
        vel = system.get_velocities()
        print(vel)
        velSum = vectorSum(vel)
        print(velSum)
        kinEnergyrvel = np.sum(masses*np.power(velSum,2)/2)
        print(kinEnergy_vel)
    return system

def initMD(system, config) -> Atoms:
    system = setInitialPosition(system, config)
    system = setInitialVelocity(system, config)
    return system

def main():
    cfg = load_config('configs/lf_nvt.toml')
    system = createAseSystem(cfg)
    print(system)
    print(cfg)
    #system = initMD(system, cfg)
