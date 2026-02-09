from typing import Dict, Type


class SingletonMeta(type):
    """
    Metaclass that enforces the Singleton design pattern.

    Ensures that only one instance of a class exists and provides
    optional validation logic for singleton classes.
    """

    _instances: Dict[Type, object] = {}

    def __new__(cls, name, bases, namespace):
        """
        Create a new class and perform validation checks.

        For specific singleton classes (e.g., ConfigManager),
        this method validates the presence of required attributes.

        Args:
            name (str): Name of the class being created.
            bases (tuple): Base classes.
            namespace (dict): Class attribute dictionary.

        Returns:
            type: Newly created class.

        Raises:
            TypeError: If required attributes are missing.
        """
        # Validation: only for concrete singleton classes
        if name == "ConfigManager":
            if "REQUIRED_KEYS" not in namespace:
                raise TypeError(
                    "ConfigManager must define REQUIRED_KEYS"
                )

        return super().__new__(cls, name, bases, namespace)

    def __call__(cls, *args, **kwargs):
        """
        Control instance creation to enforce Singleton behavior.

        Returns:
            object: The single instance of the class.
        """
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]
