# Appendix B — Quotient-Geometric Synthetic Falsification of VGM Invariants (Version 2)

## B.0 Revised invariant philosophy

The revised benchmark does not identify a raw coefficient, dimensional scale, or chosen kernel parameter with a physical invariant. The relevant object is the law/model class after quotienting coordinate, gauge, unit, field-rescaling, and normalization redundancies.

For the VGM sector considered here, the synthetic fingerprint is organized as

\[
\mathfrak I_{\rm VGM}
=
(d,w,r,\sigma,\operatorname{Spec},\operatorname{Sing},
\operatorname{Aut},\Pi,\mathcal T,\mathcal P).
\]

At the present level:
- \(d\): leading deformation/operator degree;
- \(w\): scaling weights;
- \(r\): rank structure of the transverse kinetic tensor;
- \(\sigma\): signature data when meaningful in the chosen real form;
- \(\operatorname{Spec}\): normalized kinetic/pole spectral structure;
- \(\operatorname{Sing}\): finite pole/singularity locus;
- \(\operatorname{Aut}\): Lorentz and gauge symmetry structure;
- \(\Pi\): dimensionless coordinates, especially \(z=Q^2/\Lambda^2\);
- \(\mathcal T,\mathcal P\): not established by the present VGM kernel and therefore not assigned synthetic evidence.

The dimensional quantity \(\Lambda_{\rm VGM}\) is not treated as a universal invariant. A physical modulus requires a dimensionless ratio such as \(\Lambda_{\rm VGM}/\Lambda_{\rm ref}\). Likewise, the coefficients of a Gaussian Taylor series written in dimensional \(Q^2\) coordinates are coordinate-dependent; the quotient-normalized jet in \(z=Q^2/\Lambda^2\) is the relevant shape fingerprint.

All stochastic experiments use seed 20260812.

## B.1 Experiment 1 — Unit/scale quotient gate

Define

\[
z=\frac{Q^2}{\Lambda^2},
\qquad
F(z)=e^{-z}.
\]

