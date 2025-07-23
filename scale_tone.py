# scale_generator

SCALES = {
    "major":      [2, 2, 1, 2, 2, 2, 1],
    "minor":      [2, 1, 2, 2, 1, 2, 2],
    "harmonic":   [2, 1, 2, 2, 1, 3, 1],
    "melodic":    [2, 1, 2, 2, 2, 2, 1]
}

NOTES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

def generate_scale(root: str, mode: str):
    root = root.upper()
    if root not in NOTES:
        raise ValueError("Неверная нота")
    intervals = SCALES.get(mode.lower())
    if not intervals:
        raise ValueError("Неверная тональность")

    idx = NOTES.index(root)
    scale = [root]
    for step in intervals:
        idx = (idx + step) % 12
        scale.append(NOTES[idx])
    return scale

if __name__ == "__main__":
    import sys
    root_note = sys.argv[1]
    mode = sys.argv[2]
    print(" → ".join(generate_scale(root_note, mode)))