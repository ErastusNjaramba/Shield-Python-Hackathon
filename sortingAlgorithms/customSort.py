def custom_sort(data, sort_key):
    return sorted(data, key=lambda x: x[sort_key])

# Example usage:
data = [
    {"name": "Alice", "age": 25, "height": 160},
    {"name": "Bob", "age": 20, "height": 175},
    {"name": "Charlie", "age": 23, "height": 168}
]
sorted_data = custom_sort(data, "age")
print("Sorted data by age:", sorted_data)
