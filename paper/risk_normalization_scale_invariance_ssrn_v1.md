# Risk Normalization Does Not Imply Scale Invariance: Costs, Harmonic Width, and Eligibility in Futures Trading Rules

**Ariel Elboim**  
Independent Researcher, Israel  
Corresponding author: lgboim@gmail.com  
Working Paper, Version 1.0 - September 1, 2026

**Primary empirical sample:** January 2011-December 2023  
**Operational eligibility extension:** through August 26, 2026

## Abstract

Risk normalization standardizes gross payoff geometry, not necessarily the scaling laws of implementation costs or eligibility. We derive the necessary and sufficient cost transformation for invariance conditional on a fixed gross risk-unit path. For a constant per-contract dollar cost component and point value, average normalized drag is governed by harmonic risk width. When drag is lower in a late period, downscaling can lower benchmark net performance in both periods while enlarging their measured contrast. A one-tenth multiplier-only mapping raises the fixed-friction contribution to the late-minus-baseline contrast from 0.0115R to 0.1153R in E-mini Nasdaq-100 futures and from 0.0101R to 0.1015R in E-mini S&P 500 futures. A separate 4–120-point filter changes NQ trade retention from 99.9% to 66.3%. The illustrative 2011–2017 versus 2022–2023 benchmark contrasts are positive but coarse six-month sensitivity ranges include zero. Risk units normalize the gross payoff path; they do not normalize implementation economics.

**Keywords:** risk normalization; transaction costs; futures; eligibility; opening-range breakout; scale equivariance

## Plain Language Summary

Risk units make gross trading outcomes comparable to initial risk, but they do not automatically make implementation economics comparable across contract sizes or market eras. This paper shows that fixed-dollar cost drag depends on inverse risk width, so its correct aggregate is governed by harmonic rather than arithmetic width. It also shows that smaller contract scale can lower normalized net performance in two periods while increasing the measured contrast between them. Fixed point-based eligibility rules create a separate problem by changing which opportunities enter the sample. The results motivate reporting gross payoff, implementation-cost components, inverse-width statistics, and participation separately.

## AI Use Disclosure

OpenAI ChatGPT and Codex supported code development, robustness ideation, adversarial review, literature discovery, and language editing. The author reviewed and verified all outputs and takes full responsibility for the analysis and manuscript.

## 1. Introduction

Trading-rule outcomes are often expressed as multiples of initial risk. This removes currency and price units from gross payoff geometry: a \(1.5R\) target and a \(1R\) stop retain the same meaning across risk widths. Unit-free representation, however, does not imply economic invariance. A trade can be identical in gross \(R\)-space and different in net economic \(R\)-space.

The objects combined in net performance need not share a scaling law. Gross dollar payoff may scale with initial dollar risk while commissions remain fixed in dollars, spreads are denominated in price units, and tick increments change with contract design. For a trade with \(n_i\) contracts, price-unit risk width \(W_i\), dollar point value \(V\), and dollar cost \(\mathcal C_i\), we characterize when normalized cost \(\mathcal C_i/(n_iW_iV)\) remains invariant under changes in contract count, point value, and width: dollar cost must transform with the dollar-risk denominator. Contract scale and setup scale are distinct transformations; the former can hold the realized price path fixed, whereas the latter generally cannot.

Two implications follow. First, with a constant per-contract dollar cost, average normalized drag is governed by harmonic risk width, so narrow-risk observations receive disproportionate economic weight. If drag is lower in a late period, downscaling lowers both period levels but enlarges their measured contrast. Second, cost scaling changes the economics of a fixed trade set, whereas fixed absolute eligibility bounds change the trade set itself. The framework therefore separates gross payoff geometry, implementation economics, and eligibility.

The per-trade identity itself is elementary; the contribution lies in its aggregate and selection implications: component-specific cost scaling, harmonic-width aggregation, level–contrast divergence under downscaling, and a separate equivariance benchmark for absolute eligibility rules. The distinction matters whenever performance reports compare net risk units across contract denominations or eras while summarizing setup width arithmetically or holding point-denominated eligibility bounds fixed.

The framework connects transaction costs and implementation shortfall (Perold, 1988; Bajgrowicz & Scaillet, 2012; Anghel, 2022), research selection (Sullivan et al., 1999; White, 2000; Bailey & López de Prado, 2014), risk scaling (Moreira & Muir, 2017), and opening-range and intraday-continuation evidence (Holmberg et al., 2013; Gao et al., 2018; Tsai et al., 2019; Baltussen et al., 2021).

An opening-range breakout rule in E-mini Nasdaq-100 and E-mini S&P 500 futures serves as the empirical laboratory. The 2011–2017 versus 2022–2023 benchmark net contrast is approximately \(0.11R\) in both markets, but coarse six-month sensitivity ranges include zero; it is an accounting contrast, not an established structural break. Holding every realized trade and gross outcome fixed, a one-tenth multiplier-only mapping raises fixed-friction attribution roughly tenfold while lowering benchmark net performance in both eras. A fixed 4–120-point rule separately changes NQ trade retention from 99.9% to 66.3%.

## 2. Economic objects and invariance conditions

### 2.1 Definitions

For trade \(i\), let \(r_i\) denote gross payoff in units of initial risk; \(n_i\in\mathbb N_+\) contract count; \(W_i>0\) setup width in price units; \(V>0\) dollar point value; and \(\mathcal C_i(n_i,V,W_i)\) total dollar implementation cost. Other realized determinants of implementation cost are suppressed from the notation and held fixed under the transformation. Define normalized friction intensity

\[
\phi_i(n_i,V,W_i)
=
\frac{\mathcal C_i(n_i,V,W_i)}{n_iW_iV},
\]

and net payoff

\[
N_i=r_i-\phi_i(n_i,V,W_i).
\]

The fixed-path results condition on the realized gross risk-unit payoff and opportunity set. They treat implementation cost as an additive accounting layer. Execution effects that alter fills, entry or exit prices, target or stop attainment, or \(r_i\) require a path-dependent execution model and lie outside the fixed-path result.

### 2.2 Equivariance condition and Proposition 1

Define the extended scale transformation

\[
T_{\rho,\lambda,\gamma}(n_i,V,W_i)
=(\rho n_i,\lambda V,\gamma W_i),
\qquad \rho,\lambda,\gamma>0,
\]

for transformations with \(\rho n_i\in\mathbb N_+\). This is an accounting extension; quantity changes may generate execution, impact, fee-tier, or feasibility effects outside the fixed-path result. Write \(T_{\lambda,\gamma}=T_{1,\lambda,\gamma}\) for the fixed-quantity point-value–width comparative static. The empirical multiplier-only counterfactual further specializes to \(T_{1,\lambda,1}\).

**Equivariance condition.** Normalized implementation cost is invariant under \(T_{\rho,\lambda,\gamma}\) if and only if total dollar cost transforms with the dollar-risk denominator:

