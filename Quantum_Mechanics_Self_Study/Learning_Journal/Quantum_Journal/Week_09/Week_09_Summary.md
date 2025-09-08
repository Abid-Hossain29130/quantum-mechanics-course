# Week 09 — Chapter 6: Spherically Symmetric Systems & Potentials

**Dates worked:** June–July 2025  
**Core focus:** Completed Chapter 6 — covering separation of variables in spherical coordinates, radial and angular wavefunctions, hydrogenic systems, energy degeneracy, and harmonic oscillators.

---

## 1. Chapter Overview

Covered topics include:

- Schrödinger equation in spherical coordinates  
- Angular part (spherical harmonics) and radial part of the wavefunction  
- Angular momentum quantization and eigenvalues  
- The centrifugal barrier in the effective potential  
- Solutions for 3D square well and harmonic oscillator  
- Hydrogen atom: wave functions, energy levels, and degeneracy  
- Probability current density  
- Solved exercise problems and university-style questions

---

## 2. Deep-Dive Questions & Answers

### Separation & Centrifugal Barrier  
**Question:** In the separation of the Schrödinger equation for a spherically symmetric potential, why is the angular part universal while the radial part is potential-specific? How does the centrifugal term physically prevent a non-zero angular momentum particle from collapsing into the origin?  
**Answer:**  
The angular equation arises purely from symmetry and always leads to spherical harmonics \(Y_{\ell m}\). The radial part includes a centrifugal term
\(\frac{\ell(\ell+1)\hbar^2}{2mr^2}\), 
which acts like a repulsive potential that increases sharply as \(r \to 0\), preventing a particle with \(\ell > 0\) from reaching the origin. ([source]([en.wikipedia.org](https://en.wikipedia.org/wiki/Particle_in_a_spherically_symmetric_potential?utm_source=chatgpt.com)))

---

### Asymptotic Behavior of Radial Solutions  
**Question:** Why must we analyze the wavefunction’s asymptotic behavior as \(r \to 0\) and \(r \to \infty\) before solving the hydrogenic radial equation?  
**Answer:**  
At \(r \to \infty\), we require the solution to vanish for normalizability, yielding \(R(r) \sim e^{-\kappa r}\). At \(r \to 0\), the solution must remain finite, so the power series \(F(r)\) must not diverge. This ensures a physically acceptable, normalizable wavefunction. ([source]([galileo.phys.virginia.edu](https://galileo.phys.virginia.edu/classes/751.mf1i.fall02/HydrogenAtom.htm?utm_source=chatgpt.com)))

---

### Quantization & the Principal Quantum Number  
**Question:** Why does the series solution terminate, leading to the principal quantum number \(n\)?  
**Answer:**  
For convergence and normalizability, the series must terminate—only finite polynomials give acceptable bound-state wavefunctions. That termination condition imposes discrete energy levels, introducing \(n\), the principal quantum number. ([source]([galileo.phys.virginia.edu](https://galileo.phys.virginia.edu/classes/751.mf1i.fall02/HydrogenAtom.htm?utm_source=chatgpt.com)))

---

### Expectation vs Most Probable Radius  
**Question:** Why is \(\langle r \rangle = 1.5\,a_0\) different from the most probable radius \(a_0\)?  
**Answer:**  
\(\langle r \rangle\) is a weighted average over the full probability distribution, while the most probable radius comes from the peak of the radial density \(r^2|R(r)|^2\). The difference reflects the asymmetry of the distribution and is a key insight into quantum behavior.

---

### Degeneracy in Hydrogen  
**Question:** Why do multiple \(\ell\) and \(m\) states share the same energy in hydrogen?  
**Answer:**  
Hydrogen’s potential is spherically symmetric, so energy depends only on \(n\). Different \((\ell, m)\) combinations correspond to the same \(n\), resulting in degeneracy. ([source]([en.wikipedia.org](https://en.wikipedia.org/wiki/Hydrogen_atom?utm_source=chatgpt.com)))

---

## 3. Conceptual Foundations

- Separation works only for central (\(V(r)\)) potentials due to their symmetry.  
- Spherical harmonics are universal shapes; radial differences arise from different potentials.  
- The term \(\ell(\ell + 1)\) comes from the eigenvalues of angular momentum in QM: \(L^2Y = \hbar^2 \ell(\ell+1)Y\).  
- Quantization of \(\ell\) and \(m\) stems from boundary conditions (single-valuedness, orthogonality).  
- Angular nodes = \(\ell\), radial nodes = \(n - \ell - 1\).  
- Orbital shapes (s, p, d) arise from \(\ell=0,1,2\) spherical harmonics.  
- The full wavefunction is \(\psi_{n\ell m}(r,\theta,\phi) = R_{n\ell}(r)Y_{\ell m}(\theta,\phi)\).

---

## 4. Reflection

Completing Chapter 6 sharpened my understanding of quantum symmetry, orbital structure, math methods, and their physical meaning. I’m now ready to integrate computational visualizations into my portfolio — reinforcing both theory and presentation.
