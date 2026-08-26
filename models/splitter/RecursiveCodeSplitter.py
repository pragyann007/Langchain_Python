from langchain_text_splitters import RecursiveCharacterTextSplitter,Language

py = """
    # Take an integer input from the user
number = int(input("Enter a number: "))

# Check if the number is perfectly divisible by 2
if number % 2 == 0:
    print(f"{number} is an Even number.")
else:
    print(f"{number} is an Odd number.")
# Check if the number is perfectly divisible by 2
if number % 2 == 0:
    print(f"{number} is an Even number.")
else:
    print(f"{number} is an Odd number.")

# Check if the number is perfectly divisible by 2
if number % 2 == 0:
    print(f"{number} is an Even number.")
else:
    print(f"{number} is an Odd number.")



"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=50,
    chunk_overlap=2
)

print(splitter.split_text(py))