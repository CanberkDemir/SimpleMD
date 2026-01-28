import argparse
import importlib

def run_module(module_path: str, *args):
    module = importlib.import_module(module_path)

    if not hasattr(module, "main"):
        raise AttributeError(f"{module_path} has no main()")

    return module.main(*args)


def main():
    parser = argparse.ArgumentParser("mdsim")
    sub = parser.add_subparsers(dest="command", required=True)

    run_p = sub.add_parser("run", help="Run MD simulation")
    run_p.add_argument("config")

    exec_p = sub.add_parser("exec", help="Run arbitrary module")
    exec_p.add_argument("module")

    args = parser.parse_args()

    if args.command == "run":
        run_module("mdsim.engine.run", args.config)

    elif args.command == "exec":
        run_module(args.module)


if __name__ == "__main__":
    main()
