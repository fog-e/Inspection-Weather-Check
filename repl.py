# repl.py
from gpt_api import generate_text
from file_io import read_file, write_file

def repl():
    print("Welcome to the Bee Inspection Weather Check App! Type 'help' for commands.")
    
    while True:
        command = input("> ").strip().lower()
        
        if command == 'exit':
            print("Goodbye!")
            break
        elif command == 'help':
            print("Available commands:\n"
                  "help - Show this help message\n"
                  "exit - Exit the application\n"
                  "generate - Generate text using LLM\n"
                  "read <file> - Read text from a file\n"
                  "write <file> - Write generated text to a file")
        elif command.startswith('read '):
            file_path = command.split(' ', 1)[1]
            try:
                content = read_file(file_path)
                print(f"Content of {file_path}:\n{content}")
            except FileNotFoundError:
                print(f"File {file_path} not found.")
        elif command.startswith('write '):
            file_path = command.split(' ', 1)[1]
            prompt = input("Enter the text to write: ")
            write_file(file_path, prompt)
            print(f"Text written to {file_path}")
        elif command == 'generate':
            zip_code = input("Enter your 5-digit zip code: ")
            prompt = f"Provide weather advice for beekeeping in zip code {zip_code}"
            result = generate_text(prompt)
            print(f"Generated text:\n{result}")
        else:
            print("Unknown command. Type 'help' for a list of available commands.")

if __name__ == '__main__':
    repl()
