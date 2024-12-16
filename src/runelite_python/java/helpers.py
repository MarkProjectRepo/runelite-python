def wrap_getter(wrapper_class):
    """
    A decorator to wrap the return type of a function into a specified class.

    Args:
        wrapper_class (type): The class to wrap the return type with.

    Returns:
        function: The decorated function with wrapped return type.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return wrapper_class(result)
        return wrapper
    return decorator

# Wrapper but for iterators
def wrap_iterator(wrapper_class):
    """
    A decorator to wrap the return type of a function that returns an iterator into a specified class.
    Handles arbitrary nesting of iterables.

    Args:
        wrapper_class (type): The class to wrap the return type with.

    Returns:
        function: The decorated function with wrapped return type.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            def wrap_nested(obj):
                # Handle Java iterators/iterables more carefully
                if hasattr(obj, 'iterator'):
                    try:
                        obj = obj.iterator()
                    except Exception:
                        # If iterator() fails, try treating it as a regular iterable
                        pass
                
                # Check if object is iterable (but not string)
                if hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes)):
                    return [wrap_nested(item) for item in obj]
                # Base case: wrap individual object
                return wrapper_class(obj)
            
            result = func(*args, **kwargs)
            return wrap_nested(result)
        return wrapper
    return decorator