\[
\phi_i(\rho n_i,\lambda V,\gamma W_i)=\phi_i(n_i,V,W_i)
\]

if and only if

\[
\mathcal C_i(\rho n_i,\lambda V,\gamma W_i)
=
\rho\lambda\gamma\mathcal C_i(n_i,V,W_i).
\]

Derivations of the equivariance condition and Propositions 1–2 are collected in Appendix A.

This equivalence condition organizes the analysis. It permits quantity rescaling through \(\rho\). Proposition 1 focuses on \((V,W)\) conditional on fixed \(n_i\), because that is the comparative static used by the empirical counterfactual; quantity rescaling returns in the risk-targeted-quantity remark below. Holding \(n_i\) fixed, suppose component \(j\) admits the following bi-homogeneous scaling law, with degrees \((a_j,b_j)\):

\[
\mathcal C_{ij}(n_i,\lambda V,\gamma W_i)
=
\lambda^{a_j}\gamma^{b_j}\mathcal C_{ij}(n_i,V,W_i).
\]

**Proposition 1 (normalized transformation law).** The corresponding normalized friction component obeys

\[
\phi_{ij}(n_i,\lambda V,\gamma W_i)
=
\lambda^{a_j-1}\gamma^{b_j-1}\phi_{ij}(n_i,V,W_i).
\]

The component is invariant under all point-value rescalings if and only if \(a_j=1\), under all width rescalings if and only if \(b_j=1\), and under all unrestricted joint rescalings if and only if \(a_j=b_j=1\). For a nonzero component and a particular pair \((\lambda,\gamma)\), invariance requires

\[
\lambda^{a_j-1}\gamma^{b_j-1}=1.
\]

Appendix A gives the equivalent local-elasticity representation for positive differentiable cost components.

Component-wise equivariance is sufficient for total-cost equivariance. At a particular finite transformation, non-equivariant components can also offset accidentally in the aggregate; Proposition 1 classifies structural component scaling laws rather than such pointwise equality.

Point-value invariance and setup-width invariance are the special cases \(\gamma=1\) and \(\lambda=1\). Point-value rescaling can preserve the entire realized price path by construction. Setup-width rescaling generally cannot, because width may define entry, stop, and target. The width result is therefore a conditional comparative static for the cost representation unless the gross path is independently held fixed.

### 2.3 Corollary 1: heterogeneous friction laws

Suppose

\[
\mathcal C_i(n_i,V,W_i)
=
n_iK+n_iVS_i+c\,n_iW_iV,
\]

where \(K\) is a fixed per-contract dollar component, \(S_i\) is a price-unit friction, and \(c\) is proportional to initial dollar risk. Then

\[
N_i
=
r_i
-\frac{K}{W_iV}
-\frac{S_i}{W_i}
-c.
\]

| Friction component | Representation in risk units | Invariant to \(V\)? | Invariant to \(W\)? |
|---|---:|---:|---:|
| Fixed dollars per contract | \(K/(W_iV)\) | No | No |
| Fixed price-unit friction | \(S_i/W_i\) | Yes, holding \(S_i\) fixed | No |
| Fixed number of ticks | \(m\tau/W_i\), for \(m\) ticks of size \(\tau\) | Yes, holding \(\tau\) fixed | No |
| Proportional to dollar risk | \(c\) | Yes | Yes |

A fixed number of ticks is the special case \(S_i=m\tau\). Its invariance requires the tick increment \(\tau\) to remain unchanged. This matters for actual product redesign: the 2026 E-nano S&P 500 and Nasdaq-100 contracts are one-hundredth the E-mini multiplier but use 0.5-point ticks rather than the 0.25-point increments of their Micro and E-mini counterparts (CME Group, 2026). The products provide an economic scale anchor, not a pure realization of \(T_{1,0.01,1}\).

**Remark (risk-targeted quantity).** Under a linear per-contract fee, contract-count rescaling cancels even when point value and width also change:

\[
\frac{\rho n_iK}{(\rho n_i)(\gamma W_i)(\lambda V)}
=
\frac{K}{\lambda\gamma W_iV}.
\]

The fixed-fee result therefore survives ordinary risk-based quantity scaling conditional on execution. Minimum-one-contract feasibility, margin constraints, tiered fees, and nonlinear market impact can still change participation or cost.

### 2.4 Corollary 2: harmonic-width aggregation

A central implication for fixed-dollar costs is the harmonic-width representation.

Let \(K>0\) and \(V>0\) be constant across all trades and both periods being compared, and assume

\[
0<E_t[W_i]<\infty,
\qquad
0<E_t[1/W_i]<\infty.
\]

Define gross mean \(G_t=E_t[r_i]\), fixed-dollar drag

\[
D_t=E_t\left[\frac{K}{W_iV}\right],
\]

and harmonic-mean risk width

\[
H_t=\left(E_t[1/W_i]\right)^{-1}.
\]

For a sample of \(q_t\) trades, its sample analogue is

\[
\widehat H_t
=
\frac{q_t}{\sum_{i=1}^{q_t}1/W_i}.
\]

Then

\[
D_t=\frac{K}{VH_t}.
\]

Because \(w\mapsto1/w\) is strictly convex on \(w>0\), Jensen's inequality also gives

\[
D_t=\frac{K}{V}E_t[1/W_i]
\geq
\frac{K}{V E_t[W_i]},
\]

with equality only when width is constant almost surely. The economically relevant average setup scale for fixed-dollar friction is therefore harmonic rather than arithmetic. Substituting arithmetic mean width systematically understates average fixed-dollar drag except in the degenerate constant-width case. Narrow-risk observations receive disproportionate economic weight even when trades receive equal statistical weight.

### 2.5 Corollary 3: level–contrast divergence under downscaling

For any period quantity \(X_t\), define \(\Delta X=X_1-X_0\), where \(0\) denotes the baseline and \(1\) the late period. Under point-value scaling \(V\mapsto\lambda V\),

\[
\mu_t(\lambda)=G_t-\frac{D_t}{\lambda},
\]

so

\[
\Delta\mu(\lambda)
=
\Delta G-\frac{\Delta D}{\lambda}
=
\Delta G-
\frac{K}{\lambda V}
\left(\frac{1}{H_1}-\frac{1}{H_0}\right).
\]

The comparative statics are

\[
\frac{\partial\mu_t(\lambda)}{\partial\lambda}
=
\frac{D_t}{\lambda^2}>0,
\qquad
\frac{\partial\Delta\mu(\lambda)}{\partial\lambda}
=
\frac{\Delta D}{\lambda^2}.
\]

If \(D_1<D_0\), equivalently \(E_1[1/W_i]<E_0[1/W_i]\) under \(K>0\), then reducing \(\lambda\) lowers \(\mu_0\) and \(\mu_1\) while increasing \(\Delta\mu\). Measured improvement can therefore increase while normalized net performance falls in both comparison periods.

