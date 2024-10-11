import click


@click.group()
@click.version_option("0.1.0", prog_name="iac_jenkins_assistant")
def main():
    click.echo("Running toplevel command")


@click.option("--name", required=True, type=str)
@main.command()
def create_template(name: str):
    data = {"name": name}
    click.echo(data)


@main.command()
@click.option("--template_name", required=True, type=str)
@click.option("--number_of_machines", required=True, type=int)
def deploy_infra(template_name: str, number_of_machines: int):
    data = {"template_name": template_name, "number_of_machines": number_of_machines}
    click.echo(data)


if __name__ == "__main__":
    main()
