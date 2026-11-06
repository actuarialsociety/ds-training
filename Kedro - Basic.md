# Kedro - Basic
> *Kedro is an open-source Python framework (from QuantumBlack, McKinsey) that turns notebook code into **reproducible, testable data pipelines**. Every project has the same layout, so a pricing or reserving model built by one actuary can be read, rerun and reviewed by another. In this lesson you build the official *spaceflights* project, then add your own claims-frequency pipeline on real French motor data.*

# Prerequisites
- [Python - Basic](./Python%20-%20Basic.md), [PyData Stack](./PyData%20Stack.md)
- [Terminal in Windows](./Terminal%20in%20Windows.md) / [Mac](./Terminal%20in%20Mac.md) and [Git in VS Code](./Git%20in%20VSCode.md)
- [uv installed](https://docs.astral.sh/uv/getting-started/installation/) (Kedro's recommended package manager)

# Objectives
- Explain why Kedro turns notebook code into reproducible, testable pipelines
- Create a project from the `spaceflights-pandas` starter and run it with `uv run kedro run`
- Read and add **Data Catalog** entries in `conf/base/catalog.yml`
- Write a **node**, add it to a new **pipeline** with `kedro pipeline create`, and run just that pipeline
- Explore the pipeline graph in **Kedro-Viz**

# Key concepts
- **Project template**: every project has the same folders. `conf/base` holds shared config and `conf/local` holds secrets (git-ignored). Data moves through layered folders, `data/01_raw` to `08_reporting`. Code lives in `src/<pkg>/pipelines/<name>/{nodes.py, pipeline.py}`.
- **Node**: a plain Python function wrapped in `Node(func, inputs, outputs, name)`. Inputs and outputs are dataset *names*, not file paths, so the function never reads or writes files itself and is easy to test.
- **Pipeline**: a list of nodes. Kedro works out the run order from the inputs and outputs. `find_pipelines()` registers every pipeline folder automatically, and `__default__` runs them all.
- **Data Catalog**: YAML that maps each name to a dataset type and location (`pandas.CSVDataset`, `pandas.ParquetDataset`, S3 paths and so on). Swapping CSV for Parquet, or a laptop for the cloud, is a config change, not a code change. Names missing from the catalog are kept in memory.
- **Kedro-Viz**: `kedro viz run` serves an interactive graph of your nodes and datasets. It is useful for model documentation and peer review.

# Content
* [Kedro concepts](https://docs.kedro.org/en/stable/getting-started/kedro_concepts/) · [Install](https://docs.kedro.org/en/stable/getting-started/install/) · [Cheatsheet](https://docs.kedro.org/en/stable/getting-started/cheatsheet/)
* [Spaceflights tutorial](https://docs.kedro.org/en/stable/tutorials/spaceflights_tutorial/) · [Nodes](https://docs.kedro.org/en/stable/build/nodes/) · [Pipelines](https://docs.kedro.org/en/stable/build/pipeline_introduction/) · [Data Catalog](https://docs.kedro.org/en/stable/catalog-data/data_catalog/)
* [Official Kedro video course](https://docs.kedro.org/en/stable/getting-started/course/) · [Kedro-Viz docs](https://docs.kedro.org/projects/kedro-viz/en/latest/)
* **Version note:** the course videos below are from 2023 (Kedro 0.19), when projects used `pip` and the lowercase `node()`/`pipeline()` helpers. Kedro 1.x uses `uv` and the `Node`/`Pipeline` classes, and both styles still work. Use the commands in this lesson.
* **Background (optional):** [Introduction to Kedro - What is Kedro?](https://www.youtube.com/watch?v=PdNkECqvI58)

### New to Kedro? Start Here!
[![New to Kedro? Start Here!](https://img.youtube.com/vi/P4o7n-TnL5o/0.jpg)](https://www.youtube.com/watch?v=P4o7n-TnL5o)
> *Kedro · Code along: a recent, all-in-one Kedro 1.x beginner demo*

---
### Get started with Kedro - The spaceflights starter
[![Get started with Kedro - The spaceflights starter](https://img.youtube.com/vi/K6PhgVyXhWE/0.jpg)](https://www.youtube.com/watch?v=K6PhgVyXhWE)
> *Kedro · Code along: create the spaceflights project used in the follow-along*

---
### Get started with Kedro - Set up the Kedro Data Catalog
[![Get started with Kedro - Set up the Kedro Data Catalog](https://img.youtube.com/vi/rl2cncGxyts/0.jpg)](https://www.youtube.com/watch?v=rl2cncGxyts)
> *Kedro · Code along: set up the Data Catalog*

---
### Get started with Kedro - Create your first data pipeline with Kedro
[![Get started with Kedro - Create your first data pipeline with Kedro](https://img.youtube.com/vi/3YeE_gvDCvw/0.jpg)](https://www.youtube.com/watch?v=3YeE_gvDCvw)
> *Kedro · Code along: build your first nodes and pipeline*

---
### Get started with Kedro - Run your Kedro pipeline
[![Get started with Kedro - Run your Kedro pipeline](https://img.youtube.com/vi/sll_LhZE-p8/0.jpg)](https://www.youtube.com/watch?v=sll_LhZE-p8)
> *Kedro · Code along: run the pipeline and its options*

---
### Get started with Kedro - Visualise your data pipeline with Kedro-Viz
[![Get started with Kedro - Visualise your data pipeline with Kedro-Viz](https://img.youtube.com/vi/KWqSzbHgNW4/0.jpg)](https://www.youtube.com/watch?v=KWqSzbHgNW4)
> *Kedro · Code along: visualise the pipeline with Kedro-Viz*

---

# Follow-along
**Repo:** [kedro-org/kedro-starters `spaceflights-pandas`](https://github.com/kedro-org/kedro-starters/tree/main/spaceflights-pandas) · **Data:** [freMTPL2freq on OpenML](https://www.openml.org/d/41214) (678k French motor policies)

1. **Create and run the project**
   ```bash
   uvx kedro new --starter spaceflights-pandas --name spaceflights
   cd spaceflights
   uv sync
   uv run kedro run
   ```
   You should see *Completed 9 out of 9 tasks* and *Model has a coefficient R^2 of 0.387…*.
2. **Explore it.** Read `conf/base/catalog.yml` and `src/spaceflights/pipelines/data_processing/pipeline.py`, then run:
   ```bash
   uv run kedro registry list            # __default__, data_processing, data_science, reporting
   uv run kedro run --pipelines data_science
   uv run kedro viz run
   ```
3. **Get the actuarial data** (about 1 minute):
   ```bash
   uv run python -c "from sklearn.datasets import fetch_openml; fetch_openml(data_id=41214, as_frame=True).frame.to_csv('data/01_raw/freMTPL2freq.csv', index=False)"
   ```
4. **Scaffold a pipeline and register its data**
   ```bash
   uv run kedro pipeline create claims_frequency
   ```
   Append to `conf/base/catalog.yml`:
   ```yaml
   policies:
     type: pandas.CSVDataset
     filepath: data/01_raw/freMTPL2freq.csv

   frequency_by_area:
     type: pandas.CSVDataset
     filepath: data/08_reporting/frequency_by_area.csv
   ```
5. **Write the node and the pipeline.** In `src/spaceflights/pipelines/claims_frequency/nodes.py`:
   ```python
   import pandas as pd

   def frequency_by_area(policies: pd.DataFrame) -> pd.DataFrame:
       """Observed claim frequency (claims per policy-year) by area."""
       summary = policies.groupby("Area", observed=True)[["ClaimNb", "Exposure"]].sum()
       summary["frequency"] = summary["ClaimNb"] / summary["Exposure"]
       return summary.reset_index()
   ```
   In `pipeline.py`:
   ```python
   from kedro.pipeline import Node, Pipeline
   from .nodes import frequency_by_area

   def create_pipeline(**kwargs) -> Pipeline:
       return Pipeline([
           Node(func=frequency_by_area, inputs="policies",
                outputs="frequency_by_area", name="frequency_by_area_node"),
       ])
   ```
6. **Run and view it**
   ```bash
   uv run kedro run --pipelines claims_frequency
   uv run kedro viz run
   ```
   Open `data/08_reporting/frequency_by_area.csv`. Frequency rises from about **0.082** in area A to about **0.139** in area F.
7. **Now try:** add a second node, `frequency_by_bonus_malus`, that groups by `BonusMalus` bands. Register its output in the catalog and wire it into the pipeline.

---
_Last reviewed: 2026-11-06_
