# Kedro - Advanced
> *Take a Kedro project to production. Add **hooks** for cross-cutting behaviour, **validate** data in the catalog, track a Poisson claims-frequency **GLM** in **MLflow**, choose a **runner**, and ship the project as a **Docker** image and an **Airflow** DAG. It ends with Kedro 1.x's GenAI features: LLM context nodes, serving pipelines over HTTP, and agents.*

# Prerequisites
- [Kedro - Intermediate](./Kedro%20-%20Intermediate.md) (your `spaceflights` project with `claims_frequency`)
- Docker (optional; see [Devcontainers in VS Code](./Devcontainers%20in%20VS%20Code.md) / [WSL](./Windows%20Subsystem%20Linux.md)); some MLflow basics help

# Objectives
- Write and register a **hook** (timing every node), and know which runners run it
- Enforce data quality with catalog **validators** (Pandera), and know when you need a custom dataset instead
- Track a claims-frequency GLM in **MLflow** with `kedro-mlflow`
- Speed up runs with `ThreadRunner` or `ParallelRunner`, and package the project for **Docker** and **Airflow**
- Know the Kedro 1.x GenAI and serving features: `llm_context_node`, `kedro server` and the MCP server

# Key concepts
- **Hooks**: functions that run at fixed points, such as `before/after_node_run`, `before/after_dataset_loaded/saved`, `after_catalog_created`, `before/after_pipeline_run` and `on_node_error`. You mark them `@hook_impl` and register them in `settings.py` (`HOOKS = (...)`). Plugins such as kedro-mlflow register themselves. **`ParallelRunner` does not run node or dataset hooks** in its worker processes.
- **Dataset validation (new in 1.6)**: add `validator: pkg.schemas.Schema` to a catalog entry, and Kedro checks the data on every load and save, in runs, notebooks and CI. `severity: warn` logs problems instead of failing. Pandera support comes from `kedro[pandera-pandas]`.
- **Custom datasets**: subclass `AbstractDataset` and implement `_load`, `_save` and `_describe` for anything [kedro-datasets](https://docs.kedro.org/projects/kedro-datasets/en/latest/) doesn't already cover. It covers Spark, Polars, SQL and cloud storage through fsspec.
- **Runners and deployment**: `ThreadRunner` suits I/O-bound work. `ParallelRunner` uses processes and needs datasets that can be pickled. `kedro docker` builds a uv-based image. `kedro airflow create` turns a pipeline into a DAG (`--group-by memory|namespace` merges nodes into fewer tasks). There are also guides for Databricks, Vertex AI and Argo, and `kedro package` builds a wheel.
- **Experiment tracking**: with kedro-mlflow, every `kedro run` becomes an MLflow run with its parameters logged. `MlflowModelTrackingDataset` and `MlflowMetricsHistoryDataset` log models and metrics straight from the catalog.
- **GenAI in 1.x**: `llm_context_node` (stable since 1.7) bundles an LLM, prompts and `tool()`s into an `LLMContext` for downstream agent nodes. `kedro server start` exposes `/health` and `/run` over HTTP, and `kedro-mcp` lets AI agents drive your pipelines.

# Content
* [Hooks](https://docs.kedro.org/en/stable/extend/hooks/introduction/) · [Hook examples](https://docs.kedro.org/en/stable/extend/hooks/examples/) · [Dataset validation](https://docs.kedro.org/en/stable/catalog-data/dataset_validation/) · [Custom datasets](https://docs.kedro.org/en/stable/extend/how_to_create_a_custom_dataset/)
* [MLflow integration](https://docs.kedro.org/en/stable/integrations-and-plugins/mlflow/) · [kedro-mlflow docs](https://kedro-mlflow.readthedocs.io/en/stable/) · [Runners](https://docs.kedro.org/en/stable/build/run_a_pipeline/)
* [Deployment overview](https://docs.kedro.org/en/stable/deploy/) · [Docker](https://docs.kedro.org/en/stable/deploy/single_machine/) · [Airflow](https://docs.kedro.org/en/stable/deploy/supported-platforms/airflow/) · [Databricks](https://docs.kedro.org/en/stable/deploy/supported-platforms/databricks/)
* [LLM context node](https://docs.kedro.org/en/stable/build/llm_context_node/) · [Serving](https://docs.kedro.org/en/stable/extend/serving/) · [MCP](https://docs.kedro.org/en/stable/develop/vibe_coding_with_mcp/)
* **More code-alongs (optional):** [Kedro in Docker](https://www.youtube.com/watch?v=lA-Ivuxmakw) · [Deploy to Databricks](https://www.youtube.com/watch?v=9ZttTN6zDM0) · [Serving over HTTP](https://www.youtube.com/watch?v=4ygwCQdX6PE) · [Agents and MCP](https://www.youtube.com/watch?v=ZjZUMGPMQ0k)

### Extend your Kedro project using Hooks
[![Extend your Kedro project using Hooks](https://img.youtube.com/vi/Xf8pYbJd1qg/0.jpg)](https://www.youtube.com/watch?v=Xf8pYbJd1qg)
> *Kedro · Code along: extend a project with hooks (demo in the first 20 minutes)*

---
### Dataset Validation is coming to Kedro
[![Dataset Validation is coming to Kedro](https://img.youtube.com/vi/tDJB4c5K6eg/0.jpg)](https://www.youtube.com/watch?v=tDJB4c5K6eg)
> *Kedro · Code along: dataset validation, the feature that shipped in 1.6*

---
### Experiment tracking with Kedro and MLflow
[![Experiment tracking with Kedro and MLflow](https://img.youtube.com/vi/Az_6UKqbznw/0.jpg)](https://www.youtube.com/watch?v=Az_6UKqbznw)
> *Kedro · Code along: experiment tracking with kedro-mlflow*

---
### Make complex Kedro pipelines - Accelerate your Kedro pipeline using runners
[![Make complex Kedro pipelines - Accelerate your Kedro pipeline using runners](https://img.youtube.com/vi/_B6R2uOj3-s/0.jpg)](https://www.youtube.com/watch?v=_B6R2uOj3-s)
> *Kedro · Code along: speed up a pipeline with runners*

---
### Ship your Kedro project to production - Deploy your Kedro project to Apache Airflow
[![Ship your Kedro project to production - Deploy your Kedro project to Apache Airflow](https://img.youtube.com/vi/AhCcnJ1Au70/0.jpg)](https://www.youtube.com/watch?v=AhCcnJ1Au70)
> *Kedro · Code along: deploy a Kedro project to Apache Airflow*

---
### Kedro + LangGraph: Easy Agentic Workflows
[![Kedro + LangGraph: Easy Agentic Workflows](https://img.youtube.com/vi/U-5CYb7NIj4/0.jpg)](https://www.youtube.com/watch?v=U-5CYb7NIj4)
> *Kedro · Code along: an insurance customer-support agent with Kedro and LangGraph ([demo project](https://github.com/kedro-org/kedro-academy/tree/main/kedro-agentic-workflows))*

---

# Follow-along
**Project:** your `spaceflights` project with the `claims_frequency` pipeline. Every command below was tested on Kedro 1.7, MLflow 3.18 and Python 3.12.

1. **Timing hook.** Create `src/spaceflights/hooks.py`:
   ```python
   import logging, time
   from kedro.framework.hooks import hook_impl
   logger = logging.getLogger(__name__)

   class NodeTimerHooks:
       def __init__(self):
           self._start = {}

       @hook_impl
       def before_node_run(self, node):
           self._start[node.name] = time.perf_counter()

       @hook_impl
       def after_node_run(self, node):
           logger.info("Node %s took %.2fs", node.name, time.perf_counter() - self._start.pop(node.name))
   ```
   At the end of `settings.py`, add `from spaceflights.hooks import NodeTimerHooks` and `HOOKS = (NodeTimerHooks(),)`. Then run:
   ```bash
   uv run kedro run --pipelines data_processing --runner ThreadRunner     # logs "Node … took …s"
   uv run kedro run --pipelines data_processing --runner ParallelRunner   # no timings: hooks don't fire in workers
   ```
2. **Validate the policy data**
   ```bash
   uv add "kedro[pandera-pandas]"
   ```
   Create `src/spaceflights/schemas.py`:
   ```python
   import pandera.pandas as pa

   class PolicySchema(pa.DataFrameModel):
       IDpol: float = pa.Field(unique=True)
       ClaimNb: int = pa.Field(ge=0)
       Exposure: float = pa.Field(gt=0, le=1)

       class Config:
           strict = False
           coerce = True
   ```
   Add `validator: spaceflights.schemas.PolicySchema` under `policies:` in `catalog.yml` and run `uv run kedro run --pipelines claims_frequency`. It **fails**, because 1,224 policies have `Exposure > 1`, up to 2.01. This is a real data-quality finding. Switch the entry to the warning form:
   ```yaml
     validator:
       class: spaceflights.schemas.PolicySchema
       severity: warn
   ```
   Then handle the bad rows in the model node (next step).
3. **Poisson frequency GLM node.** Append to `claims_frequency/nodes.py`:
   ```python
   from sklearn.linear_model import PoissonRegressor
   from sklearn.metrics import mean_poisson_deviance

   def fit_frequency_glm(policies: pd.DataFrame, params: dict):
       """Poisson GLM for claim frequency, weighted by exposure."""
       policies = policies.assign(Exposure=policies["Exposure"].clip(upper=1))
       X = policies[params["features"]]
       y = policies["ClaimNb"] / policies["Exposure"]
       glm = PoissonRegressor(alpha=params["alpha"], max_iter=300)
       glm.fit(X, y, sample_weight=policies["Exposure"])
       deviance = mean_poisson_deviance(y, glm.predict(X), sample_weight=policies["Exposure"])
       return glm, {"mean_poisson_deviance": {"value": deviance, "step": 0}}
   ```
   Add the node to the pipeline:
   ```python
   Node(func=fit_frequency_glm, inputs=["policies", "params:frequency_glm"],
        outputs=["frequency_glm", "frequency_glm_metrics"], name="fit_frequency_glm_node")
   ```
   And create `conf/base/parameters_claims_frequency.yml`:
   ```yaml
   frequency_glm:
     alpha: 0.0001
     features: [VehPower, VehAge, DrivAge, BonusMalus, Density]
   ```
4. **Track it in MLflow**
   ```bash
   uv add kedro-mlflow
   uv run kedro mlflow init
   ```
   In `conf/local/mlflow.yml`, set `mlflow_tracking_uri: sqlite:///mlflow.db`. MLflow 3.18 rejects the old `./mlruns` file store. Then append to `catalog.yml`:
   ```yaml
   frequency_glm:
     type: kedro_mlflow.io.models.MlflowModelTrackingDataset
     flavor: mlflow.sklearn

   frequency_glm_metrics:
     type: kedro_mlflow.io.metrics.MlflowMetricsHistoryDataset
   ```
   ```bash
   uv run kedro run --pipelines claims_frequency
   uv run kedro mlflow ui        # parameter frequency_glm, mean Poisson deviance ≈ 0.626, sklearn model
   ```
   Change `alpha` or `features`, re-run, and compare the runs in the UI.
5. **Containerise**
   ```bash
   uv add kedro-docker
   uv run kedro docker init
   uv run kedro docker build --image kedro-claims
   uv run kedro docker run --image kedro-claims --pipelines claims_frequency
   ```
6. **Airflow DAG**
   ```bash
   uv add kedro-airflow
   uv run kedro airflow create --pipelines claims_frequency
   ```
   Open `airflow_dags/spaceflights_claims_frequency_dag.py`. It has one task per node. Try `--group-by memory` and see how the DAG changes.
7. **Optional, serving and agents:** `uv add "kedro[server]"`, then `uv run kedro server start`, then `curl http://127.0.0.1:8000/health`. Then read the [LLM context node docs](https://docs.kedro.org/en/stable/build/llm_context_node/) and browse [kedro-agentic-workflows](https://github.com/kedro-org/kedro-academy/tree/main/kedro-agentic-workflows) alongside video 6. It needs an OpenAI key and Langfuse or Opik credentials.

---
_Last reviewed: 2026-11-06_
