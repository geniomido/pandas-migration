# Pandas 3.0 Migration Check 🐼

**Audit your Python codebase for Pandas 3.0 breaking changes.**

Pandas 3.0 introduces significant API changes (PyArrow backend, copy-on-write). This script scans your `.py` files for deprecated patterns.

## Checks For:
- `append()` (Use `concat` instead)
- `mad()` (Mean Absolute Deviation removed)
- `frame.applymap()` (Use `map`)
- `pd.value_counts()` (Use `Series.value_counts`)
- ...and more.

## Usage

```bash
python3 pandas3_migration_check.py /path/to/your/project
```

## Output

```
[WARNING] File: analysis.py:42
  usage of .append() detected. Consider using pd.concat().

[ERROR] File: old_script.py:10
  .mad() is removed in Pandas 3.0.
```

## Disclaimer
This is a static analysis tool (regex-based). It may produce false positives. Always run your tests!

## License
MIT © Geniom