Under \(Q\mapsto sQ,\ \Lambda\mapsto s\Lambda\), the quotient coordinate must satisfy \(z'=z\).

Across 20,000 random samples with scale factors spanning twelve orders of magnitude:
- median \(|\Delta z|\) = 0.000e+00;
- 95th-percentile \(|\Delta z|\) = 4.441e-16;
- median \(|\Delta F|\) = 0.000e+00.

A Q-only rescaling negative control produced median \(|\Delta F|\) = 0.015.

**Decision:** PASS. The dimensionless quotient coordinate \(z\), not raw \(Q\) or \(\Lambda\), carries the kernel shape.

## B.2 Experiment 2 — Lorentz quotient gate

For spacelike momentum,

\[
z=-\frac{k_\mu k^\mu}{\Lambda^2}.
\]

Across 12,000 random spacelike momenta and random boosts with \(|\beta|<0.9\):
- median absolute kernel error = 0.000e+00;
- 95th percentile = 1.110e-16.

The anisotropic negative control had median absolute error 1.096e-03.

**Decision:** PASS.

## B.3 Experiment 3 — Rank, transversality and normalized spectral fingerprint

In Euclidean diagnostic signature define

\[
K_{\mu\nu}(k)=k^2\delta_{\mu\nu}-k_\mu k_\nu.
\]

It obeys \(K_{\mu\nu}k^\nu=0\) and has generic rank three. Under the scalar inverse-kinetic deformation \(K\mapsto K/F\), the null direction and normalized eigenvalue multiplicity pattern should remain unchanged.

| condition                                   |     N |   median_transversality_residual |   p95_transversality_residual |   rank3_fraction |   median_normalized_spectrum_distance |   p95_normalized_spectrum_distance |
|:--------------------------------------------|------:|---------------------------------:|------------------------------:|-----------------:|--------------------------------------:|-----------------------------------:|
| scalar Gaussian inverse-kinetic deformation | 10000 |                      4.47052e-17 |                   9.45472e-17 |           1      |                            1.3598e-16 |                        2.60754e-16 |
| tensor-breaking negative control            | 10000 |                      0.00759614  |                   0.0930636   |           0.0007 |                            0.00550353 |                        0.0631108   |

**Decision:** PASS for the scalar kinetic deformation. Rank/null-space and normalized spectral pattern are stronger identity carriers than raw propagator amplitude.

## B.4 Experiment 4 — Leading scaling degree as an identity-bearing invariant

IR correspondence \(F(0)=1\) alone is insufficient. Compare

\[
F_G(z)=e^{-z},
\qquad
F_{SG}(z)=e^{-z^2}.
\]

Both satisfy \(F(0)=1\), but

\[
1-F_G(z)\sim z,
\qquad
1-F_{SG}(z)\sim z^2.
\]

With 1% multiplicative noise on the deformation magnitude:

| kernel                   |   true_leading_degree |   median_fitted_degree |   p05_fitted_degree |   p95_fitted_degree |
|:-------------------------|----------------------:|-----------------------:|--------------------:|--------------------:|
| Gaussian exp(-z)         |                     1 |               0.997343 |            0.996691 |            0.997975 |
| Super-Gaussian exp(-z^2) |                     2 |               1.99993  |            1.9993   |            2.00058  |

**Decision:** the leading exponent/degree \(d\) is identity-bearing; IR normalization alone is not.

## B.5 Experiment 5 — Singular-locus and pole fingerprint

| kernel                      | propagator         | finite_extra_poles        | massless_pole_z0   | singular_locus_class            |
|:----------------------------|:-------------------|:--------------------------|:-------------------|:--------------------------------|
| Gaussian exp(-z)            | exp(-z)/z          | none                      | preserved          | {0}                             |
| rescaled Gaussian exp(-2z)  | exp(-2z)/z         | none                      | preserved          | {0}                             |
| Super-Gaussian exp(-z^2)    | exp(-z^2)/z        | none                      | preserved          | {0}                             |
| pole-mutant exp(-z)/(1+z^4) | exp(-z)/[z(1+z^4)] | 4 complex roots of z^4=-1 | preserved          | {0} plus 4 finite complex poles |

The pole-mutant kernel is deliberately constructed to share the Gaussian jet through cubic order while introducing four finite complex poles.

**Decision:** \(\operatorname{Sing}\) contains information that finite low-order local jets can miss.

## B.6 Experiment 6 — Quotient-normalized algebraic jet

In dimensional \(x=Q^2\) coordinates,

\[
F(x)=1-\frac{x}{\Lambda^2}+\frac{x^2}{2\Lambda^4}-\cdots.
\]

After quotient normalization,

\[
z=\frac{Q^2}{\Lambda^2},
\qquad
\widetilde F(z)=e^{-z},
\]

the coefficients are fixed:

\[
a_n=\frac{(-1)^n}{n!}.
\]

Hence the normalized finite jet satisfies

\[
a_0-1=0,\quad
a_1+1=0,\quad
2a_2-1=0,\quad
6a_3+1=0,\quad
24a_4-1=0,\ldots
\]

| quantity                        |   coefficient_of_variation |       min |          max |
|:--------------------------------|---------------------------:|----------:|-------------:|
| raw a1 in x=Q^2                 |                3.55837     | -999452   | -1.00141e-06 |
| normalized a1 in z=Q^2/Lambda^2 |                4.13325e-17 |      -1   | -1           |
| normalized a2 in z=Q^2/Lambda^2 |                4.213e-17   |       0.5 |  0.5         |

**Decision:** the previous one-parameter dimensional jet locus is replaced by a quotient-normalized shape fingerprint. \(\varepsilon=\Lambda^{-2}\) is a scale coordinate, not by itself a universal invariant.

## B.7 Experiment 7 — Reconstructibility ladder

Four synthetic kernels were used:
1. \(G=e^{-z}\);
2. \(G_2=e^{-2z}\), quotient-equivalent to \(G\) after a scale-coordinate redefinition;
3. \(SG=e^{-z^2}\);
4. \(P=e^{-z}/(1+z^4)\), matching the Gaussian through cubic jet order but adding finite complex poles.

| kernel             | quotient_class   |   IR_degree | J3                               | extra_pole_class       |
|:-------------------|:-----------------|------------:|:---------------------------------|:-----------------------|
| G: exp(-z)         | Gaussian         |           1 | (-1, 1/2, -1/6)                  | none                   |
| G2: exp(-2z)       | Gaussian         |           1 | same after z'=2z normalization   | none                   |
| SG: exp(-z^2)      | SuperGaussian    |           2 | (0, -1, 0)                       | none                   |
| P: exp(-z)/(1+z^4) | PoleMutant       |           1 | same as Gaussian through order 3 | 4 finite complex poles |

The information ladder gives:

| fingerprint_stage            |   physical_classes_resolved |   target_physical_classes |
|:-----------------------------|----------------------------:|--------------------------:|
| F(0)=1 + Lorentz scalar only |                           1 |                         3 |
| + leading IR degree d        |                           2 |                         3 |
| + normalized jet J^3         |                           2 |                         3 |
| + singular locus Sing        |                           3 |                         3 |

The target is three physical quotient classes because \(G\) and \(G_2\) represent the same Gaussian shape after scale reparameterization.

**Decision:** reconstructibility requires quotient normalization plus degree and singular-locus information. Raw coefficients overcount theory identity.

## B.8 Experiment 8 — Relational invariant falsification of the scalar three-gluon ansatz

The old ansatz

\[
\Gamma_{3,\rm VGM}=F_3\Gamma_{3,0}
\]

was tested against the modified inverse-kinetic contraction condition. \(F_3\) was optimized independently for each synthetic kinematic sample.

|   momentum_scale_over_Lambda |    N |   median_residual |   p95_residual |
|-----------------------------:|-----:|------------------:|---------------:|
|                         0.05 | 5000 |        0.00354222 |      0.0109776 |
|                         0.1  | 5000 |        0.0141605  |      0.0408778 |
|                         0.25 | 5000 |        0.0713333  |      0.192894  |
|                         0.5  | 5000 |        0.180958   |      0.438692  |
|                         1    | 5000 |        0.277586   |      0.667089  |
|                         1.5  | 5000 |        0.325818   |      0.781882  |

**Decision:** FAIL for generic nonzero deformation. The scalar \(F_3\) should be removed from the core theory; the interaction sector must be derived from a gauge-covariant nonlocal action or a richer tensor vertex.

## B.9 Experiment 9 — UV damping as admissibility, not invariant identity

|   K_over_Lambda |   local_proxy |   gaussian_proxy |
|----------------:|--------------:|-----------------:|
|             0.5 |       1.14828 |         0.978131 |
|             1   |       1.81251 |         1.22138  |
|             2   |       2.49823 |         1.24544  |
|             3   |       2.90231 |         1.24546  |
|             5   |       3.41242 |         1.24546  |
|            10   |       4.10527 |         1.24546  |
|            30   |       5.20379 |         1.24546  |
|           100   |       6.40776 |         1.24546  |

**Decision:** PASS as a UV-admissibility property of the Gaussian kernel only. This is not an invariant fingerprint, beta-function calculation, or evidence for a UV fixed point.

## B.10 Revised tested fingerprint

\[
\boxed{
\mathfrak I_{\rm VGM}^{(\rm tested)}
=
\left(
d_{\rm IR},
r_{\rm kin},
\operatorname{Spec}_{\rm norm},
\operatorname{Sing}_D,
\operatorname{Aut}_L,
\Pi_z
\right)
}
\]

with

\[
\Pi_z=\frac{Q^2}{\Lambda^2}.
\]

Not presently established as invariants:
- raw \(\Lambda_{\rm VGM}\);
- \(\varepsilon=\Lambda^{-2}\);
- dimensional Taylor coefficients;
- scalar \(F_3,F_4\);
- a modified beta function;
- a UV fixed point;
- the proposed confinement mechanism.

The gauge component of \(\operatorname{Aut}\) remains unresolved until one nonlocal gauge-covariant action generates the propagator, all gluonic vertices, the ghost sector and the BRST differential consistently.

## B.11 Coefficient-strength classification

**I0 — removable/reparameterization data**
- Gaussian slope \(c\) in \(e^{-cz}\) when absorbed into \(\Lambda\);
- dimensional jet coefficients before quotient normalization;
- removable overall normalization factors.

**I1 — moduli data**
- dimensionless ratios such as \(\Lambda_{\rm VGM}/\Lambda_{\rm ref}\), if independently measurable.

**I2 — discrete/topological data**
- none established in the present kernel-only benchmark.

**I3 — singular/critical identity data**
- change in finite pole/singularity locus;
- change in generic kinetic rank/null-space structure.

## B.12 Current falsification status

| Component | Status |
|---|---|
| unit/scale quotient \(z=Q^2/\Lambda^2\) | PASS |
| Lorentz-scalar dependence | PASS |
| transverse rank/null-space | PASS |
| normalized kinetic spectrum | PASS |
| leading IR degree as discriminant | PASS |
| Gaussian finite-pole audit | PASS |
| normalized Gaussian jet fingerprint | PASS |
| reconstructibility in synthetic kernel atlas | PASS |
| scalar \(F_3\Gamma_3\) completion | FAIL |
| full BRST/Slavnov–Taylor invariance | OPEN |
| loop-level unitarity | OPEN |
| VGM beta function | OPEN |
| confinement mechanism | OPEN |
| collider phenomenology | OPEN |

## B.13 Consequence

The revised VGM is not a list of preserved coefficients. It is a quotient-geometric identity class. At the present level the Gaussian kernel is a candidate representative whose dimensional scale is removed into dimensionless coordinates, while leading deformation degree, transverse rank, normalized spectrum and singular locus form a minimal reconstructible fingerprint.

The next formal benchmark must begin from an explicitly gauge-covariant nonlocal action and derive the propagator, three- and four-gluon vertices, ghost sector and BRST differential from the same generator. Only structures surviving that quotient-level test should remain in the core theory.