### 2.6 Proposition 2: fixed absolute eligibility bounds are not generally scale equivariant

Let

\[
A_i(W_i;L,U)=\mathbf 1\{L\leq W_i\leq U\}.
\]

Under \(W_i'=\gamma W_i\) with fixed nominal bounds,

\[
A_i(W_i';L,U)
=
A_i(W_i;L/\gamma,U/\gamma).
\]

Jointly scaling the state and bounds restores equivariance:

\[
A_i(\gamma W_i;\gamma L,\gamma U)=A_i(W_i;L,U).
\]

For period CDF \(F_t^W\), define tick-discrete boundary locations

\[
b_{L,t}=F_t^W(L^-),
\qquad
b_{U,t}=F_t^W(U).
\]

Then participation is

\[
p_t(L,U)
=P_t(A_i=1)
=b_{U,t}-b_{L,t}.
\]

The proposition supplies an exact multiplicative-rescaling benchmark. Historical boundary ranks diagnose more general distribution drift without assuming that one period is a scalar multiple of another; they do not establish invariance within the selected interval.

For every member of a stated pre-filter candidate universe, let \(N_i^{\mathrm{cand}}\) denote potential net payoff and define realized filtered payoff \(\widetilde N_i=A_iN_i^{\mathrm{cand}}\). Provided \(P_t(A_i=1)>0\), the participation-quality identity is

\[
E_t[\widetilde N_i]
=
P_t(A_i=1)
E_t[N_i^{\mathrm{cand}}\mid A_i=1].
\]

Eligibility can therefore change participation, conditional gross payoff, and conditional fixed-cost intensity \(E_t[1/W_i\mid A_i=1]\). All expectations are relative to the declared candidate universe; empirically, Section 5 distinguishes trade-candidate and complete-session denominators.

## 3. Data and empirical design

### 3.1 Data and continuous-contract construction

The canonical sample uses Sierra Chart one-minute contract records for NQ and ES from January 2011 through December 2023 (Sierra Chart, 2026). Contract lineage follows the previous completed session's volume leader, while all trading geometry uses raw, unadjusted prices from the selected quarterly contract. Databento supplies the 2024–August 2026 operational extension, with 2023 retained as a vendor-overlap year.

Sessions require all 270 one-minute bars from 09:30 through 13:59 New York time. Baseline coverage is 1,716 of 1,748 scheduled full-window sessions for NQ (98.17%) and 1,717 of 1,748 for ES (98.23%). A calendar audit identified incomplete bars in the legacy pre-2017 Databento segment. Before repaired results were inspected, a uniform protocol was frozen and the full canonical history was rebuilt from Sierra contract-level records. Appendix C documents contract construction, calendar handling, the repair and coverage reconciliation, before-and-after estimates, source inventory, and hashes.

### 3.2 Fixed opening-range rule

The opening range is the high-low interval from 09:30 through 09:59. The rule enters on the first one-sided break from 10:00 onward; a bar opening beyond the relevant boundary enters at its open. The initial-risk distance equals one opening-range width, with stop and target distances measured from the realized entry price. The target is \(+1.5R\), the stop is \(-1R\), and an open position exits at the 13:59 close. Post-entry ambiguous same-bar cases receive stop priority. Appendix E and the frozen replication package specify the complete bar-level conventions, including two-sided pre-entry bars, entry-bar treatment, gap entry, and terminal-bar entry.

The headline universe applies no range filter and subtracts a constant four-dollar round-trip component per contract. Throughout the empirical sections, “net” denotes gross payoff less this stated fixed-dollar benchmark unless an additional penalty is explicitly introduced; it is not an estimate of all-in realized execution cost.

| Design component | Headline specification |
|---|---|
| Opening range | 09:30–09:59 New York time |
| Entry | First one-sided break from 10:00 onward |
| Stop | One opening-range width |
| Target | \(+1.5R\) |
| Time exit | 13:59 close |
| Fixed cost component | \(\$4\) round trip per contract |
| Headline range filter | None |
| Main sample end | December 2023 |

### 3.3 Three empirical universes

The historical comparison uses every signal from a complete session. The fixed-path contract-scale counterfactual uses exactly the same days, entries, exits, widths, and gross outcomes, changing only point value. A separate eligibility analysis applies the inherited 4–120-point filter and therefore uses a different trade universe. The filter was historically inspected and is used only to demonstrate opportunity-set non-invariance, not as a prospectively selected strategy improvement.

The distinction matters numerically. The NQ headline universe contains 490 trades in 2022–2023; the filtered universe contains 325. No filtered-universe result enters the fixed-path accounting result. The bounds were inherited from a prior implementation, but their original selection date and rationale cannot be recovered from the accessible archive; they are not treated as prospectively selected for this study (Appendix C).

### 3.4 Historical contrast and inference status

The headline history was inspected before the later source repair and before the cross-market extension. The repair protocol froze a uniform reconstruction pipeline before repaired results were viewed; it did not constitute independent preregistration or erase earlier researcher degrees of freedom. The named subperiods are therefore presented as documented summary contrasts within a visible historical path.

![Figure 1. Annual gross payoff, fixed-dollar drag, and benchmark net payoff.](assets/figure1_annual_gross_drag_net.svg)

**Figure 1. Annual gross payoff, fixed-dollar drag, and benchmark net payoff.** The figure reports the complete 2011–2023 historical path for each headline market under the four-dollar original-point-value convention. Shaded bands mark the four named reporting periods within the full annual history. Annual trade counts are omitted to avoid mixing quantities with different scales on one axis. The chronology audit separately records when period definitions and endpoint grids entered the research process.

Estimated mean benchmark net payoff is negative in 2011–2017 and positive in each later period in both markets.

**Table 1. Mean benchmark net payoff per trade by period**

| Market | Period | Trades | Mean benchmark net payoff |
|---|---:|---:|---:|
| NQ | 2011–2017 | 1,693 | -0.044R |
| NQ | 2018–2019 | 488 | +0.011R |
| NQ | 2020–2021 | 492 | +0.053R |
| NQ | 2022–2023 | 490 | +0.071R |
| ES | 2011–2017 | 1,703 | -0.066R |
| ES | 2018–2019 | 492 | +0.039R |
| ES | 2020–2021 | 496 | +0.044R |
| ES | 2022–2023 | 495 | +0.044R |

The 2022–2023 late-minus-baseline contrasts are \(+0.1153R\) for NQ and \(+0.1101R\) for ES. Calendar-aligned six-month sensitivity ranges include zero in both markets—\([-0.017R,+0.247R]\) for NQ and \([-0.030R,+0.250R]\) for ES—and classification varies with block phase (Appendix B). A separately frozen retrospective NQ grid enumerates every ordered pairing of a seven-consecutive-year baseline and a later nonoverlapping two-consecutive-year window available from complete calendar years 2011–2025. It uses the canonical Sierra history through 2023 and the separately labeled Databento operational extension for 2024–2025; it is an endpoint-selection audit and does not extend the primary performance sample. The headline ranks 12th of 28 such transitions and third of seven comparisons holding the 2011–2017 baseline fixed; it is not the locally maximal endpoint. This endpoint enumeration was conducted for NQ only, and no corresponding ES rank is claimed. We therefore use the historical difference as an accounting contrast rather than evidence of a structural break.

## 4. Fixed-path contract-scale dependence

### 4.1 Empirical harmonic-width mechanism

NQ harmonic width rises 6.3-fold, from 14.60 points in 2011–2017 to 92.07 in 2022–2023, reducing fixed-dollar drag from \(0.01370R\) to \(0.00217R\). In ES, harmonic width rises 3.2-fold, from 5.43 to 17.43 points, and drag falls from \(0.01474R\) to \(0.00459R\). Values are computed from unrounded estimates. The mechanism is distributional rather than a generic rise in “volatility”: fixed-dollar drag is governed by inverse width, and downscaling magnifies its inter-period difference even as both benchmark net levels fall.

### 4.2 Accounting decomposition

Each trade ends at target, stop, or time exit. For period \(t\) and outcome \(k\), let \(p_{tk}\) be the category frequency and \(m_{tk}\) the conditional gross payoff. The reported decomposition has \(p_{tk}>0\) for every category in both periods. If a category is empty, its conditional mean is undefined and the category-level decomposition requires a pre-specified pooling or reporting convention rather than an arbitrary zero assignment. Mean gross payoff is

\[
G_t=\sum_k p_{tk}m_{tk}.
\]

For baseline \(0\) and late period \(1\), define the symmetric gross-frequency and gross-conditional-payoff components

\[
\Delta G_{\mathrm{freq}}
=
\frac12\sum_k(p_{1k}-p_{0k})(m_{0k}+m_{1k}),
\]

\[
\Delta G_{\mathrm{pay}}
=
\frac12\sum_k(m_{1k}-m_{0k})(p_{0k}+p_{1k}).
\]

For scale \(\lambda\), define the fixed-friction contribution

\[
J(\lambda)
=
\frac{D_0-D_1}{\lambda}
=
-\frac{\Delta D}{\lambda}.
\]

Then

\[
\Delta\mu(\lambda)
=
\Delta G_{\mathrm{freq}}
+
\Delta G_{\mathrm{pay}}
+
J(\lambda)
.
\]

The symmetric replacement is the two-factor Shapley decomposition: it averages the two possible frequency-payoff replacement orders (Shorrocks, 2013). It is an accounting identity rather than causal attribution. The two gross components are invariant to \(\lambda\) in the fixed-path experiment; \(J(\lambda)\) alone changes with the multiplier-only mapping.

Under the frozen exact-fill conventions of Section 3.2 and Appendix E, target and stop payoffs are fixed by design at \(+1.5R\) and \(-1R\), respectively. Inter-period variation in the gross conditional-payoff component therefore arises from the time-exit category.

A calendar-month reweighting audit was specified after the point estimates were inspected, then frozen before the audit was run. It is reported descriptively in the replication package and is not used for inferential classification.

### 4.3 Multiplier-only counterfactual

The counterfactual changes NQ point value from \(\$20\) to \(\$2\) and ES point value from \(\$50\) to \(\$5\). It changes no realized price path, opportunity, width, or gross \(R\) outcome. The four-dollar component remains fixed. The values correspond to \(\lambda=0.1\), matching the E-mini-to-Micro multiplier ratio (CME Group, 2019) while deliberately abstracting from actual Micro fee schedules, spreads, liquidity, depth, and execution.

**Table 2. Fixed-path decomposition of the 2022–2023 contrast relative to 2011–2017**

| Market | Mapping | Baseline benchmark net | Late benchmark net | \(\Delta\) benchmark net | Gross frequency | Gross conditional payoff | Fixed friction \(J(\lambda)\) |
|---|---|---:|---:|---:|---:|---:|---:|
| NQ | Original point value | -0.044R | +0.071R | +0.1153R | +0.0676R | +0.0361R | +0.0115R |
| NQ | Multiplier-only \(\lambda=0.1\) | -0.167R | +0.052R | +0.2190R | +0.0676R | +0.0361R | +0.1153R |
| ES | Original point value | -0.066R | +0.044R | +0.1101R | +0.0520R | +0.0480R | +0.0101R |
| ES | Multiplier-only \(\lambda=0.1\) | -0.198R | +0.003R | +0.2015R | +0.0520R | +0.0480R | +0.1015R |

*Notes:* Components and benchmark net levels are rounded independently; displayed sums may differ from \(\Delta\) benchmark net by \(0.0001R\). The tenfold fixed-friction relation holds before rounding.

Downscaling leaves both gross components unchanged and magnifies only \(J(\lambda)\), raising the fixed-friction contribution tenfold. Benchmark net performance falls in both eras even as the measured late-minus-baseline contrast rises.

The downscaled late-period ES level is only \(+0.003R\) before any additional execution penalty. It is therefore an accounting value near zero, not evidence of economically robust profitability at smaller contract scale.

Increasing contract count to maintain a target dollar-risk exposure does not remove this result. Under a linear per-contract fee, \(n_i\) cancels from normalized fixed friction, as shown in Section 2.3.

![Figure 2. Contract-scale downscaling frontier.](assets/figure2_downscaling_frontier.svg)

**Figure 2. Contract-scale downscaling frontier.** Baseline benchmark net payoff, late-period benchmark net payoff, and the late-minus-baseline contrast are shown over the economically anchored range \(0.01\leq\lambda\leq1\). The analytical result applies for every \(\lambda>0\). Markers at \(0.1\) and \(0.01\) are multiplier-scale accounting anchors, not Micro or E-nano execution claims.

### 4.4 Fee-scale sensitivity

The four-dollar convention is a benchmark, not a calibrated optimum. For any positive fixed fee \(K'\), the fixed-friction contribution is

\[
J(K',\lambda)
=
\frac{K'}{\lambda V}
\left(E_0[1/W]-E_1[1/W]\right).
\]

Fee and multiplier sensitivity enter only through the effective fixed-fee parameter \(K'/\lambda\); no trade path must be rerun. Exact preservation of original fixed-fee drag requires \(K_s=\lambda K\). Relative to the four-dollar anchor, the invariance thresholds are \(\$0.40\) at \(\lambda=0.1\) and \(\$0.04\) at \(\lambda=0.01\). These are transformation benchmarks, not fee quotes; a dated all-in schedule is required to label a named-contract execution point. The replication package reports the analytical grid.

## 5. Absolute eligibility and the opportunity set

The fixed 4–120-point filter illustrates a separate non-invariance. Two denominators are used for distinct questions. Historical trade retention is

\[
p_t^{\mathrm{trade}}
=
P_t(A=1\mid\text{unfiltered trade candidate}),
\]

whereas the operational state-space diagnostic is

\[
p_t^{\mathrm{session}}
=
P_t(A=1\mid\text{complete session}).
\]

In the NQ historical trade universe, the filter excludes two of 1,693 baseline trade candidates but 165 of 490 candidates in 2022–2023. The baseline exclusions comprise one width below four points and one above 120; all 165 late-period exclusions are above 120. Thus \(p_t^{\mathrm{trade}}\) falls from 99.9% to 66.3%. In the complete-session width distributions used for the CDF diagnostic, the lower and upper boundary locations are 0.1% and 99.9% in 2011–2017 versus 0.0% and 65.7% in 2022–2023. Numerical constancy of the bounds does not preserve their percentile ranks or the conditional distribution inside the interval.

The frozen operational extension ends on August 26, 2026. In matched January 1–August 26 windows, NQ session eligibility falls from 87.7% in 2023 to 80.4%, 44.7%, and 12.9% in 2024–2026. Every rejection is above 120 points; with matched calendar windows, the deterioration is entirely an upper-bound phenomenon rather than a lower-bound or unequal-window artifact. These session-level rates are not directly comparable to historical trade retention. The 2023 Sierra–Databento overlap produces identical opening-range widths and classifications on all common complete sessions, providing no evidence of a vendor-splice discontinuity in the overlap year.

A distributional shift that lowers \(E[1/W]\) reduces fixed-dollar drag in \(R\), while a fixed upper bound can exclude more candidates. Cost scaling changes the economics of a fixed trade set; absolute eligibility bounds change the trade set itself.

![Figure 3. Eligibility distributions and participation-quality decomposition.](assets/figure3_eligibility_decomposition.svg)

**Figure 3. Eligibility distributions and participation-quality decomposition.** Panel A shows complete-session width CDFs and boundary locations. Panel B reports historical trade-candidate retention, conditional benchmark net payoff, unconditional benchmark net payoff per declared candidate, and conditional harmonic width. Panel C keeps the operational complete-session denominator separate and uses matched January 1–August 26 windows. Panel D reports the exact lower- and upper-bound rejection counts: one and one in 2011–2017, versus zero and 165 in 2022–2023.

## 6. Execution boundary

The fixed-path analysis is an accounting experiment rather than an execution backtest. An additive P&L penalty equivalent to four adverse ticks at entry and four at exit—eight ticks round trip, in addition to the four-dollar component—is applied ex post without changing the realized target, stop, or time-exit category. With \(\tau=0.25\), the price-unit penalty is \(8\tau/W_i=2/W_i\) in risk units. It is therefore invariant to the multiplier-only mapping when tick size is held fixed, whereas the fixed-dollar component scales as \(\lambda^{-1}\). Under this convention, late-period penalized net payoff is \(+0.049R\) at original scale and \(+0.030R\) after downscaling in NQ, versus \(-0.070R\) and \(-0.112R\) in ES. The penalty also stresses the optimistic threshold-fill convention in Appendix E, but it is not a calibrated estimate of gap-through slippage.

Actual contract redesign can also change tick size, fees, depth, liquidity, and integer sizing. The E-nano contracts make the distinction concrete: their multiplier is one-hundredth of the E-mini multiplier, but their 0.5-point tick is twice the 0.25-point E-mini and Micro increment, so they are not a pure realization of \(T_{1,0.01,1}\) (CME Group, 2026). Bollen et al. (2003) document that the 1997 S&P 500 futures redesign, which halved denomination and doubled tick size, increased bid-ask spreads and reduced volume. Karagozoglu and Martell (1999) likewise show that changing futures contract size can induce endogenous volume and liquidity responses. More recently, Nordén et al. (2026) model and estimate the joint trading-cost effects of tick- and lot-size restrictions. Those studies examine endogenous execution and liquidity consequences; the present fixed-path exercise instead holds execution state and the realized gross path fixed to isolate transformation of the normalized accounting estimand.

## 7. Reporting implications and discussion

### 7.1 Reporting implications

The framework implies a compact reporting standard. First, report mean gross payoff \(G_t\) separately from implementation-cost components. Second, when a constant fixed-dollar component is material, report its normalized drag \(D_t\) and \(E_t[1/W]\), or the corresponding harmonic width, alongside ordinary width summaries. Third, report eligibility participation, conditional payoff, and conditional inverse-width intensity over an explicitly declared candidate universe.

Eligibility normalization should follow the economic question. If distribution-relative comparability is intended, pre-specified lagged rolling percentile bounds or other ex-ante relative-width rules target a distribution-relative notion of setup scale more directly than fixed point bounds. The lookback window and updating rule must use only information available before the candidate is classified. If absolute bounds are justified by tick mechanics, capacity, or another absolute economic constraint, they should not be replaced mechanically; instead, their boundary percentile ranks and participation effects should be reported. Proposition 2 supplies the equivariance benchmark, not a universal prescription for relative thresholds.

### 7.2 Interpretation and literature

The fixed-path design isolates an exact conditional accounting effect by changing only point value; it does not model actual Micro or E-nano execution. Setup-width transformations are different because width enters the signal and payoff rule. The observed historical contrast illustrates magnitude but is not a structural claim: its coarse ranges include zero and its classification is phase-sensitive. The frozen retrospective NQ endpoint grid also shows that 2022–2023 is not the locally maximal equal-geometry endpoint.

Frozen signal-path and cross-market extensions are mixed and are reported in Appendix D; they limit trading-performance claims but do not affect the transformation results.

Market microstructure invariance instead posits equilibrium and empirical scaling relations linking trading costs to bet activity and volatility across assets (Kyle & Obizhaeva, 2016). Hou et al. (2024) estimate those relations in futures using client-trading volume and the trade-related component of volatility. That literature studies cross-asset regularities in trading costs; the present object is the accounting equivariance of a risk-normalized trading-rule estimand conditional on a fixed gross path.

The work also relates to implementation costs and selection (Perold, 1988; Sullivan et al., 1999; White, 2000; Bajgrowicz & Scaillet, 2012; Bailey & López de Prado, 2014; Anghel, 2022), risk scaling (Moreira & Muir, 2017; Lundström, 2018; Lundström & Peltomäki, 2018), risk-unit reporting (Tharp, n.d.; Carver, 2023; Viaggi, 2026), and opening-range and intraday-continuation evidence (Holmberg et al., 2013; Gao et al., 2018; Tsai et al., 2019; Baltussen et al., 2021). We are not aware of a unified treatment of risk-normalized trading-rule evaluation that links component-specific cost equivariance, harmonic-width aggregation, level–contrast divergence, and absolute-rule eligibility scaling.

## 8. Conclusion

A dimensionless trading statistic is not necessarily a scale-invariant economic estimand. Conditional on a fixed gross path, normalized implementation cost remains invariant only when dollar cost transforms with the dollar-risk denominator. Fixed-dollar costs do not generally satisfy that condition and fail it under the point-value downscaling studied here. Under a constant fixed-dollar component, average normalized drag is governed by harmonic risk width.

The empirical application shows why the distinction matters. Under the stated fixed-cost convention, downscaling lowers benchmark net performance in both comparison periods while enlarging the measured historical contrast and raising the fixed-friction contribution tenfold. The downscaled late-period ES level is only \(+0.003R\), an accounting value near zero rather than evidence of robust profitability. Absolute bounds separately alter participation and the selected opportunity set.

Risk units normalize the gross payoff path. They do not normalize implementation economics.

## Data and code availability

The primary source data are commercially licensed through the Sierra Chart Historical Data Service and cannot be redistributed. The operational extension uses separately licensed Databento data. The companion replication archive contains versioned analysis code, sanitized source manifests, derived audit tables, frozen protocols, the repair audit, and a hash-linked replication manifest. It is available at https://doi.org/10.5281/zenodo.22230814. Reproducing the raw-data pipeline requires independent access to the licensed sources.

## Declaration of generative AI and AI-assisted technologies

AI-assisted tools, including OpenAI ChatGPT and Codex, supported code development, robustness ideation, adversarial review, literature discovery, and language editing. The author selected the questions, approved the analysis protocols, verified cited claims and reported results, reviewed and edited all outputs, and takes full responsibility for the analysis and manuscript. Numerical results were generated by versioned scripts and reconciled against the canonical result manifest.


## References

Anghel, D. G. (2022). No pain, no gain: You should always incorporate trading costs for a bias-free evaluation of trading rule overperformance. *Economics Letters, 216*, 110584. https://doi.org/10.1016/j.econlet.2022.110584

Bailey, D. H., & López de Prado, M. (2014). The deflated Sharpe ratio: Correcting for selection bias, backtest overfitting, and non-normality. *Journal of Portfolio Management, 40*(5), 94–107. https://doi.org/10.3905/jpm.2014.40.5.094

Bajgrowicz, P., & Scaillet, O. (2012). Technical trading revisited: False discoveries, persistence tests, and transaction costs. *Journal of Financial Economics, 106*(3), 473–491. https://doi.org/10.1016/j.jfineco.2012.06.001

Baltussen, G., Da, Z., Lammers, S., & Martens, M. (2021). Hedging demand and market intraday momentum. *Journal of Financial Economics, 142*(1), 377–403. https://doi.org/10.1016/j.jfineco.2021.04.029

Benjamini, Y., & Hochberg, Y. (1995). Controlling the false discovery rate: A practical and powerful approach to multiple testing. *Journal of the Royal Statistical Society: Series B, 57*(1), 289–300. https://doi.org/10.1111/j.2517-6161.1995.tb02031.x

Bollen, N. P. B., Smith, T., & Whaley, R. E. (2003). Optimal contract design: For whom? *Journal of Futures Markets, 23*(8), 719–750. https://doi.org/10.1002/fut.10086

Carver, R. (2023). *Advanced futures trading strategies*. Harriman House.

CME Group. (2019, May 6). *CME Group announces launch of new Micro E-mini equity index futures*. https://www.cmegroup.com/media-room/press-releases/2019/5/06/cme_group_announceslaunchofnewmicroe-miniequityindexfutures.html

CME Group. (2026). *Frequently asked questions: E-nano equity index futures*. https://www.cmegroup.com/articles/faqs/faq-e-nano-equity-index-futures.html

Databento. (2026). *CME Globex MDP2 data has incomplete bars for many days*. Databento Issues. https://issues.databento.com/roadmap/cme-globex-mdp2-data-has-incomplete-bars-for-many-days

Gao, L., Han, Y., Li, S. Z., & Zhou, G. (2018). Market intraday momentum. *Journal of Financial Economics, 129*(2), 394–414. https://doi.org/10.1016/j.jfineco.2018.05.009

Holmberg, U., Lönnbark, C., & Lundström, C. (2013). Assessing the profitability of intraday opening range breakout strategies. *Finance Research Letters, 10*(1), 27–33. https://doi.org/10.1016/j.frl.2012.09.001

Hou, A. J., Nordén, L. L., & Xu, C. (2024). Futures trading costs and market microstructure invariance: Identifying bet activity. *Journal of Futures Markets, 44*(6), 901–922. https://doi.org/10.1002/fut.22496

Ibragimov, R., & Müller, U. K. (2010). t-statistic based correlation and heterogeneity robust inference. *Journal of Business & Economic Statistics, 28*(4), 453–468. https://doi.org/10.1198/jbes.2009.08046

Karagozoglu, A. K., & Martell, T. F. (1999). Changing the size of a futures contract: Liquidity and microstructure effects. *Financial Review, 34*(4), 75–94. https://doi.org/10.1111/j.1540-6288.1999.tb00470.x

Kyle, A. S., & Obizhaeva, A. A. (2016). Market microstructure invariance: Empirical hypotheses. *Econometrica, 84*(4), 1345–1404. https://doi.org/10.3982/ECTA10486

Lundström, C. (2018). Optimal leverage in day trading. *Journal of Trading, 13*(2), 57–68. https://doi.org/10.3905/jot.2018.13.2.057

Lundström, C., & Peltomäki, J. (2018). Optimal embedded leverage. *Quantitative Finance, 18*(7), 1077–1085. https://doi.org/10.1080/14697688.2017.1408959

Moreira, A., & Muir, T. (2017). Volatility-managed portfolios. *Journal of Finance, 72*(4), 1611–1644. https://doi.org/10.1111/jofi.12513

Nordén, L. L., Qu, C., & Xu, C. (2026). Tick size, lot size, and liquidity in futures trading. *Journal of Futures Markets, 46*(1), 43–55. https://doi.org/10.1002/fut.70044

Perold, A. F. (1988). The implementation shortfall: Paper versus reality. *Journal of Portfolio Management, 14*(3), 4–9. https://doi.org/10.3905/jpm.1988.409150

Shorrocks, A. F. (2013). Decomposition procedures for distributional analysis: A unified framework based on the Shapley value. *The Journal of Economic Inequality, 11*(1), 99–126. https://doi.org/10.1007/s10888-011-9214-z

Sierra Chart. (2026). *Sierra Chart Historical Data Service*. https://www.sierrachart.com/index.php?page=doc/SierraChartHistoricalData.php

Sullivan, R., Timmermann, A., & White, H. (1999). Data-snooping, technical trading rule performance, and the bootstrap. *Journal of Finance, 54*(5), 1647–1691. https://doi.org/10.1111/0022-1082.00163

Tharp, V. K. (n.d.). A short lesson on R and R-multiples. Van Tharp Institute. https://vantharp.com/wp-content/uploads/2018/06/A_Short_Lesson_on_R_and_R-multiple.pdf

Tsai, Y.-C., Wu, M.-E., Syu, J.-H., Lei, C.-L., Wu, C.-S., Ho, J.-M., & Wang, C.-J. (2019). Assessing the profitability of timely opening range breakout on index futures markets. *IEEE Access, 7*, 32061–32071. https://doi.org/10.1109/ACCESS.2019.2899177

Viaggi, S. (2026). A standardized R-multiple framework for the statistical validation of trading edge in retail trading systems. SSRN working paper. https://doi.org/10.2139/ssrn.6653758

White, H. (2000). A reality check for data snooping. *Econometrica, 68*(5), 1097–1126. https://doi.org/10.1111/1468-0262.00152

## Appendix A. Proofs

### A.1 Derivation of the equivariance condition

Under \(T_{\rho,\lambda,\gamma}\), normalized implementation cost is

\[
\phi_i(\rho n_i,\lambda V,\gamma W_i)
=
\frac{\mathcal C_i(\rho n_i,\lambda V,\gamma W_i)}
{\rho\lambda\gamma n_iW_iV}.
\]

Equality with \(\phi_i(n_i,V,W_i)\) therefore holds if and only if

\[
\mathcal C_i(\rho n_i,\lambda V,\gamma W_i)
=
\rho\lambda\gamma\mathcal C_i(n_i,V,W_i).
\]

### A.2 Proof of Proposition 1

For a component admitting the stated bi-homogeneous scaling law,

\[
\phi_{ij}(n_i,\lambda V,\gamma W_i)
=
\frac{\lambda^{a_j}\gamma^{b_j}\mathcal C_{ij}(n_i,V,W_i)}
{\lambda\gamma n_iW_iV}
=
\lambda^{a_j-1}\gamma^{b_j-1}\phi_{ij}(n_i,V,W_i).
\]

The conditions for invariance under all point-value, width, or unrestricted joint rescalings follow by requiring the corresponding exponent or exponents to equal zero. For a nonzero component and a specified pair, the necessary and sufficient condition is \(\lambda^{a_j-1}\gamma^{b_j-1}=1\).

For strictly positive differentiable components, define

\[
\varepsilon_{V,j}=\frac{\partial\log\mathcal C_{ij}}{\partial\log V},
\qquad
\varepsilon_{W,j}=\frac{\partial\log\mathcal C_{ij}}{\partial\log W}.
\]

For the local elasticity statement,

\[
\log\phi_{ij}
=
\log\mathcal C_{ij}-\log n_i-\log W_i-\log V.
\]

Differentiation with respect to \(\log V\) and \(\log W_i\), holding the other realized determinants fixed, gives \(\partial\log\phi_{ij}/\partial\log V=\varepsilon_{V,j}-1\) and \(\partial\log\phi_{ij}/\partial\log W=\varepsilon_{W,j}-1\).

### A.3 Proof of Proposition 2

For \(\gamma>0\),

\[
A(\gamma W;L,U)
=
\mathbf 1\{L\leq\gamma W\leq U\}
=
\mathbf 1\{L/\gamma\leq W\leq U/\gamma\}
=
A(W;L/\gamma,U/\gamma).
\]

Thus fixed numerical bounds do not generally preserve the classification mapping. Jointly rescaling the bounds restores equivariance because

\[
A(\gamma W;\gamma L,\gamma U)=A(W;L,U).
\]

## Appendix B. Coarse six-month dependence sensitivity

Let \(S_{eg}\) be the sum of benchmark net trade payoffs and \(n_{eg}\) the trade count in six-month block \(g\) of era \(e\), with \(B_e\) blocks. The headline estimator remains trade weighted:

\[
\widehat\mu_e
=
\frac{\sum_{g=1}^{B_e}S_{eg}}
{\sum_{g=1}^{B_e}n_{eg}}.
\]

Define the block residual total

\[
u_{eg}=S_{eg}-n_{eg}\widehat\mu_e
\]

and the finite-block sandwich dispersion

\[
\widehat V_e
=
\frac{B_e}{B_e-1}
\frac{\sum_{g=1}^{B_e}u_{eg}^2}
{\left(\sum_{g=1}^{B_e}n_{eg}\right)^2}.
\]

Treating the separated baseline and late eras as independent for this coarse calculation, the reference statistic is

\[
t_{\mathrm{ref}}
=
\frac{\widehat\mu_1-\widehat\mu_0}
{\sqrt{\widehat V_1+\widehat V_0}}.
\]

The displayed range uses three reference degrees of freedom:

\[
\min(B_0,B_1)-1=3.
\]

This degrees-of-freedom rule is a sensitivity convention, not a theorem for the serially partitioned design. The width generated by the nominal 95% \(t_3\) reference rule is not asserted to have frequentist coverage under unknown dependence and is not presented as a direct application of Ibragimov and Müller (2010).

**Table B1. Coarse six-month dependence sensitivity**

| Market | Estimate | Nominal 95% \(t_3\)-reference range | Late blocks |
|---|---:|---:|---:|
| NQ | +0.1153R | [-0.017R, +0.247R] | 4 |
| ES | +0.1101R | [-0.030R, +0.250R] | 4 |

Both calendar-aligned ranges include zero. A post-hoc audit shifts the six-month partition by zero through five months while retaining all observations. The range crosses zero in four of six phases for NQ and five of six for ES. Nonzero phases create shorter edge blocks and five late-period blocks rather than four; the point estimate remains fixed while classification changes.

A post-hoc shorter-horizon circular moving-block sensitivity produces narrower ranges that exclude zero: \([+0.026R,+0.205R]\) for NQ and \([+0.007R,+0.213R]\) for ES. Because classification depends on a post-hoc dependence-horizon choice, the procedure is not used for structural classification; the discrepancy instead shows that classification depends on the assumed dependence scale. Its full specification and results are retained in the replication package.

## Appendix C. Data provenance and repair audit

The original research build used a Databento-derived OHLCV segment in the pre-2017 history. After the complete-window defect was diagnosed, the canonical January 2011–December 2023 history was reconstructed from Sierra Chart contract-level records under a protocol frozen before repaired outcomes were inspected. Raw, unadjusted quarterly-contract prices determine opening-range width, entries, stops, targets, and gross payoff; the continuous chain determines contract lineage only.

Continuous lineage uses the previous available completed session's total-volume leader. A CME trade-date bucket runs from 18:00 on the preceding New York calendar date through 17:59 on the labeled date and includes every source record in that interval. The universe is the inventoried quarterly outright files, with no separate near-expiry exclusion; equal-volume ties are resolved by contract symbol. The manifest records `price_adjustment: none`. Session timestamps and daylight-saving transitions use `America/New_York`. The scheduled denominator excludes early closes incapable of containing all 270 bars from 09:30 through 13:59.

Databento (2026) documents incomplete OHLCV bars in older CME Globex historical data before May 21, 2017. Our calendar audit found 439 NQ and 440 ES scheduled sessions in the legacy baseline segment that failed the complete-window requirement, consistent with the documented issue. The replication materials preserve a September 1, 2026 snapshot of the dynamic issue record with SHA-256 `a61af573f549dd6e889ce5742638d080dfbcd59dc79c4a4d718272526bc43548`.

The 2011–2017 baseline calendar contains 1,748 scheduled full-window sessions in each headline market. NQ has 3 absent sessions, 29 observed but incomplete sessions, 1,716 complete sessions, and 1,693 generated trades. ES has 4 absent sessions, 27 incomplete sessions, 1,717 complete sessions, and 1,703 generated trades. Across the full 2011–2023 history, the independent calendar contains 3,245 scheduled full-window sessions in each market. The canonical data contain 3,209 complete NQ sessions (98.89%) and 3,210 complete ES sessions (98.92%). The replication materials include the date-level reconciliation and all absent or incomplete scheduled dates.

The source inventory contains all 186 expected non-empty contract files: 53 each for NQ, ES, and YM and 27 for RTY. Approximately 18.96 million source records were validated. Of these, 797 were out of timestamp order and were sorted before continuous-chain construction; no record had invalid price or volume fields. The final continuous NQ and ES files each contain zero duplicate minute timestamps. Exact within-file duplicate minute timestamps were not separately counted inside each raw contract file in the frozen manifest; timestamp overlap across different quarterly contracts is expected and is not a duplication defect. The within-file source count is therefore not reported and is not inferred from the continuous artifacts.

The 4–120-point eligibility bounds were inherited from a prior implementation. The earliest preserved accessible protocol stating the exact bounds is dated August 30, 2026 and prohibits parameter search or model change, but this recent record does not establish when the implementation was originally locked or when 4 and 120 were first selected. The manuscript therefore treats the bounds only as a historically inspected absolute-rule example, not as an ex-ante rule validated by the accessible archive. The replication materials contain the dedicated provenance audit.

The repair increased baseline NQ trades from 1,287 to 1,693 and ES trades from 1,296 to 1,703. Baseline benchmark net expectancy changed from \(-0.049R\) to \(-0.044R\) in NQ and from \(-0.058R\) to \(-0.066R\) in ES. The 2022–2023 late-minus-baseline contrast changed from \(+0.1205R\) to \(+0.1153R\) in NQ and from \(+0.1022R\) to \(+0.1101R\) in ES.

For 2018–2023, the reconstructed and legacy sources generate the same 1,470 NQ and 1,483 ES signal dates and agree on every outcome category. Gross \(R\) differs on 20 NQ dates: the median and maximum absolute differences conditional on disagreement are \(0.00704R\) and \(0.02062R\), and the aggregate mean shift across all common trades is \(-0.000016R\). For ES, gross \(R\) differs on 11 dates: the corresponding values are \(0.03125R\), \(0.04762R\), and \(-0.000067R\). Opening-range width differs on four NQ dates, with median and maximum absolute differences of 0.5 and 1.0 points, and on one ES date by 0.5 points.

For the operational eligibility extension, full-year or available-year NQ session pass rates are 88.7% in 2023, 72.7% in 2024, 47.0% in 2025, and 12.9% through August 26, 2026. The matched-window rates reported in Figure 3 use January 1–August 26 in every year. The Sierra–Databento overlap identifies the same 248 complete 2023 sessions, with zero opening-range-width or classification differences.

The frozen reconstruction protocol has SHA-256

```text
dd1e6bd545dedd5ca45663cf46c5bb86633d53672533ce11a27c19e9c698aa2a
```

The public source manifest has SHA-256

```text
4416fb67c27e021590bae4175f39da7bdb28979c9d3231d302181e5b705db893
```

The canonical continuous-source artifact hashes are

```text
NQ  6567af5416544f9b6cfe728823149b05fe0737dd746fec91868268ff87e2432a
ES  a054658ea943b673d70dc20d6c8b9d997b1afbde52e58f35410bc7bc7ccfdb20
YM  ea2b082566311dfd24ed926ace2315e9bb65f91a8da5e2689eab102a800a83b4
RTY c91c89a033086051b5228ab77be5336851fc32b39bd789dc1fd9110bbf9f27c1
```

Figures 1–3, including values reported only in figure panels, are generated in one run from the canonical lineage artifacts. The figure-generation script has SHA-256

```text
edaf8c04368a5d7b18574002be3d89e981b0f92fa391a59101d6f8ed1f6a3530
```

## Appendix D. Signal and cross-market scope audits

A separately frozen audit evaluates signed returns and excursions after breakout entry without targets, stops, costs, sizing, or range eligibility. Signed return to the close improves by \(+0.1284R\) in NQ and \(+0.1279R\) in ES, but none of 30 market-by-horizon-by-path contrasts survives Benjamini–Hochberg adjustment (Benjamini & Hochberg, 1995). The point estimates are consistent with stronger continuation or weaker reversal, not proof that breakout direction became more informative.

A separately frozen YM/RTY extension required a positive change of at least \(+0.08R\) in both markets and at least 100 trades per headline period. YM changes by \(+0.0732R\) and RTY by \(+0.0059R\), so the joint magnitude criterion fails. RTY's formal count-rule pass relies on a baseline covering only July–December 2017 and is weakly comparable to the seven-year headline baseline. The replication package supplies the full path diagnostics and frozen protocols.

## Appendix E. Bar-level trading-rule conventions

The following conventions define the deterministic one-minute implementation used for every reported trade:

1. **Opening range.** The range is the highest high and lowest low from 09:30 through 09:59 New York time.
2. **Breakout search.** Beginning with the 10:00 bar, the algorithm searches chronologically for the first one-sided break of either range boundary. If no qualifying break occurs by 13:59, no trade is recorded.
3. **Two-sided bars.** A bar whose high and low cross both boundaries is skipped, and the search continues. This is a uniform ambiguity convention: the within-minute crossing order is generally unidentified, and the same rule is retained even when a gap-open reveals which boundary was already crossed at the open.
4. **Entry price.** For the first remaining one-sided break, a bar opening beyond the relevant boundary enters at its open. Otherwise, entry occurs exactly at the crossed boundary.
5. **Risk geometry.** Initial risk is one opening-range width. Stop and target distances are measured from the realized entry price, including after a gap entry. The stop is \(-1R\) and the target is \(+1.5R\). Stops and targets fill at their stated thresholds upon touch; no gap-through price adjustment is applied.
6. **Entry-bar adjudication.** A stop touched on the entry bar is charged. A target touched on the entry bar is not credited.
7. **Later same-bar ambiguity.** On any later bar that touches both stop and target, the stop receives priority.
8. **Terminal-bar entry.** A first qualifying break on the 13:59 bar is executable. Unless the entry-bar stop is touched, the position exits at that bar's close; no entry-bar target is credited.
9. **Time exit.** Any position still open at 13:59 exits at that bar's close.

These conventions define the realized target, stop, and time-exit categories held fixed in the accounting counterfactual. The replication package contains the matching executable protocol.
