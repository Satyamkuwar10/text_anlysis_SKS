import re
from collections import Counter

def analyze_text_file(file_path):
    # Initialize counters
    line_count = 0
    word_count = 0
    char_count = 0
    word_frequency = Counter()

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                # Count lines
                line_count += 1
                
                # Count characters
                char_count += len(line)
                
                # Process words in the line
                words = re.findall(r'\w+', line.lower())  # Extract words and convert to lowercase
                word_count += len(words)
                word_frequency.update(words)  # Update word frequency


        results = {
            "Total Lines": line_count,
            "Total Words": word_count,
            "Total Characters": char_count,
            "Word Frequency": word_frequency.most_common(10)  
        }

        return results

    except FileNotFoundError:
        return f"Error: The file '{file_path}' was not found."
    except Exception as e:
        return f"An error occurred: {str(e)}"

def display_results(results):
    print("=== Text File Analysis Results ===")
    print(f"Total Lines: {results['Total Lines']}")
    print(f"Total Words: {results['Total Words']}")
    print(f"Total Characters: {results['Total Characters']}")
    
    print("\nWord Frequency Distribution (Top 10):")
    for word, frequency in results['Word Frequency']:
        print(f"{word}: {frequency}")

# Example usage
if __name__ == "__main__":
    file_path = 'C:\Users\admin\Desktop\Sainket Systems\text_anlysis.py'  # Replace with your text file path
    analysis_results = analyze_text_file(file_path)
    
    if isinstance(analysis_results, dict):
        display_results(analysis_results)
    else:
        print(analysis_results)
