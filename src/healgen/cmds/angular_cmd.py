import dspy
import typer
from pathlib import Path

from dspy import Signature

from healgen.utils.cli_tools import run_command
from healgen.utils.dspy_tools import init_dspy

app = typer.Typer()


def write_to_file(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)


@app.command(name="component")
def angular_component(user_story: str):
    """Generate an Angular component"""
    name = ""  # Create by language model
    content = f"""import {{ Component }} from '@angular/core';

@Component({{
  selector: 'app-{name}',
  templateUrl: './{name}.component.html',
  styleUrls: ['./{name}.component.css']
}})
export class {name.capitalize()}Component {{

}}
"""
    write_to_file(Path(f"src/app/{name}/{name}.component.ts"), content)
    write_to_file(Path(f"src/app/{name}/{name}.component.html"), f"<p>{name} works!</p>")
    write_to_file(Path(f"src/app/{name}/{name}.component.css"), f"/* Styles for {name} component */")
    typer.echo(f"Component {name} created.")


@app.command(name="service")
def angular_service(name: str):
    """Generate an Angular service"""
    content = f"""import {{ Injectable }} from '@angular/core';

@Injectable({{
  providedIn: 'root'
}})
export class {name.capitalize()}Service {{

  constructor() {{ }}

}}
"""
    write_to_file(Path(f"src/app/services/{name}.service.ts"), content)
    typer.echo(f"Service {name} created.")


@app.command(name="module")
def angular_module(name: str):
    """Generate an Angular module"""
    content = f"""import {{ NgModule }} from '@angular/core';
import {{ CommonModule }} from '@angular/common';
import {{ {name.capitalize()}Component }} from './{name}.component';

@NgModule({{
  declarations: [{name.capitalize()}Component],
  imports: [
    CommonModule
  ]
}})
export class {name.capitalize()}Module {{ }}
"""
    write_to_file(Path(f"src/app/{name}/{name}.module.ts"), content)
    typer.echo(f"Module {name} created.")


@app.command(name="directive")
def angular_directive(name: str):
    """Generate an Angular directive"""
    content = f"""import {{ Directive }} from '@angular/core';

@Directive({{
  selector: '[app{name.capitalize()}]'
}})
export class {name.capitalize()}Directive {{

  constructor() {{ }}

}}
"""
    write_to_file(Path(f"src/app/directives/{name}.directive.ts"), content)
    typer.echo(f"Directive {name} created.")


@app.command(name="pipe")
def angular_pipe(name: str):
    """Generate an Angular pipe"""
    content = f"""import {{ Pipe, PipeTransform }} from '@angular/core';

@Pipe({{
  name: '{name}'
}})
export class {name.capitalize()}Pipe implements PipeTransform {{

  transform(value: unknown, ...args: unknown[]): unknown {{
    return null;
  }}

}}
"""
    write_to_file(Path(f"src/app/pipes/{name}.pipe.ts"), content)
    typer.echo(f"Pipe {name} created.")


@app.command(name="guard")
def angular_guard(name: str):
    """Generate an Angular guard"""
    content = f"""import {{ Injectable }} from '@angular/core';
import {{ CanActivate, ActivatedRouteSnapshot, RouterStateSnapshot, UrlTree }} from '@angular/router';
import {{ Observable }} from 'rxjs';

@Injectable({{
  providedIn: 'root'
}})
export class {name.capitalize()}Guard implements CanActivate {{
  canActivate(
    route: ActivatedRouteSnapshot,
    state: RouterStateSnapshot): Observable<boolean | UrlTree> | Promise<boolean | UrlTree> | boolean | UrlTree {{
    return true;
  }}
}}
"""
    write_to_file(Path(f"src/app/guards/{name}.guard.ts"), content)
    typer.echo(f"Guard {name} created.")


