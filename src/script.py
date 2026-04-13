import os

def generate_output_file(output_path: str = "output.txt") -> str:   
    # Content to write to the file
    content = """Output Generated file"""
    
    output_dir = os.path.dirname(output_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Successfully generated: {output_path}")    
    return output_path


def main():
    output_file = "output.txt"
    
    print("=" * 50)
    print("Starting file generation...")
    print("=" * 50)
    
    generated_path = generate_output_file(output_file)
    
    print("=" * 50)
    print(f"File generation complete: {generated_path}")
    print("=" * 50)


if __name__ == "__main__":
    main()