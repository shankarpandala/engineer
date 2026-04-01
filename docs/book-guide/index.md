# Book Guide

Use this guide to move between *Machine Learning for Trading, Third Edition* and
`ml4t-engineer` without guessing which notebook maps to which production API.

`ml4t-engineer` appears in two distinct ways throughout the book:

- pedagogical notebooks that build ideas step by step
- reusable library workflows that collapse those ideas into stable APIs

The book teaches the method. The library is where you should go when you want to
reuse that method across assets, case studies, and production pipelines.

## How to Use This Guide

Start from the book if you want intuition, derivations, and plots. Start from the
library guides if you want reusable implementations, validated APIs, and pipeline
integration.

Use this page when you need to answer one of these questions:

- "Which chapter teaches the concept behind this API?"
- "Which notebook should I read before using this workflow in production?"
- "Which library guide replaces the manual code from the book?"

## Recommended Reader Journey

1. Read the relevant chapter notebook to understand the modeling idea.
2. Jump to the matching user-guide page for the production API.
3. Use the case-study pipeline files as the bridge from teaching code to reusable
   workflows.
4. Use the [API Reference](../api/index.md) when you need exact signatures.

## Chapter Map

### Chapter 3: Market Microstructure

| Book path | What the book teaches | Library entry point | Docs page |
|-----------|-----------------------|---------------------|-----------|
| `03_market_microstructure/code/08_itch_bar_sampling.py` | Why time bars are statistically weak and how tick, volume, and dollar bars improve sampling | `TickBarSampler`, `VolumeBarSampler`, `DollarBarSampler` | [Alternative Bars](../user-guide/bars.md) |
| `03_market_microstructure/code/10_itch_information_bars.py` | Imbalance bars and threshold dynamics | `TickImbalanceBarSampler`, `FixedTickImbalanceBarSampler`, `FixedVolumeImbalanceBarSampler` | [Alternative Bars](../user-guide/bars.md) |
| `03_market_microstructure/code/13_databento_bar_sampling.py` | Applying bar samplers to a modern vendor feed | Same sampler family with production input contracts | [Alternative Bars](../user-guide/bars.md) |

What changes when you move to the library:

- the book focuses on the statistical motivation and diagnostics
- the library gives you stable samplers, warnings, and reusable OHLCV outputs
- fixed-threshold imbalance bars are the recommended production path

### Chapter 7: Defining the Learning Task

| Book path | What the book teaches | Library entry point | Docs page |
|-----------|-----------------------|---------------------|-----------|
| `07_defining_learning_task/code/02_preprocessing_pipeline.py` | Leakage-safe preprocessing and split-aware scaling | `StandardScaler`, `MinMaxScaler`, `RobustScaler`, `PreprocessingPipeline` | [Preprocessing](../user-guide/preprocessing.md) |
| `07_defining_learning_task/code/03_label_methods.py` | Triple-barrier, percentile, trend-scanning, meta-labeling, and sample weighting | `LabelingConfig`, `triple_barrier_labels`, `rolling_percentile_binary_labels`, `trend_scanning_labels`, `meta_labels` | [Labeling](../user-guide/labeling.md) |
| `07_defining_learning_task/code/04_minimum_favorable_adverse_excursion.py` | Barrier behavior and excursion analysis | `LabelingConfig.triple_barrier()` | [Labeling](../user-guide/labeling.md) |
| `07_defining_learning_task/code/10_ml4t_library_ecosystem.py` | The library-oriented view of feature computation, discovery, and dataset building | `compute_features`, `feature_catalog`, `create_dataset_builder` | [Features](../user-guide/features.md), [Feature Discovery](../user-guide/discovery.md), [Dataset Builder](../user-guide/dataset-builder.md) |

What changes when you move to the library:

- manual notebook experiments become serialized `LabelingConfig` workflows
- feature discovery moves from ad hoc inspection to metadata-driven search
- dataset preparation becomes train-only scaling and splitter-aware folds by default

### Chapter 8: Feature Engineering

| Book path | What the book teaches | Library entry point | Docs page |
|-----------|-----------------------|---------------------|-----------|
| `08_feature_engineering/code/01_price_volume_features.py` | Momentum, trend, volatility, and volume feature intuition | `compute_features` with registry-backed indicators | [Features](../user-guide/features.md) |
| `08_feature_engineering/code/02_microstructure_features.py` | Microstructure feature construction and interpretation | Microstructure feature functions and registry metadata | [Features](../user-guide/features.md) |
| `08_feature_engineering/code/03_structural_cross_instrument_features.py` | Cross-asset and panel relationships | `ml4t.engineer.features.cross_asset` | [Features](../user-guide/features.md) |
| `08_feature_engineering/code/04_fundamentals_macro_calendar.py` | Lag features, calendar encodings, and ML-oriented transforms | ML feature utilities and preprocessing bridge | [Features](../user-guide/features.md), [ML Readiness](../user-guide/ml-readiness.md) |

