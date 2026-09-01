# Provenance audit for the 4–120-point eligibility rule

The 4–120-point bounds were inherited from a prior implementation. The accessible archive does not establish when the implementation was originally locked, when the bounds were first selected, or whether every statistic later used in the manuscript was still unseen at that time.

The earliest preserved protocol in the accessible workspace that states the exact rule is `payoff_path_decomposition_preregister.json`, whose filesystem record is dated August 30, 2026 at 16:13:22 Asia/Jerusalem. It defines the simple opening-range universe as complete sessions with opening-range width constrained to 4–120 points and prohibits parameter search or model change.

Later preserved protocols on the same date explicitly call 4–120 the fixed or locked band and compare it with alternative caps only as non-actionable diagnostics. In particular, `full_core_band_preregister.json` labels `locked_4_120` as the reference policy and forbids promotion regardless of the diagnostic result.

These files establish only that the exact bounds were written into a locked-rule protocol before the dated manuscript version. The two-day documentary lead is not treated as evidence of genuinely ex-ante selection. The files do not establish when the bounds were originally designed or why 4 and 120 were first chosen. The manuscript therefore uses them only as a historically inspected example of absolute-bound eligibility non-equivariance, not as an optimized or prospectively validated filter.
