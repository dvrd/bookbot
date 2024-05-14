import sys


def read_file(path: str) -> str:
    with open(path) as f:
        file_contents = f.read()
        return file_contents


def report(words: int, freq: dict) -> None:
    freq_arr = [{"name": c, "num": freq[c]} for c in freq]
    freq_arr.sort(reverse=True, key=lambda dict: dict["num"])

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the document")
    for data in freq_arr:
        print(f"The {data["name"]} character was found {data["num"]} times")
    print("--- End report ---")


def main() -> int:
    path_to_file = "books/frankenstein.txt"
    contents = read_file(path_to_file)
    words = contents.split()
    freq = dict()
    for c in contents:
        if c.isalpha() == False:
            continue
        c = c.lower()
        if freq.get(c) == None:
            freq[c] = 1
        else:
            freq[c] += 1

    report(len(words), freq)
    return 0


if __name__ == "__main__":
    sys.exit(main())
