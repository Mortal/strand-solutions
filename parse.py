import glob
import json
import re
import datetime


def main() -> None:
    with open("data.json", "w") as ofp:
        for f in glob.glob("*-*-?????-?-?-?-?"):
            mdy = f[:-9]
            dt = datetime.datetime.strptime(mdy, "%B-%d-%Y")
            with open(f) as fp:
                s = fp.read()
            data = {mo.group(1): mo.group(2) for mo in re.finditer(r'<span id="(.*)" hidden>(.*)</span>', s)}
            ofp.write(json.dumps({"date":str(dt.date()),**data}) + "\n")


if __name__ == "__main__":
    main()
