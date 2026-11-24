# The Funniest Toaster Error Message — make.fun entry
# (u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)
#
# One line, at most 120 characters, written to /output/entry.txt:
# the error message a kitchen toaster shows its owner when something
# goes wrong. It must read like a real message on a real appliance
# and make someone laugh. The line is a fixed string: the grader
# runs the program twice and the runs must be deterministic, so there
# is no randomness and no input. The gate allows 1 to 120 characters
# of UTF-8, not only whitespace.

LINE = (
    "ERROR 04: BREAD REFUSED. It saw what happened to the last slice "
    "and declines to participate."
)

MAX_CHARS = 120


def main() -> None:
    assert 1 <= len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars, gate is 1-120"
    assert "\n" not in LINE, "entry must be a single line"
    assert LINE.strip() == LINE, "entry must not be only whitespace / padded"
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"Wrote {len(LINE)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
