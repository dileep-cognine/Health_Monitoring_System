import cProfile
from src.data_handlers.metrics_before import process_metrics

metrics = list(range(10_000))

cProfile.run("process_metrics(metrics)")
