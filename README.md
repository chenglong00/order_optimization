# Technologies

- Python >= 3.10
- FastAPI, uvcorn, Pydantic
- Docker/Kubernetes for deployment & scale

# Overview

Main packages:

- `order_optimizer.optimizer.optimizer`: implemenation of optimization logic
- `order_optimizer.optimizer.order`: implementation of Order Object
- `order_optimizer.api.main`: main entry point (e.i. FastAPIs).
- `tests.test_optimizer`: unit and integration tests.


# Development
- pip list --format=freeze > requirements.txt
- Install python/anaconda virtual environment (refer to `Deployment` section for a docker quick-start approach):

```
cd path/to/project

virtualenv -p python3.10 venv    # Or conda create -n tcb-pool python=3.8
source venv/bin/activate        # Or conda activate tcb-pool
pip install -r requirements.txt

# Set PYTHONPATH for module imports
export PYTHONPATH=path/to/project/order_optimizer
```

Config IDE (e.g PyCharm) to use the virtual environment `venv`: Go to File > Settings > Project Interpreter. To resolve
import problems, right-click on the `order_optimizer` folder and mark this directory as source root.

- Start APIs:

```bash
python order_optimizer/main.py
```
Run unit tests in `tests/` folder:

```bash
# To run all tests
python -m unittest discover -p *test*.py -v
```

Test coverage: just replace the initial `python` with `coverage run`

```bash
coverage run -m unittest discover -p *test*.py -v

# To show report on console
coverage report -m  # must above 90%

# To show report on Web UI
coverage html
```


# Deployment with High-availability and Scalability

```bash
# Build docker image
docker build -t order-optimizer:1.0.0 .

# To run APIs in a container
docker container run --name order-optimizer -p 5000:5000 order-optimizer:1.0.0 
```

# Contributors

- Chenglong Wu(chenglong.w1@gmail.com)