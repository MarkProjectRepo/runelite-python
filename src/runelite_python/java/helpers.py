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
            if result is None:
                return None
            return wrapper_class(result)
        return wrapper
    return decorator

def wrap_iterator(wrapper_class):
    """
    A decorator to wrap the return type of a function that returns an iterator into a specified class.
    Handles arbitrary nesting of iterables and consistently yields wrapped items.

    Args:
        wrapper_class (type): The class to wrap the return type with.

    Returns:
        function: The decorated function that yields wrapped items.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            def wrap_nested(obj):
                # Handle Java iterators/iterables
                if hasattr(obj, 'iterator'):
                    try:
                        obj = obj.iterator()
                    except Exception:
                        pass
                
                # Check if object is iterable (but not string)
                if hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes)):
                    return (wrapped_item 
                           for item in obj 
                           for wrapped_item in wrap_nested(item))
                
                # Base case: wrap individual object
                yield wrapper_class(obj)
            
            result = func(*args, **kwargs)
            yield from wrap_nested(result)
            
        return wrapper
    return decorator