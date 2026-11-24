#!/usr/bin/env python3
"""Rebuild all active GitHub profile SVG assets."""

import gen_architecture
import gen_banners
import gen_career
import gen_projects
import gen_skills_grid


def main() -> None:
    gen_banners.generate()
    gen_skills_grid.generate()
    gen_projects.generate()
    gen_architecture.generate()
    gen_career.generate()


if __name__ == "__main__":
    main()