from typing import List

def is_palindrome(s: str) -> bool:
    """Return True if s reads the same forward and backward (case-insensitive, alnum only)."""
    cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]

def chunk(lst: List[int], size: int) -> List[List[int]]:
    """Split list into chunks of given size (>0)."""
    if size <= 0:
        raise ValueError("size must be > 0")
    return [lst[i:i+size] for i in range(0, len(lst), size)]

def mean(nums: List[float]) -> float:
    """Compute the arithmetic mean of a non-empty list."""
    if not nums:
        raise ValueError("nums must be non-empty")
    return sum(nums) / len(nums)
