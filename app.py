import pandas as pd

df = pd.read_csv("cars.csv")

# Sort the DataFrame by the 'model' column in ascending order (A-Z)
df_sorted = df.sort_values(by="model")

# Display the first few rows of the sorted DataFrame
# print(df_sorted.head())

# Optionally save the sorted data to a new CSV file
df_sorted.to_csv("sorted_cars.csv", index=False)
# print("Data sorted by model and saved to 'sorted_cars.csv'")

def binary_search(data, target):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = data[mid]
        
        if mid_value == target:
            return mid  # Target found
        elif mid_value < target:
            low = mid + 1  # Search in the right half
        else:
            high = mid - 1  # Search in the left half

    return -1  # Target not found

ar = [0,4,6,0,1,9,9,0,9,9,0]

def search_higest_sum():
    is_zero = False
    # second_zero = False
    temp_sum = 0
    biggest_sum = 0
    for num in ar:
        if num == 0:
            if is_zero == False: 
                print('true')
                is_zero = True
            elif is_zero == True:
                print(temp_sum, biggest_sum)
                if temp_sum > biggest_sum: biggest_sum = temp_sum
                is_zero = False
                temp_sum = 0
        elif is_zero == True:
            temp_sum += num
    return biggest_sum




if __name__ == '__main__':
    df_sorted = pd.read_csv("sorted_cars.csv")

# Convert the 'model' column to a list
    model_list = df_sorted["model"].tolist()

# Define the model to search for
    target_model = "Enclave"

# Perform the binary search
    index = binary_search(model_list, target_model)

    if index != -1:
        print(f"Model '{target_model}' found at index {index}:")
        print(df_sorted.iloc[index])
    else:
        print(f"Model '{target_model}' not found.")
    # print(search_higest_sum())