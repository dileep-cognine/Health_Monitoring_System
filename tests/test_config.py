from src.metaclasses.config_manager import ConfigManager


def test_singleton_config():
    """
    Verify that ConfigManager follows the Singleton pattern.

    This test ensures that multiple instantiations of ConfigManager
    return the same object instance.
    """
    c1 = ConfigManager()
    c2 = ConfigManager()
    assert c1 is c2
