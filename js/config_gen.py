#!/usr/bin/env python3
import sys
import json


def replace(fname, search, replace):
    if search == replace:
        return

    txt = ""
    with open(fname, "r") as inp:
        txt = inp.read()
    txt.replace(search, replace)
    with open(fname, "w") as out:
        out.write(txt)


def main():
    if len(sys.argv) != 2:
        sys.exit(1)

    config = {}
    with open(sys.argv[1], "r") as cfg:
        config = json.load(cfg)

    with open("src/config.js", "w") as cfg:
        lines = [
            "// Do not edit this file!",
            "// This file was autogenerated by running:",
            "// {}".format(" ".join(sys.argv)),
            "export const config = {};".format(json.dumps(config, sort_keys=True, indent=4)),
        ]
        cfg.write("\n".join(lines))

    replace("develop/envoy.yaml", "android-emulator-ac251-default-rtdb", config["projectId"])
    replace("docker/envoy.yaml", "android-emulator-ac251-default-rtdb", config["projectId"])


if __name__ == "__main__":
    main()