@app.command(name="interceptor")
def angular_interceptor(name: str):
    """Generate an Angular interceptor"""
    content = f"""import {{ Injectable }} from '@angular/core';
import {{ HttpEvent, HttpInterceptor, HttpHandler, HttpRequest }} from '@angular/common/http';
import {{ Observable }} from 'rxjs';

@Injectable()
export class {name.capitalize()}Interceptor implements HttpInterceptor {{

  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {{
    const clonedRequest = req.clone();
    return next.handle(clonedRequest);
  }}
}}
"""
    write_to_file(Path(f"src/app/interceptors/{name}.interceptor.ts"), content)
    typer.echo(f"Interceptor {name} created.")


@app.command()
def routing_module(name: str):
    """Generate an Angular routing module"""
    content = f"""import {{ NgModule }} from '@angular/core';
import {{ RouterModule, Routes }} from '@angular/router';
import {{ {name.capitalize()}Component }} from './{name}.component';

const routes: Routes = [
  {{ path: '', component: {name.capitalize()}Component }}
];

@NgModule({{
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
}})
export class {name.capitalize()}RoutingModule {{}}
"""
    write_to_file(Path(f"src/app/{name}/{name}-routing.module.ts"), content)


@app.command()
def ng_module(name: str):
    """Generate an Angular NgModule"""
    content = f"""import {{ NgModule }} from '@angular/core';
import {{ CommonModule }} from '@angular/common';
import {{ {name.capitalize()}RoutingModule }} from './{name}-routing.module';
import {{ {name.capitalize()}Component }} from './{name}.component';
import {{ FormsModule }} from '@angular/forms';
import {{ HttpClientModule }} from '@angular/common/http';

@NgModule({{
  declarations: [{name.capitalize()}Component],
  imports: [
    CommonModule,
    {name.capitalize()}RoutingModule,
    FormsModule,
    HttpClientModule
  ]
}})
export class {name.capitalize()}Module {{}}
"""
    write_to_file(Path(f"src/app/{name}/{name}.module.ts"), content)


@app.command()
def forms_module(name: str):
    """Generate an Angular Forms Module"""
    write_to_file(Path(f"src/app/{name}/{name}.module.ts"), f"import {{ FormsModule }} from '@angular/forms';\n")


@app.command()
def http_client_module(name: str):
    """Generate an Angular HttpClientModule"""
    write_to_file(Path(f"src/app/{name}/{name}.module.ts"), f"import {{ HttpClientModule }} from '@angular/common/http';\n")


@app.command(name="readme")
def generate_readme(project_charter: str):
    """Generate a README file for the Angular project."""
    init_dspy()
    pred = dspy.Predict("project_charter -> readme")
    content = pred.forward(project_charter=project_charter).readme
    write_to_file(Path("src/app/README.md"), content)


class GenerateProjectStructure(Signature):
    """Generate the project structure section for the README file.
    """
    readme = dspy.InputField(desc="The README file for the project.")
    angular_project_structure = dspy.OutputField(desc="The project structure section for the README file. "
                                                      "This is for an Angular project. It must include all files "
                                                      "in the project and their locations.",
                                                 prefix="## Project Structure\n\n")

# Create the project structure section for the readme
@app.command(name="structure")
def generate_structure(readme: Path = typer.Argument("src/app/README.md")):
    """Generate the project structure section for the README file."""
    init_dspy(model="gpt-4o")
    content = """## Project Structure"""
    pred = dspy.ChainOfThought(GenerateProjectStructure)
    content += pred.forward(readme=readme.read_text()).angular_project_structure
    write_to_file(Path("src/app/README.md"), content)


@app.command(name="feature", help="Generate an Angular feature.")
def generate_feature(feature_name: str):
    """Generate an Angular feature with the given name."""
    commands = [
        f"healgen angular component {feature_name}",
        f"healgen angular service {feature_name}",
        f"healgen angular module {feature_name}",
        "healgen angular directive highlight",
        "healgen angular pipe filter",
        "healgen angular guard auth",
        "healgen angular interceptor auth",
    ]

    for command in commands:
        typer.echo(f"Executing: {command}")
        run_command(command)

    typer.echo(f"Feature {feature_name} for the medical system has been generated.")


if __name__ == "__main__":
    app()
