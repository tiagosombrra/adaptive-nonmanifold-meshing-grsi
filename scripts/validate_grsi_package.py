#!/usr/bin/env python3
from __future__ import annotations

import struct
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "GRSI_SUBMISSION.txt",
    "GRSI_LIABILITY.txt",
    "INSTALL_WINDOWS.txt",
    "DATA_PROVENANCE.md",
    "GRSI_FORM_VALUES.txt",
    "LICENSE",
    "THIRD_PARTY_LICENSES.md",
    "reproduce_eistute_windows.bat",
    "reproduce_eistute_linux.sh",
    "docs/GRSI_REVIEW_GUIDE.md",
    "assets/grsi_representative.png",
    "reference/eistute_stage4.obj",
    "reference/eistute_metrics.csv",
    "reference/eistute_stage4.json",
    "scripts/verify_reference.py",
    "scripts/verify_eistute.py",
]


def png_dimensions(path: Path) -> tuple[int, int]:
    with path.open("rb") as stream:
        signature = stream.read(8)
        if signature != b"\x89PNG\r\n\x1a\n":
            raise ValueError("not a PNG file")
        length = struct.unpack(">I", stream.read(4))[0]
        chunk_type = stream.read(4)
        if chunk_type != b"IHDR" or length < 8:
            raise ValueError("missing PNG IHDR")
        width, height = struct.unpack(">II", stream.read(8))
        return width, height


def main() -> None:
    errors: list[str] = []

    for relative in REQUIRED_FILES:
        path = ROOT / relative
        if not path.is_file():
            errors.append(f"missing required file: {relative}")

    image_path = ROOT / "assets/grsi_representative.png"
    if image_path.is_file():
        try:
            dimensions = png_dimensions(image_path)
            if dimensions != (250, 250):
                errors.append(
                    f"representative image is {dimensions[0]}x{dimensions[1]}, "
                    "expected 250x250"
                )
        except ValueError as exc:
            errors.append(f"invalid representative image: {exc}")

    liability = ROOT / "GRSI_LIABILITY.txt"
    if liability.is_file():
        text = liability.read_text(encoding="utf-8")
        if "[INSERT SUBMISSION DATE]" in text or '[TYPE "CONFIRMED"' in text:
            errors.append(
                "GRSI_LIABILITY.txt still contains author-confirmation placeholders"
            )

    provenance = ROOT / "DATA_PROVENANCE.md"
    if provenance.is_file():
        text = provenance.read_text(encoding="utf-8")
        if "Author confirmation required before submission" in text:
            errors.append(
                "DATA_PROVENANCE.md still requires the author to select and confirm "
                "the applicable provenance option"
            )

    preprint = ROOT / "paper/preprint.pdf"
    if not preprint.is_file():
        print(
            "NOTICE: paper/preprint.pdf is not present. A different direct PDF URL "
            "may be used in the GRSI form."
        )

    if errors:
        print("GRSI package validation found unresolved items:")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)

    print("GRSI repository package structure verified.")
    print("Representative image verified: 250x250 PNG.")


if __name__ == "__main__":
    main()
