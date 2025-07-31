from src.mock_array import Array

def main():
    print("Creating array with max size 2...")
    arr = Array(max_size=2)

    print("Appending values: 10, 20, 30 (should trigger resize)...")
    arr.append(10)
    arr.append(20)
    arr.append(30)

    print(f"Current index: {arr.index}")
    print("Retrieving values:")
    for i in range(arr.index + 1):
        print(f"arr[{i}] = {arr.get(i)}")

    print("\nInserting 99 at position 1...")
    arr.insert(99, 1)
    print(f"arr[1] = {arr.get(1)}")

    print("\nTrying to access private method and attribute (will raise errors):")
    try:
        print(arr.__resize)
    except AttributeError as e:
        print(f"Access denied to __resize: {e}")

    try:
        print(arr.__instance_count)
    except AttributeError as e:
        print(f"Access denied to __instance_count: {e}")

    print("\nAccessing instance count through class method:")
    print("Array.get_instance_count() =", Array.get_instance_count())

if __name__ == "__main__":
    main()

