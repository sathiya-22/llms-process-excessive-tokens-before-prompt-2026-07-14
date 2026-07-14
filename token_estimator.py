import tiktoken
import click
import os

def num_tokens_from_string(string: str, encoding_name: str = "cl100k_base") -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

@click.command()
@click.argument('texts_or_files', nargs=-1, required=True, type=str)
@click.option('--file', '-f', 'is_file', is_flag=True, help='Treat arguments as file paths instead of direct text strings.')
@click.help_option('--help', '-h')
def estimate_tokens(texts_or_files, is_file):
    """
    Estimates the number of tokens for given text strings or content from files.

    Example:
    token_estimator.py "Hello, world!"
    token_estimator.py --file my_prompt.txt
    token_estimator.py -f system_prompt.txt "User query here." -f another_file.md
    """
    total_tokens = 0
    items_processed = []

    for item in texts_or_files:
        content = ""
        item_name = item
        
        if is_file:
            if not os.path.exists(item):
                click.echo(f"Error: File not found: {item}", err=True)
                continue
            try:
                with open(item, 'r', encoding='utf-8') as f:
                    content = f.read()
                items_processed.append(f"File: {item}")
            except Exception as e:
                click.echo(f"Error reading file {item}: {e}", err=True)
                continue
        else:
            content = item
            items_processed.append(f"Text: '{item[:50]}...'") # Show first 50 chars for text

        tokens = num_tokens_from_string(content)
        click.echo(f"'{item_name}' contains {tokens} tokens.")
        total_tokens += tokens

    click.echo("\n--- Summary ---")
    click.echo(f"Total tokens across all inputs: {total_tokens}")
    click.echo(f"Inputs processed: {len(items_processed)}")


if __name__ == '__main__':
    estimate_tokens()
