from anyio import run
from functools import wraps

import typer

class AsyncTyper(typer.Typer):
    def async_command(self, *args, **kwargs):
        def decorator(async_func):
            @wraps(async_func)
            async def coro_wrapper():
                return await async_func(*args, **kwargs)

            self.command(*args, **kwargs)(coro_wrapper)
            return async_func

        return decorator

app = AsyncTyper()

@app.async_command()
async def list(uri: str, verbose: bool = False):
    typer.echo(f"Listing {uri}!")

if __name__ == "__main__":
    app()
