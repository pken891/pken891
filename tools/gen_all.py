#!/usr/bin/env python3
"""Rebuild all active GitHub profile SVG assets."""

import gen_banners
import gen_career
import gen_projects


def main() -> None:
    gen_banners.generate()
    gen_projects.generate()
    gen_career.generate()


if __name__ == "__main__":
    main()