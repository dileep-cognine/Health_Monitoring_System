# Profiling Report — System Monitoring Platform

## Tools Used
- cProfile
- timeit

---

## Bottleneck 1: Metric Processing Logic

### Description
Initial implementation recalculated the average inside a loop, leading to O(N²) complexity.

### Before Optimization
- Dataset size: 10,000
- Execution Time (timeit): 0.8421 seconds

### Optimization Applied
- Precomputed average once
- Replaced loop with list comprehension

### After Optimization
- Execution Time (timeit): 0.1124 seconds

### Improvement
- Performance improvement: ~86.6%

---

## Bottleneck 2: Redundant Computations

### Description
Repeated function calls caused unnecessary CPU usage.

### Optimization
- Cached intermediate results
- Reduced redundant calculations

### Result
- Reduced CPU overhead
- Improved response time under load

---

## Conclusion
Profiling identified critical inefficiencies in data processing.
Optimizations reduced execution time significantly while maintaining correctness.
