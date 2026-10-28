# Relative metric estimates near reducible Yang–Mills connections

**Bernd Johannes Wuebben** · 28 October 2026 · 14 pages

[Read the paper](main.pdf) · [LaTeX source](main.tex) ·
[Abstract and citation](https://bwuebben.github.io/papers/relative-metrics-reducible-yang-mills/) ·
[Zenodo:23740619](https://zenodo.org/records/23740619) ·
[Geometry & moduli guide](https://bwuebben.github.io/research/geometry/) ·
[Author ORCID](https://orcid.org/0009-0002-4588-3284)

Near a reducible Yang–Mills connection, stabilizers can grow and positive orbit
eigenvalues can approach zero at arbitrarily different rates. This paper proves
that the classical quadratic model nevertheless approximates the actual
surface gauge quotient metric and its complete small gauge spectrum with a
uniform relative error.

## Results

Let `A_0` be a central Yang–Mills connection on a closed oriented Riemannian
surface, let `h` be a harmonic deformation parameter in the quadratic moment-map
zero set, and let `T_h` be the infinitesimal action of the stabilizer of `A_0`.

- **Quotient metric:** the natural `L²` metric and the linear reduction metric
  compare by factors `1 ± C|h|²` on every orbit-type stratum, with the same
  constant. The paper computes the leading correction using the fixed Green
  operators at `A_0`.
- **Small spectrum:** every small eigenvalue of the real gauge Laplacian
  `d_A* d_A` compares with an eigenvalue of `T_h* T_h` by the same relative
  factors. Zero eigenvalues and changes in kernel dimension are included;
  the remaining spectrum has a fixed positive gap.
- **Curved examples:** quaternionic projective and hyperbolic reductions admit
  exact orbit and quotient-metric formulas. A weighted four-cycle is realized
  both by actual surface connections and by these curved reductions, with
  independently vanishing weak weights.

The estimates require no lower bound on ratios between positive orbit
eigenvalues. The proof removes the gauge directions with a fixed spectral gap
before minimizing over the residual finite-dimensional orbit.

## Scope and context

The symplectic local model and singular-reduction foundations are classical;
the proposed contribution is the quantitative analysis of the actual metric
and spectrum. The main theorems concern central Yang–Mills connections on
surfaces. For unitary bundles, these are Hermitian–Einstein connections.
The quaternionic comparison concerns explicit space forms; it does not establish
a general quaternionic Kähler normal form across all stabilizers or determine
an unknown physical compactification metric.

The paper begins a research direction on **metrics and spectra of singular
quotients**. Open questions include general quaternionic Kähler quotients across
stabilizer changes, higher-dimensional HYM quotient metrics with control of the
integrable deformation space, and compact-transition applications with the
necessary physical metric and kinetic data.

Related work:

- [Uniform Hermitian–Einstein spectra for bipartite two-step extensions](https://bwuebben.github.io/papers/uniform-hermitian-einstein-spectra/)
  studies the small Dolbeault spectrum at Hermitian–Einstein metrics near
  stability walls.
- [The Higgs Branch of a Compact Calabi–Yau Transition at Finite Planck Mass](https://bwuebben.github.io/papers/compact-higgs-finite-planck/)
  proves a quaternionic quotient comparison under a freeness hypothesis.

## Build and reproduce

The LaTeX source is self-contained, including its bibliography. With a standard
TeX Live or MiKTeX installation and `latexmk`, run:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The finite checker requires Python 3 and only the standard library:

```sh
python3 checks/check_cycle.py
```

It checks the displayed four-cycle block decomposition, product formula and
kernel jump in 48 exact rational cases, and a quaternionic moment cancellation.
Its output is [checks/cycle_results.json](checks/cycle_results.json).
These calculations check the finite formulas; the analytic and geometric
theorems are proved in the manuscript.

## Files and citation

- `main.pdf` and `main.tex`: released manuscript and corresponding source.
- `checks/`: exact finite checker and its recorded output.
- `manuscript.json`: release metadata and file checksums.
- `CITATION.cff` and `citation.bib`: citation metadata.
- [RIGHTS.md](RIGHTS.md): manuscript and supplementary-file rights.

The version 1.0 archive is [doi:10.5281/zenodo.23740619](https://doi.org/10.5281/zenodo.23740619).
The [concept DOI](https://doi.org/10.5281/zenodo.23740618) identifies the version
series. Cite the version DOI for this exact manuscript. The repository PDF is
the current released version; `manuscript.json` records its checksum.

This repository distributes the released paper. arXiv submission is pending.
