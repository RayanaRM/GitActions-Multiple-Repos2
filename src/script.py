import os


def read_input_file(input_path: str) -> str:
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    return content


def generate_output_file(input_content: str, output_path: str = "generated_file_from_repo2.txt") -> str:
    content = f"""The file 'generated_file_from_repo1.txt' was successfully read.

Content of the file:
---
{input_content}
---
"""
    
    output_dir = os.path.dirname(output_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Successfully generated: {output_path}")
    return output_path


def main():
    input_file = "generated_file_from_repo1.txt"
    output_file = "generated_file_from_repo2.txt"
    
    print("=" * 50)
    print("Starting file processing...")
    print("=" * 50)
    
    input_content = read_input_file(input_file)
    
    generated_path = generate_output_file(input_content, output_file)
    
    print("=" * 50)
    print(f"File generation complete: {generated_path}")
    print("=" * 50)


if __name__ == "__main__":
    main()