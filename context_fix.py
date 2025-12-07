# context_fix.py
import django.template.context


def new_context_copy(self):
    """Fixed __copy__ method for BaseContext to work with Python 3.14"""
    # Create a new instance without calling parent's __copy__
    duplicate = self.__class__.__new__(self.__class__)

    # Copy all attributes from the original instance
    duplicate.__dict__.update(self.__dict__)

    # Make sure dicts is a copy, not a reference
    if hasattr(self, 'dicts'):
        duplicate.dicts = self.dicts[:]

    return duplicate


# Apply the monkey patch
django.template.context.BaseContext.__copy__ = new_context_copy

print("✅ Applied Python 3.14 compatibility patch for Django")