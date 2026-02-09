import timeit

before = timeit.timeit(
    "process_metrics(metrics)",
    setup="from src.data_handlers.metrics_before import process_metrics; metrics=list(range(10000))",
    number=10
)

after = timeit.timeit(
    "process_metrics(metrics)",
    setup="from src.data_handlers.metrics_after import process_metrics; metrics=list(range(10000))",
    number=10
)

print(f"Before: {before:.4f}s")
print(f"After: {after:.4f}s")
