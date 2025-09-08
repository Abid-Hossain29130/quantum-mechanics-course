# Week 09 — Chapter 6: Spherically Symmetric Systems & Potentials

**Dates worked:**  Aug 28, 2025 - Sep 9, 2025  [28/08/2025-09/08/2025]
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

## 2. Deep-Dive Questions & Answers

### 2.1. Separation & Centrifugal Barrier
**Question:** In the separation of the Schrödinger equation for a spherically symmetric potential, why is the angular part universal while the radial part is potential-specific? How does the centrifugal term physically prevent a non-zero angular momentum particle from collapsing into the origin?  
**Answer:**  
The angular equation arises purely from the symmetry of space (spherical coordinates), so it’s independent of the exact potential — it always yields spherical harmonics. The radial part, however, includes the centrifugal term \(\frac{\ell(\ell+1)\hbar^2}{2mr^2}\), which acts as an effective repulsive potential near \(r \to 0\). This barrier prevents particles with non-zero angular momentum from reaching the origin, as going too close would significantly raise their energy.:contentReference[oaicite:0]{index=0}

---

### 2.2. Asymptotic Behavior of Radial Solutions
**Question:** Why must we analyze the wavefunction’s asymptotic behavior as \(r \to 0\) and \(r \to \infty\) before solving hydrogen’s radial equation?  
**Answer:**  
We assume \(R(r) = e^{-\kappa r} F(r)\) to ensure physical acceptability: as \(r \to \infty\), the exponential makes the wavefunction vanish (bound-state condition), while near \(r \to 0\) we require \(R(r)\) to remain finite and regular. Asymptotic analysis ensures \(F(r)\) is well-behaved and prevents divergent behavior.:contentReference[oaicite:1]{index=1}

---

### 2.3. Principal Quantum Number & Energy Quantization
**Question:** Why does the power series solution for the hydrogen radial equation need to terminate, and how does that lead to the principal quantum number \(n\)?  
**Answer:**  
If the series doesn’t terminate, the wavefunction diverges at large \(r\), making it non-normalizable. Allowing only polynomial solutions (i.e., terminating series) ensures square-integrability. This requirement quantizes the allowed energies, introducing the principal quantum number \(n\), which directly yields the discrete hydrogen energy levels.:contentReference[oaicite:2]{index=2}

---

### 2.4. Expectation vs Most Probable Radius
**Question:** Why is the average radius \(\langle r \rangle = 1.5a_0\) different from the most probable radius \(a_0\) in hydrogen?  
**Answer:**  
\(\langle r \rangle\) is an average weighted by probability density, reflecting contributions from all radii — including the tail of the distribution. The most probable radius arises from the peak of the radial density \(r^2|R(r)|^2\). Its difference demonstrates the asymmetry and spread of the probability distribution — a key quantum mechanical insight about measurement outcomes.

---

### 2.5. Degeneracy in Hydrogen
**Question:** Why do multiple \(\ell\), \(m\) combinations correspond to the same energy level in the hydrogen atom?  
**Answer:**  
The hydrogen atom’s potential depends only on \(r\) (not angles), giving it full spherical symmetry. Energy eigenvalues depend only on \(n\), not on \(\ell\) or \(m\). This symmetry generates degeneracy: all orbitals with the same \(n\) share energy.:contentReference[oaicite:3]{index=3}

---

### 2.6. Conceptual & Foundations

- **Why is separation only possible for spherically symmetric potentials?**  
  Because only then are the angular and radial dependencies independent, letting us solve separately via symmetry.

- **Does angular independence mean orbital shapes are universal?**  
  Yes — spherical harmonics are universal for any central potential; only the radial part changes based on the specific \(V(r)\).

- **Physical significance of \( \ell(\ell + 1) \):**  
  It represents the eigenvalue of the squared angular momentum operator \(L^2\), showing how angular momentum quantizes in quantum mechanics.

- **Quantization of \(m\) and \(\ell\):**  
  Requires the angular solution functions to be single-valued and continuous over \(\theta\), \(\phi\), leading to integer quantization of \(\ell\) and \(m\).

- **Exam-essential insights from spherical harmonics derivation:**  
  The central results: \( L^2 Y_{\ell m} = \hbar^2\ell(\ell+1)Y_{\ell m} \) and behavior of angular wavefunctions — focus on these, skip longer recursion derivations unless asked.

- **Predicting angular and radial nodes uniquely:**  
  Number of angular nodes = \(\ell\); number of radial nodes = \(n - \ell - 1\).

- **Connection to orbital shapes:**  
  Spherical harmonics directly describe orbital shapes: \(\ell=0\) gives spherically symmetric s orbitals; \(\ell=1\) gives dumbbell-shaped p orbitals; \(\ell=2\) gives d-orbitals' clover shapes.

- **What next after spherical harmonics?**  
  You proceed to the radial equation. Combine both solutions (\(R(r)\) and \(Y_{\ell m}\)) to form full hydrogenic wavefunctions \(\psi_{n\ell m}(r, \theta, \phi)\).
--- 