What changes when you move to the library:

- the book derives and visualizes features individually
- the library lets you request validated feature sets through one computation API
- registry and catalog metadata help you choose features systematically

### Chapter 9: Time-Series Analysis

| Book path | What the book teaches | Library entry point | Docs page |
|-----------|-----------------------|---------------------|-----------|
| `09_time_series_analysis/code/03_fractional_differencing.py` | The memory-stationarity tradeoff and ADF-based search for `d` | `ffdiff`, `find_optimal_d`, `fdiff_diagnostics` | [Fractional Differencing](../user-guide/fractional-differencing.md) |
| `09_time_series_analysis/code/08_garch_volatility.py` | Volatility estimators and conditional volatility modeling | Volatility feature family | [Features](../user-guide/features.md) |
| `09_time_series_analysis/code/09_har_rough_volatility.py` | Multi-horizon volatility structure | Volatility features used downstream in pipelines | [Features](../user-guide/features.md) |
| `09_time_series_analysis/code/11_hmm_regimes.py` | Regime detection workflows | Regime feature family | [Features](../user-guide/features.md) |
| `09_time_series_analysis/code/13_regime_as_feature.py` | Turning regimes into model inputs | Regime features in reusable pipelines | [Features](../user-guide/features.md) |
| `09_time_series_analysis/code/14_panel_features.py` | Cross-sectional panel features | Cross-asset feature functions for multi-asset inputs | [Features](../user-guide/features.md) |

What changes when you move to the library:

- research notebooks stay focused on method validation
- library functions package the same transforms into repeatable feature pipelines
- the case studies show how to combine these transforms with labels and CV

## Case-Study Pipeline Map

Most case studies follow the same structure. `ml4t-engineer` is the handoff point
between raw market data and model-ready datasets.

| Case-study step | Typical file | Library workflow | Docs page |
|-----------------|--------------|------------------|-----------|
| Labels | `case_studies/<study>/code/02_labels.py` | `LabelingConfig`, barrier labels, percentile labels, fixed-horizon labels | [Labeling](../user-guide/labeling.md) |
| Features | `case_studies/<study>/code/03_features.py` | `compute_features` plus feature-specific functions | [Features](../user-guide/features.md) |
| Temporal prep | `case_studies/<study>/code/04_temporal.py` | fractional differencing and leakage-safe preparation | [Fractional Differencing](../user-guide/fractional-differencing.md), [Dataset Builder](../user-guide/dataset-builder.md) |

Examples called out in the current integration audit:

- ETFs: percentile labels, production `compute_features`, fractional differencing
- US Equities Panel: triple-barrier labels, panel features, fractional differencing
- CME Futures: ATR-based barriers and futures-aware labeling workflows
- NASDAQ-100 Microstructure: manual pedagogical implementations with strong overlap to
  production-ready microstructure features in this library

## From Notebook Code to Library API

Use this translation when moving from the book to reusable code:

| Book pattern | Library equivalent |
|--------------|--------------------|
| Manually computing several indicators in sequence | `compute_features(data, feature_spec)` |
| Notebook-only feature browsing | `feature_catalog.list()`, `feature_catalog.search()`, `registry.get()` |
| Inline barrier parameters spread across a notebook | `LabelingConfig.triple_barrier(...)` or `LabelingConfig.atr_barrier(...)` |
| One-off train/test scaling | `create_dataset_builder(..., scaler=...)` |
| Manual stationarity experiments | `find_optimal_d()` then `ffdiff()` |
| Bar-construction experiments | sampler classes in `ml4t.engineer.bars` |

## Maturity and Scope

These are the workflows readers should prioritize:

- production-ready: feature computation, labeling methods, alternative bars,
  fractional differencing, feature discovery, dataset builder
- advanced: cross-asset feature workflows and pipeline orchestration
- experimental or low-priority: DuckDB store and any workflows not yet used in the
  book or case studies

This matches the current audit: the strongest value in `ml4t-engineer` is the
production API for feature engineering, labeling, and dataset preparation.

## Where to Go Next

- Start with [Quickstart](../getting-started/quickstart.md) if you want a working
  example first.
- Read [Features](../user-guide/features.md) for the core computation API.
- Read [Labeling](../user-guide/labeling.md) if you are building supervised targets.
- Read [Alternative Bars](../user-guide/bars.md) for microstructure workflows.
- Read [Dataset Builder](../user-guide/dataset-builder.md) for leakage-safe model
  inputs.
- Use [API Reference](../api/index.md) for exact signatures.
