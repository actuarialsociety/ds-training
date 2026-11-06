# Kedro - Intermediate
> *Make one pipeline do many jobs. Drive it with **parameters** and **environments**, reuse it with **namespaces** (champion vs challenger, as in a pricing review), cut catalog boilerplate with **dataset factories**, keep every model with **versioning**, run just the slices you need, and test it all with pytest.*

# Prerequisites
- [Kedro - Basic](./Kedro%20-%20Basic.md) (your `spaceflights` project with the `claims_frequency` pipeline)
- Basic pytest is helpful

# Objectives
- Control behaviour with parameters, override them from the CLI, and switch config environments (`conf/base`, `conf/local`, `conf/prod`)
- Reuse one pipeline twice with **namespaces** (champion vs challenger model)
- Replace repeated catalog entries with **dataset factories**, and **version** model outputs
- Run parts of a pipeline with `--pipelines`, `--nodes`, `--from-nodes`, `--to-outputs`, `--namespaces` and `--tags`
- Work with project data in IPython/Jupyter and unit-test nodes with pytest

# Key concepts
- **OmegaConfigLoader and environments**: `conf/base` is shared. `--env prod` layers `conf/prod` on top, and the default run environment is `local`. Credentials live in the git-ignored `conf/local/credentials.yml` and are referenced by name from the catalog. Templating such as `${oc.env:VAR}` and `${runtime_params:key}` keeps config flexible.
- **Parameters**: values in `parameters*.yml` reach nodes as `params:<key>`. Override them at run time with `--params "model_options.test_size=0.3"`. Since 1.3, a Pydantic model or dataclass type hint validates parameters automatically.
- **Namespaces**: `Pipeline(base, namespace="challenger", inputs={...}, parameters={...})` prefixes every node, dataset and parameter name, so the same pipeline can run twice side by side. Kedro-Viz collapses each namespace into one expandable "super node".
- **Dataset factories and versioning**: a pattern such as `"{namespace}.regressor"` covers many catalog entries at once. `versioned: true` saves a timestamped copy on every run, and `--load-versions` reloads an older one. This gives you a model audit trail for free.
- **Slicing**: run part of a pipeline with `--nodes`, `--from-nodes`, `--to-outputs` and `--tags`. A slice can only start where its inputs are *persisted*. Datasets held only in memory don't exist between runs.
- **Notebooks and tests**: `kedro ipython` / `kedro jupyter lab` (or `%load_ext kedro.ipython`) gives you `catalog`, `context`, `pipelines` and `session`. Nodes are plain functions, so you test them directly with pytest.

