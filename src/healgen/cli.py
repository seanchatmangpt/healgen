"""HealGen CLI."""

import typer
from jinja2 import Template
from rich import print
from typer import Typer

from healgen.utils.cli_tools import load_commands
from healgen.utils.path_tools import project_root

app = typer.Typer()


if __name__ == "__main__":
    load_commands()
    app()
else:
    load_commands()



# @app.command()
# def fire(name: str = "Chell") -> None:
#     """Fire portal gun."""
#     print(project_root())
#     print(f"[bold red]Alert![/bold red] {name} fired [green]portal gun[/green] :boom:")


# @app.command(name="code")
# def gen_code_with_jinja(
#     namespace: str = typer.Option("HealGen", help="Namespace for the controller"),
#     controller_name: str = typer.Option("WeatherForecastController", help="Name of the controller"),
#     endpoint: str = typer.Option("weather-forecast", help="Endpoint for the controller"),
#     method_name: str = typer.Option("PostWeatherForecast", help="Name of the method"),
#     model_name: str = typer.Option("WeatherForecast", help="Name of the model"),
# ) -> None:
#     """Generate code with Jinja for Dapr .NET endpoint."""
#     print("[bold blue]Generating code with Jinja[/bold blue]")
#
#     code_template = """
#     using Microsoft.AspNetCore.Mvc;
#     using Dapr.Client;
#     using System.Threading.Tasks;
#
#     namespace {{ namespace }}
#     {
#         [ApiController]
#         [Route("[controller]")]
#         public class {{ controller_name }} : ControllerBase
#         {
#             private readonly DaprClient _daprClient;
#
#             public {{ controller_name }}(DaprClient daprClient)
#             {
#                 _daprClient = daprClient;
#             }
#
#             [HttpPost("{{ endpoint }}")]
#             public async Task<IActionResult> {{ method_name }}([FromBody] {{ model_name }} forecast)
#             {
#                 // Process the message
#                 await Task.Yield(); // Placeholder for actual processing logic
#
#                 return Ok();
#             }
#         }
#
#         public class {{ model_name }}
#         {
#             public DateTime Date { get; set; }
#             public int TemperatureC { get; set; }
#             public string Summary { get; set; }
#         }
#     }
#     """
#
#     template = Template(code_template)
#
#     rendered_code = template.render(
#         namespace=namespace,
#         controller_name=controller_name,
#         endpoint=endpoint,
#         method_name=method_name,
#         model_name=model_name
#     )
#
#     with open("DaprNetApiController.cs", "w") as f:
#         f.write(rendered_code)
#
#     print("[bold green]Code generation complete! Check DaprNetApiController.cs[/bold green]")
#
