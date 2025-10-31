### 🔍 Indexing Performance Comparison

| Metric | Before Index | After Index |
|---------|---------------|--------------|
| Query Stage | COLLSCAN (Collection Scan) | IXSCAN + FETCH (Index Scan) |
| Index Used | None | category_1 |
| totalDocsExamined | 22 | 7 |
| totalKeysExamined | 0 | 7 |
| nReturned | 7 | 7 |
| executionTimeMillis | ~0 ms (small data) | ~29 ms (with index overhead) |

**Observation:**  
Before indexing, MongoDB scanned the entire `products` collection to find matching categories.  
After adding an index on `category`, the query planner switched to using an `IXSCAN`, scanning only the indexed documents and retrieving results directly.  

### Text Search Summary

- Created a compound text index on `name` and `category`.
- Used `$text` search to find products by keywords such as `"watch"`, `"electronics"`, and `"clothing"`.
- Verified performance using `explain("executionStats")` — query plan showed `"TEXT_MATCH"` stage with index `"name_text_category_text"`.