# Content
* [Configuration basics](https://docs.kedro.org/en/stable/configure/configuration_basics/) · [Parameters](https://docs.kedro.org/en/stable/configure/parameters_and_credentials/) · [Templating](https://docs.kedro.org/en/stable/configure/templating/)
* [Namespaces](https://docs.kedro.org/en/stable/build/namespaces/) · [Dataset factories](https://docs.kedro.org/en/stable/catalog-data/kedro_dataset_factories/) · [Slice a pipeline](https://docs.kedro.org/en/stable/build/slice_a_pipeline/)
* [Kedro and notebooks](https://docs.kedro.org/en/stable/integrations-and-plugins/notebooks_and_ipython/kedro_and_notebooks/) · [Test a project](https://docs.kedro.org/en/stable/tutorials/test_a_project/)
* **More code-alongs (optional):** [Apply versioning to datasets](https://www.youtube.com/watch?v=iRwy-IStfPo) · [Use Kedro from Jupyter](https://www.youtube.com/watch?v=3q2RNWLibyY) · [Visualise pipelines in notebooks](https://www.youtube.com/watch?v=fuxXtJPypAY)

### Make complex Kedro pipelines - Master parameters in Kedro
[![Make complex Kedro pipelines - Master parameters in Kedro](https://img.youtube.com/vi/eIA12RQMlFY/0.jpg)](https://www.youtube.com/watch?v=eIA12RQMlFY)
> *Kedro · Code along: parameters*

---
### Ship your Kedro project to production - Define your own Kedro environments
[![Ship your Kedro project to production - Define your own Kedro environments](https://img.youtube.com/vi/9quRBGDOFq8/0.jpg)](https://www.youtube.com/watch?v=9quRBGDOFq8)
> *Kedro · Code along: define your own environments*

---
### Make complex Kedro pipelines - Reuse your Kedro pipeline using namespaces
[![Make complex Kedro pipelines - Reuse your Kedro pipeline using namespaces](https://img.youtube.com/vi/cYHHVAoWZ2E/0.jpg)](https://www.youtube.com/watch?v=cYHHVAoWZ2E)
> *Kedro · Code along: reuse a pipeline with namespaces*

---
### Make complex Kedro pipelines - Create Kedro datasets dynamically using factories
[![Make complex Kedro pipelines - Create Kedro datasets dynamically using factories](https://img.youtube.com/vi/tNE-tdvHNP8/0.jpg)](https://www.youtube.com/watch?v=tNE-tdvHNP8)
> *Kedro · Code along: dataset factories*

---
### Slice your Kedro pipelines from the CLI and on Kedro Viz
[![Slice your Kedro pipelines from the CLI and on Kedro Viz](https://img.youtube.com/vi/NtqE0Kd97YE/0.jpg)](https://www.youtube.com/watch?v=NtqE0Kd97YE)
> *Kedro · Code along: slicing pipelines from the CLI and in Kedro-Viz*

---
### All about the Data Catalog
[![All about the Data Catalog](https://img.youtube.com/vi/-rozSBY2g48/0.jpg)](https://www.youtube.com/watch?v=-rozSBY2g48)
> *Kedro · Code along: the Kedro 1.x Data Catalog in depth (environments, templating, factories)*

---

# Follow-along
**Project:** your `spaceflights` project from [Kedro - Basic](./Kedro%20-%20Basic.md). Every command below was tested on Kedro 1.7.

1. **Parameters and slices**
   ```bash
   uv run kedro run --params "model_options.test_size=0.3"     # R^2 changes to ~0.331
   uv run kedro run --nodes split_data_node,train_model_node
   uv run kedro run --from-nodes split_data_node
   uv run kedro run --to-outputs model_input_table
   ```
   Then try `--from-nodes train_model_node`. It fails, because `X_train` and the other splits live only in memory.
2. **A prod environment**
   ```bash
   mkdir -p conf/prod
   printf 'model_options:\n  test_size: 0.3\n  random_state: 42\n  features:\n    - engines\n    - passenger_capacity\n    - crew\n' > conf/prod/parameters_data_science.yml
   uv run kedro run --env prod --pipelines data_science       # R^2 ~0.366: prod overrides base
   ```
3. **Challenger model with a namespace**
   ```bash
   uv run kedro pipeline create model_challenger
   ```
   Replace `src/spaceflights/pipelines/model_challenger/pipeline.py` with:
   ```python
   from kedro.pipeline import Pipeline
   from ..data_science.pipeline import create_pipeline as base_data_science

   def create_pipeline(**kwargs) -> Pipeline:
       return Pipeline(
           base_data_science(),
           namespace="challenger",
           inputs={"model_input_table"},                       # shared input, not prefixed
           parameters={"params:model_options": "params:challenger_model_options"},
       )
   ```
   In `conf/base/parameters_model_challenger.yml`:
   ```yaml
   challenger_model_options:
     test_size: 0.2
     random_state: 3
     features: [engines, passenger_capacity, crew, company_rating]
   ```
4. **Dataset factory with versioning.** Append to `catalog.yml`:
   ```yaml
   "{namespace}.regressor":
     type: pickle.PickleDataset
     filepath: data/06_models/{namespace}_regressor.pickle
     versioned: true
   ```
   ```bash
   uv run kedro run                       # 12 tasks, two R^2 values: champion vs challenger
   uv run kedro run --namespaces challenger
   uv run kedro catalog resolve-patterns
   uv run kedro viz run                   # a collapsible "Challenger" node
   ```
   Look in `data/06_models/challenger_regressor.pickle/`. There is one timestamped folder per run.
5. **Interactive work**
   ```bash
   uv run kedro ipython
   ```
   In the IPython session, try `catalog.load("model_input_table").shape`, which should be `(6027, 27)`, and `catalog.load("frequency_by_area")`. Inside Jupyter, `%load_node split_data_node` pulls a node's code into cells for debugging.
6. **Tests**
   ```bash
   uv sync --extra dev
   uv run pytest                          # the starter's 4 tests pass
   ```
   Add `tests/pipelines/claims_frequency/test_nodes.py` that builds a 4-row DataFrame by hand and asserts that `frequency_by_area` returns the right claims-per-exposure for each area.

---
_Last reviewed: 2026-11-06_
