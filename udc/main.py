import typer
main = typer.Typer()

@main.command()
def list(uri: str, verbose: bool = False):
    typer.echo(f"Listing {uri}!")

if __name__ == "__main__":
    main()
