import argparse
import ast


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("filename", type=str)
    p.add_argument("--function_name", type=str)
    p.add_argument("--additional_paths", type=list)

    args = p.parse_args()

    with open(args.filename) as f:
        text = f.read()
        tree = ast.parse(text)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                print(node.name)


if __name__ == "__main__":
    main()