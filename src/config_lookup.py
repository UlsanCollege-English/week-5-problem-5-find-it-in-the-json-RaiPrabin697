def find_key(data, target):
    """
    Recursively search for the first occurrence of `target` key in
    nested structures (dicts, lists, tuples).
    Returns the associated value or None if not found.
    """
    # Handle dicts
    if isinstance(data, dict):
        # Check if key exists at current level
        if target in data:
            return data[target]
        # Otherwise, search in all values
        for value in data.values():
            result = find_key(value, target)
            if result is not None:
                return result
        return None

    # Handle lists or tuples
    elif isinstance(data, (list, tuple)):
        for item in data:
            result = find_key(item, target)
            if result is not None:
                return result
        return None

    # Other data types — can't contain target
    return None
