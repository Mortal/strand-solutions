import json


linedrawing = {
        (-1,-1):"╲",
        (1,1):"╲",
        (1,-1):"╱",
        (-1,1):"╱",
        (0,1):"─",
        (0,-1):"─",
        (1,0):"│",
        (-1,0):"│",
        }


def main() -> None:
    with open("data.json") as fp:
        data = [json.loads(line) for line in fp]
    data.sort(key=lambda d: d["date"])
    for day in data:
        grid = [[" "] * (2 * 6) for _ in range(2 * 8)]
        locs = [divmod(int(x), 6) for x in day["loc"].split("|")]
        ix = 0
        allwords = [(day["spangram"], [divmod(int(x), 6) for x in day["spangramloc"].split("|")])]
        for w in day["words"].split("|"):
            allwords.append((w, locs[ix : ix + len(w)]))
            ix += len(w)
        allwords.sort(key=lambda x: min(x[1]) + max(x[1]))
        for wi, (w, locs) in enumerate(allwords):
            grid[wi].append(w)
            for i, letter in enumerate(w):
                a, b = locs[i]
                grid[2 * a][2 * b] = letter.upper()
                if i:
                    c, d = locs[i - 1]
                    grid[a + c][b + d] = linedrawing[a - c, b - d]
        print(f'\n## {day["date"]}\n')
        for gridline in grid:
            print("\t" + "".join(gridline).rstrip())


if __name__ == "__main__":
    main()
